"""Read-only live terminal log for the five dataset workers. Ctrl+C exits only this viewer."""
import argparse
import ctypes
from datetime import datetime
import json
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / 'output/parallel_dataset'
STAGES = ROOT / 'krugrade-questions-pipeline/CEDT_KruGradeAI_Direct_Pipeline/question_generation/output/university_math_1000/stages'
COLORS = ('96','92','93','95','94')
NAMES = ('CYAN','GREEN','YELLOW','MAGENTA','BLUE')


def enable_color():
    if not sys.stdout.isatty(): return False
    if os.name != 'nt': return True
    kernel = ctypes.windll.kernel32
    handle = kernel.GetStdHandle(-11)
    mode = ctypes.c_ulong()
    if not kernel.GetConsoleMode(handle, ctypes.byref(mode)): return False
    return bool(kernel.SetConsoleMode(handle, mode.value | 4))


def read_json(path):
    try: return json.loads(path.read_text(encoding='utf-8'))
    except (OSError, ValueError): return None


class Tail:
    def __init__(self):
        self.offsets = {}
        self.pending = {}

    def read(self, path):
        try:
            size = path.stat().st_size
            first = path not in self.offsets
            offset = self.offsets.get(path, max(0,size-4096))
            if size < offset: offset=0; self.pending[path]=b''
            with path.open('rb') as stream:
                stream.seek(offset)
                content=stream.read()
                self.offsets[path]=stream.tell()
            if first and offset:
                content=content.partition(b'\n')[2]
            content=self.pending.get(path,b'')+content
            lines=content.split(b'\n')
            self.pending[path]=lines.pop()
            decoded=[line.decode('utf-8',errors='replace').rstrip('\r') for line in lines]
            return decoded[-5:] if first else decoded
        except OSError: return []


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--once',action='store_true',help='Print a single snapshot for diagnostics')
    parser.add_argument('--no-color',action='store_true')
    parser.add_argument('--interval',type=float,default=1.0)
    args=parser.parse_args()
    if args.interval < 0.2: parser.error('--interval must be at least 0.2 seconds')
    color=not args.no_color and enable_color()
    if sys.stdout.isatty() and os.name=='nt':
        ctypes.windll.kernel32.SetConsoleTitleW('KruGrade | 5 workers | Live logs')

    def emit(label,message,worker=None,error=False):
        prefix=f'[{datetime.now():%H:%M:%S}] [{label}] '
        code='91;1' if error else (COLORS[worker] if worker is not None else '97')
        text=prefix+message
        print(f'\033[{code}m{text}\033[0m' if color else text,flush=True)

    emit('MONITOR','LIVE: 1-second polling | Ctrl+C / close this window stops only the viewer')
    emit('MONITOR','Shows state changes, saved generation stages, and answer/evaluation logs; not model token streaming.')
    for index in range(5): emit(f'W{index}',NAMES[index],index)
    tail=Tail(); last={}; stage_seen=set(); last_summary=0; previous_summary=None
    watched={}; last_wait={}; supervisor_seen=None
    try:
        while True:
            current=time.monotonic()
            summary=read_json(OUTPUT/'status.json')
            if summary:
                counts=summary.get('outputs',{})
                key=(summary.get('status'),summary.get('completed_questions'),counts.get('new_samples.csv'),
                     counts.get('training_candidates.csv'),counts.get('review_queue.csv'))
                if key!=previous_summary or current-last_summary>=30:
                    emit('TOTAL',f"status={key[0]} | completed={key[1]}/{summary.get('target_questions',1000)} "
                         f"| samples={key[2]} | candidates={key[3]} | review={key[4]} "
                         f"| exporter_updated={summary.get('updated_at','?')}")
                    previous_summary=key;last_summary=current
            for index in range(5):
                state=read_json(OUTPUT/f'worker-{index}.json')
                if not state:
                    if index not in last: emit(f'W{index}','Waiting for worker status file',index);last[index]=None
                    continue
                qid=state.get('question_id','-')
                state_key=(qid,state.get('phase'),state.get('status'),state.get('completed'),state.get('error'))
                changed=state_key!=last.get(index)
                if changed or current-last_wait.get(index,0)>=30:
                    emit(f'W{index}',f"{state.get('status')} | {qid} | {state.get('phase')} "
                         f"| done={state.get('completed',0)}/{state.get('assigned',200)} "
                         f"| updated={state.get('updated_at','?')}",index,state.get('status')=='error')
                    if changed and state.get('error'): emit(f'W{index}',state['error'],index,True)
                    last[index]=state_key;last_wait[index]=current
                if qid=='-': continue
                for phase in ('questions','solutions','rubrics','review'):
                    path=STAGES/qid/(phase+'.json')
                    marker=(index,qid,phase)
                    if marker not in stage_seen and path.is_file():
                        data=read_json(path)
                        if data:
                            detail=(' verdict='+str(data.get('result',{}).get('status'))) if phase=='review' else ''
                            emit(f'W{index}',f'{qid} | saved {phase}{detail}',index)
                            stage_seen.add(marker)
                job=OUTPUT/'jobs'/qid
                # Keep previous question logs watched so a final line cannot be
                # missed if the worker moves on between polling ticks.
                for name in ('answers.log','evaluation.log'):
                    watched[(index,job/name)]=qid
            for (index,path),qid in list(watched.items()):
                for line in tail.read(path):
                    if line.strip():
                        bad=any(word in line.lower() for word in ('failed','traceback','error:'))
                        emit(f'W{index}',f'{qid[-5:]} / {path.name}: {line}',index,bad)
            for line in tail.read(OUTPUT/'supervisor.stderr.log'):
                if line.strip(): emit('EXPORTER',line,error=True)
            if args.once: break
            time.sleep(args.interval)
    except KeyboardInterrupt:
        emit('MONITOR','Viewer closed. Dataset workers continue running.')


if __name__=='__main__': main()
