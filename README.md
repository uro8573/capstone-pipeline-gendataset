# KruGrade Dataset Generation Pipelines

Pipeline สร้าง dataset สำหรับ AI Grader วิชาคณิตศาสตร์มหาวิทยาลัย: โจทย์ → เฉลย → rubric → ตรวจโจทย์ → คำตอบนักเรียนจำลอง → ให้คะแนน → ประเมินซ้ำ → คัดข้อมูลและแบ่ง train/validation/test

ใช้ Python standard library และ Codex CLI สามารถรันแบบลำดับหรือ 5 Docker workers ได้ คะแนนทั้งหมดเป็น **synthetic labels ที่ยังไม่ได้ยืนยันโดยมนุษย์** การผ่าน AI review ไม่เท่ากับ human-verified ground truth

## ผลรอบ 200 โจทย์ล่าสุด

รอบนี้ประมวลผลครบเมื่อ **15 พฤศจิกายน 2026 เวลา 04:04 น. (Asia/Bangkok)** และ workers ถูกหยุดแล้ว ตัวเลขต่อไปนี้เป็นผลของรอบที่บันทึกไว้ ไม่ใช่จำนวนที่รับประกันเมื่อรันใหม่

| รายการ | จำนวน |
|---|---:|
| โจทย์ตามแผน / ประมวลผลครบ | 200 / 200 |
| ผ่านการสร้างและ review โจทย์ | 191 |
| โจทย์รอ review ตั้งแต่ขั้นสร้าง | 9 |
| คำตอบนักเรียนที่สร้างและประเมิน | 955 แถว |
| Training candidates หลังคัด | **686 แถว จาก 172 โจทย์** |
| Train / Validation / Synthetic test | 536 / 79 / 71 แถว |
| FULL / PARTIAL / WRONG ใน candidates | 168 / 408 / 110 แถว |
| PARTIAL ต่ำ / กลาง / สูง ใน candidates | 126 / 137 / 145 แถว |

ตรวจไฟล์ candidates แล้ว: ฟิลด์หลักครบ คะแนนรวมตรงผลรวมคะแนนรายเกณฑ์ ไม่มี response ID ซ้ำ และไม่มี family ข้าม split ทั้ง 686 แถวยังคงเป็น `label_review_status=unreviewed`

**`finished` หมายถึงประมวลผลทุกโจทย์ตามแผนแล้ว** รวมโจทย์ที่ถูกกันไว้ review ไม่ได้หมายความว่าทุกโจทย์ผ่าน หรือได้คำตอบครบเป้าหมาย 1,000 แถว ไฟล์ผลลัพธ์และฐานประวัติไม่ได้รวมอยู่ใน Git ผู้ที่ clone จะได้โค้ดและชุดตัวอย่างที่ติดตามไว้ ไม่ได้รับผลรอบนี้โดยอัตโนมัติ

## โครงสร้าง

| Path | หน้าที่ |
|---|---|
| `parallel_dataset.py` | แบ่งงาน 5 workers, checkpoint, เลือก 200 ข้อ และรวมผลฝั่ง host |
| `docker-compose.workers.yml` | Docker services `worker0`–`worker4` |
| `watch_workers.py`, `watch_workers.cmd` | Live logs แยกสี อ่านอย่างเดียว |
| `run_full_dataset.py` | ตัวรันแบบลำดับสำหรับแผน 1,000 ข้อ |
| `krugrade-questions-pipeline/CEDT_KruGradeAI_Direct_Pipeline/question_generation` | แผนโจทย์ เฉลย rubric, review และ duplicate registry |
| `krugrade-questions-pipeline/CEDT_KruGradeAI_Direct_Pipeline/answer_generation` | Direct answer pipeline: FULL/PARTIAL/WRONG |
| `krugrade-eval-pipeline/krugrade-eval-pipeline` | ประเมินโจทย์และให้คะแนนคำตอบซ้ำ คัด training candidates |
| `krugrade-answer-pipeline/krugrade-codex-pipeline` | Legacy answer pipeline: PARTIAL เท่านั้น |

## เริ่มจาก clone ใหม่: 200 โจทย์ / 5 workers

ต้องมี **Python 3.10+**, Docker Desktop/Engine ที่กำลังทำงาน และ Codex CLI ที่ล็อกอินด้วยบัญชีของผู้รันแล้ว (`codex login`) การสร้างจริงใช้โควต้าของบัญชีนั้น โค้ด Python ไม่ต้องติดตั้ง pip dependencies

Image ใช้ Node 22, Python 3 จาก Debian และ Codex CLI `0.169.0` ส่วนโมเดลและ reasoning กำหนดใน `.env.workers` ต้องเป็นโมเดลที่บัญชีของคุณใช้งานได้ ไม่ต้องใส่ token หรือรหัสผ่านใน repo

รันจาก root ของ repository:

```powershell
git clone https://github.com/uro8573/capstone-pipeline-gendataset.git
cd capstone-pipeline-gendataset
Copy-Item .env.workers.example .env.workers
```

แก้ `CODEX_AUTH_FILE` ใน `.env.workers` ให้ชี้ไปยังไฟล์ `auth.json` ของคุณด้วย absolute path เช่น `C:/Users/YOUR_USER/.codex/auth.json` และตรวจชื่อโมเดลก่อนเริ่ม สำหรับ Linux ใช้ path เช่น `/home/YOUR_USER/.codex/auth.json`

```powershell
# เตรียมแผนและเลือกชุด 200 ข้อ: สองคำสั่งนี้ยังไม่เรียก AI
python -B -X utf8 parallel_dataset.py prepare
python -B -X utf8 parallel_dataset.py reduce-to-200

# Build ครั้งแรก แล้วเริ่ม workers
docker compose --env-file .env.workers -f docker-compose.workers.yml build worker0
docker compose --env-file .env.workers -f docker-compose.workers.yml up -d --no-build

# เปิดตัวรวมผลบน host ค้างไว้ (ใช้ terminal อีกหน้าต่างสำหรับดู log)
python -B -X utf8 parallel_dataset.py supervise
```

ชุดย่อยเลือก **10 หมวด หมวดละ 20 ข้อ** รวม 200 ข้อ โดยเก็บ family สองข้อไว้ด้วยกันและรักษา split เดิม: train 160 / validation 20 / test 20 **ก่อนคัดกรอง** แต่ละ worker รับผิดชอบ 40 ข้อ ไม่มีการหยิบโจทย์เดียวกันซ้ำ ตัวเลือกถูกบันทึกใน `output/parallel_dataset/selection.json`

หากเปลี่ยนจากรอบ 1,000 ข้อที่กำลังรัน ต้องให้ workers และ supervisor หยุดก่อนใช้ `reduce-to-200` ระบบให้ความสำคัญกับ family ที่เริ่มทำแล้ว และจะรายงานข้อผิดพลาดหากไม่สามารถรักษาข้อมูลเดิมภายใต้โควต้าชุดย่อยได้

ต้องเปิดเครื่อง เชื่อมต่ออินเทอร์เน็ต และให้ Docker กับ supervisor ทำงานต่อเนื่อง หากไม่เลือกชุดย่อย แผนเริ่มต้นเป็น 1,000 ข้อ ห้ามเปิด `run_full_dataset.py` พร้อมกับตัวรันขนาน

ชื่อโฟลเดอร์ stages ยังเป็น `question_generation/output/university_math_1000` แม้เลือก 200 ข้อ เพื่อใช้ checkpoint และประวัติตรวจซ้ำเดิมต่อ ให้ดู `target_questions` ในสถานะของ parallel run เป็นจำนวนเป้าหมายจริง

## การสร้างคำตอบและการคัดข้อมูล

ค่าเริ่มต้น `--mode balanced --count 5` ตั้งเป้าต่อโจทย์เป็น FULL 1, PARTIAL ต่ำ/กลาง/สูงอย่างละ 1 และ WRONG 1

| ประเภท / ช่วง | เกณฑ์จากคะแนนจริง |
|---|---|
| FULL | คะแนนเต็มตาม rubric |
| WRONG | 0 คะแนน |
| PARTIAL ต่ำ | มากกว่า 0 แต่น้อยกว่า 1/3 ของคะแนนเต็ม |
| PARTIAL กลาง | ตั้งแต่ 1/3 แต่น้อยกว่า 2/3 |
| PARTIAL สูง | ตั้งแต่ 2/3 แต่น้อยกว่าคะแนนเต็ม |

การสร้างคำตอบไม่ส่ง official solution ให้โมเดล จากนั้นใช้ call แยกเพื่อให้คะแนนตามคำตอบที่เขียนจริง ไม่ส่งประเภทหรือช่วงคะแนนเป้าหมายเข้า grader ถ้าคะแนนจริงไม่ตรงเป้า ให้เก็บคะแนนจริงและ flag `generation_target_mismatch` ไม่ปรับคะแนนหรือแก้คำตอบให้ตรงเป้า

Evaluator ให้คะแนนซ้ำโดยไม่เห็น `expected_score` แล้วจึงเปรียบเทียบด้วย Python Candidate ต้องมีฟิลด์หลักครบ โจทย์และคำตอบผ่าน AI review คะแนนรวม/รายเกณฑ์ตรงกัน และไม่มี target mismatch ความผิดพลาดของนักเรียนที่เหมาะสมกับ PARTIAL/WRONG ไม่ใช่เหตุให้ตัดทิ้งโดยตัวมันเอง

ไม่มีการสร้างทดแทนอัตโนมัติจนเต็มโควต้า จำนวนและการกระจายคะแนนหลังคัดจึงอาจต่ำกว่าเป้า ข้อผิดพลาดด้านรูปแบบข้อมูลถูกเก็บใน review queue ส่วนปัญหา provider/auth/การประมวลผลจะหยุดงานให้ตรวจและ resume

## ไฟล์ผลลัพธ์และฟิลด์สำคัญ

ผลรวมของรอบขนานอยู่ใน `output/parallel_dataset/`:

| ไฟล์ | เนื้อหา |
|---|---|
| `status.json`, `worker-0.json` … `worker-4.json` | สถานะ จำนวนงาน และข้อผิดพลาด |
| `new_samples.csv` | คำตอบที่ทำครบและอยู่ภายใต้โจทย์ที่ผ่านการตรวจซ้ำส่วนกลาง |
| `training_candidates.csv` | แถวที่ผ่านการคัดเบื้องต้นสำหรับตรวจใช้เทรน |
| `train.csv`, `validation.csv`, `test.csv` | Candidates แบ่งตาม family เดิม |
| `answer_evaluation.csv` | คะแนนตรวจซ้ำและผลประเมินรายคำตอบ |
| `review_queue.csv` | โจทย์/คำตอบที่ต้องตรวจต่อ |
| `jobs/<question_id>/` | Input ของแต่ละข้อ, raw stages, logs และรายงาน |

ฟิลด์หลักในแต่ละแถวคำตอบ:

- **หมวดวิชา:** `subject`, `topic`, `subtopic`, `concept_tags`
- **โจทย์:** `question_id`, `question_text`, `solution`, `final_answer`, `difficulty`, `question_type`
- **เกณฑ์และคะแนน:** `rubric_criteria`, `rubric_max_score`, `expected_score`, `rubric_analysis`
- **คำตอบ:** `response_id`, `answer_text`, `sample_type`, `grader_feedback`, `missed_concepts`
- **การแบ่งชุดและที่มา:** `family_id`, `split`, `data_origin`, `label_source`, `label_review_status`
- **เป้าหมายเทียบผลจริง:** `requested_sample_type`, `target_score_band`, `actual_score_band`, `generation_target_status`

บางฟิลด์เป็น JSON ในเซลล์ CSV เช่น `concept_tags`, `rubric_criteria`, `rubric_analysis`, `missed_concepts` ต้อง parse ก่อนใช้งาน ฟิลด์ optional อาจว่างได้ และ FULL ที่ไม่มีข้อผิดพลาดสามารถใช้ `not_applicable` สำหรับตำแหน่งที่ผิดได้

`topic` มี 10 หมวด: Single-variable Calculus, Multivariable Calculus, Linear Algebra, Differential Equations, Probability, Statistics, Discrete Mathematics, Numerical Methods, Optimization และ Complex Variables ส่วน `subtopic` ระบุเรื่องย่อย เช่น Linear systems, Eigenvalues and diagonalization, Hypothesis testing และ Linear programming หมวดมาจาก blueprint จึงยังควรตรวจความตรงกับเนื้อหาจริง

## Live logs, หยุด และ resume

เปิด `watch_workers.cmd` บน Windows หรือรัน:

```powershell
python -X utf8 watch_workers.py
```

ตัวดูอัปเดตทุก 1 วินาที: W0 ฟ้า, W1 เขียว, W2 เหลือง, W3 ม่วง, W4 น้ำเงิน และ error สีแดง แสดงสถานะ ขั้นที่บันทึกเสร็จและ log รายข้อ ไม่ใช่ token streaming ของโมเดล การปิดหน้าต่าง viewer ไม่หยุด workers

```powershell
# Raw Docker logs
docker compose --env-file .env.workers -f docker-compose.workers.yml logs -f

# หยุดแบบให้ข้อปัจจุบันทำเสร็จก่อน
New-Item -ItemType File -Force output/parallel_dataset/STOP

# หรือหยุด containers ทันที โดยยังเก็บข้อมูลไว้
docker compose --env-file .env.workers -f docker-compose.workers.yml stop
```

หลังแก้สาเหตุและ workers/supervisor หยุดแล้ว:

```powershell
python -B -X utf8 parallel_dataset.py resume
docker compose --env-file .env.workers -f docker-compose.workers.yml up -d --no-build
python -B -X utf8 parallel_dataset.py supervise
```

`resume` ใช้ขั้นที่เสร็จแล้วต่อและรักษาชุด 200 ข้อเดิม หากตั้งใจเปลี่ยนโค้ด ใช้ `resume --refresh-code` หลังหยุด workers; ระบบบันทึกประวัติ fingerprint ห้ามแก้ manifest เพื่อหลบการตรวจ config หากบังคับหยุดจนสถานะยังค้าง `running` ต้องตรวจว่า process หยุดจริงและจัดการสถานะก่อน resume

ตัวเขียนสถานะและ CSV รวมจะลอง atomic rename ซ้ำแบบจำกัดเวลาเมื่อเจอ Windows/Docker file lock ชั่วคราว ข้อผิดพลาดถาวรยังถูกรายงาน ไม่ข้ามการตรวจเงียบ ๆ

## การกันซ้ำและการใช้ร่วมกันหลาย clone

ตัวรวมผลบน host ตรวจประวัติใน `question_generation/output/question_registry.sqlite3` ก่อนเผยแพร่แถวลงชุดรวม โดยตรวจข้อความหลัง normalize, รูปแบบที่เปลี่ยนเฉพาะตัวเลข และข้อความใกล้เคียงตาม threshold 0.90 พร้อมบันทึกหลักฐานใน review queue การตรวจนี้ไม่ใช่การพิสูจน์ความสมมูลทางคณิตศาสตร์

**Clone โค้ดอย่างเดียวไม่ส่งต่อประวัติการสร้าง** เพราะ SQLite และ outputs ถูก ignore ผู้ร่วมทีมต้องรับ historical question CSV แล้ว import ก่อนรัน จากโฟลเดอร์ `question_generation`:

```powershell
python -B -m pipeline.question_registry --input PATH_TO_HISTORY.csv --registry output/question_registry.sqlite3 --dataset-id STABLE_HISTORY_DATASET_ID
```

ใช้ dataset ID คงที่สำหรับประวัติชุดเดียวกันเพื่อ import ซ้ำได้ CSV ต้องมี `question_id` และ `question_text`; ควรส่ง `family_id` และ `split` ด้วย การใช้ path ข้อความเดียวกันบนคนละเครื่องไม่ได้ทำให้เป็นฐานเดียวกัน

การสร้างรอบใหม่ด้วย question CLI ให้ใช้ config สำเนา เปลี่ยน `dataset_id`/`seed` และ output ใหม่ แต่เก็บ registry ประวัติไว้ การเปลี่ยน seed หรือ ID ไม่รับประกันว่าเนื้อหาไม่ซ้ำ ตัวรันขนานปัจจุบันผูกกับ run/selection ที่ freeze ไว้ ไม่ใช่ตัวสร้างรอบใหม่หลายรอบอัตโนมัติ

ยังไม่มีการ sync registry ข้ามเครื่องหรือ service กลาง และยังไม่มี semantic deduplication ด้วย embeddings หากหลายคนสร้างพร้อมกัน ต้องรวมประวัติและตรวจอีกครั้งก่อนรับเข้า dataset กลาง แนวทางที่วางไว้สำหรับอนาคตคือประวัติรายรอบแบบ JSONL, import อัตโนมัติ และการตรวจตอน merge ซึ่ง **ยังไม่ได้ implement**

## ทดสอบและคู่มือเพิ่มเติม

ทดสอบ offline จาก root:

```powershell
python -B -X utf8 -m unittest discover -s tests -v
```

แต่ละ pipeline มี `tests/` แยกกัน ให้รันคำสั่งเดียวกันจากโฟลเดอร์ question generation, direct answer, legacy answer และ evaluation ด้วย Tests ใช้ mock ไม่เรียก AI และไม่ยืนยันความถูกต้องทางคณิตศาสตร์ของข้อมูลจริง

- [คู่มือ 5 Docker workers](docker/parallel/README.md)
- [สร้างโจทย์ / config / duplicate registry](krugrade-questions-pipeline/CEDT_KruGradeAI_Direct_Pipeline/question_generation/BULK_GENERATION.md)
- [สร้างคำตอบ FULL/PARTIAL/WRONG](krugrade-questions-pipeline/CEDT_KruGradeAI_Direct_Pipeline/answer_generation/README.md)
- [การประเมินและคัด training candidates](krugrade-eval-pipeline/krugrade-eval-pipeline/README.md)

Synthetic test เป็นชุดทดสอบสังเคราะห์ ไม่ใช่ benchmark อิสระจากข้อมูลจริง ควรตรวจ labels และความครอบคลุมของหัวข้อก่อนนำไปสรุปประสิทธิภาพของ grader
