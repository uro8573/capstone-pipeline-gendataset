# KruGrade Dataset Generation Pipelines

เครื่องมือเตรียมโจทย์ เฉลย Rubric และคำตอบนักเรียนจำลอง รวมถึงตรวจคุณภาพข้อมูล
ก่อนนำไปฝึกหรือประเมิน AI Grader คะแนนและเฉลยที่ AI สร้างยังเป็นข้อมูลสังเคราะห์
ที่ต้องตรวจยืนยัน ไม่ถือเป็น human-verified ground truth โดยอัตโนมัติ

## โครงสร้าง

| โฟลเดอร์ | หน้าที่ |
|---|---|
| `krugrade-questions-pipeline/CEDT_KruGradeAI_Direct_Pipeline/question_generation` | เตรียมชุดเดิม หรือสร้างโจทย์ใหม่พร้อมเฉลย/Rubric และตรวจซ้ำ |
| `krugrade-questions-pipeline/CEDT_KruGradeAI_Direct_Pipeline/answer_generation` | สร้างคำตอบ PARTIAL จาก question dataset โดยตรง |
| `krugrade-answer-pipeline/krugrade-codex-pipeline` | สร้างคำตอบ PARTIAL เพิ่มจาก dataset รูปแบบเดิม |
| `krugrade-eval-pipeline/krugrade-eval-pipeline` | ตรวจโจทย์และให้คะแนนคำตอบใหม่ พร้อมส่งรายการที่มีปัญหาให้มนุษย์ตรวจ |

## สร้างโจทย์คณิตศาสตร์มหาวิทยาลัย 1,000 ข้อ

ตั้งค่าใน [generation.university_math.json](krugrade-questions-pipeline/CEDT_KruGradeAI_Direct_Pipeline/question_generation/config/generation.university_math.json)

- 10 หมวด หมวดละ 100 ข้อ: แคลคูลัสตัวแปรเดียว/หลายตัวแปร พีชคณิตเชิงเส้น
  สมการเชิงอนุพันธ์ ความน่าจะเป็น สถิติ คณิตศาสตร์ไม่ต่อเนื่อง วิธีเชิงตัวเลข
  Optimization และจำนวนเชิงซ้อน
- Easy 200 / Medium 500 / Hard 300 พร้อมรูปแบบโจทย์ 6 แบบ
- วางแผน Train 800 / Validation 100 / Synthetic Test 100 โดยเก็บ family เดียวกันใน split เดียว
- แยกการสร้างโจทย์ → เฉลย → Rubric → AI Review จำนวน 4 model calls ต่อโจทย์
- บันทึกขั้นตอนสำหรับ resume ตรวจข้อมูลซ้ำ และแยกรายการรอตรวจออกจาก export

ต้องมี Python 3.10+ และ Codex CLI ที่ติดตั้งและล็อกอินแล้วสำหรับการสร้างจริง
ใช้ Python standard library เท่านั้น โหมด plan/test ไม่เรียก AI

```powershell
cd krugrade-questions-pipeline/CEDT_KruGradeAI_Direct_Pipeline/question_generation

# สร้างแผนและ prompt packets โดยไม่เรียก AI
python generate_dataset.py plan --out output/university_math_1000

# ลงทะเบียนโจทย์เดิมเพื่อให้ชุดใหม่ตรวจเทียบด้วย
python -B -m pipeline.question_registry --input output/dataset/all_in_one.csv --registry output/question_registry.sqlite3 --dataset-id original_signals_30

# ทดลองสองโจทย์; รอบถัดไปจะใช้ stage ที่เสร็จแล้วและทำข้อที่เหลือต่อ
python generate_dataset.py generate --out output/university_math_1000 --limit 2
python generate_dataset.py generate --out output/university_math_1000 --limit 20

# รันข้อที่เหลือทั้งหมด (ทั้งชุดประมาณ 4,000 calls ก่อน retries)
python generate_dataset.py generate --out output/university_math_1000 --all

# ตรวจและส่งออกซ้ำโดยไม่เรียก AI
python generate_dataset.py export --out output/university_math_1000
```

## ตรวจโจทย์ซ้ำข้ามรอบ

ทุกการ generate/export ใช้ฐานกลาง `output/question_registry.sqlite3` โดยปริยาย
แม้ output ของแต่ละรอบจะอยู่คนละโฟลเดอร์ สามารถใช้ `--registry` ระบุฐานกลางอื่นได้
เมื่อต้องการใช้ร่วมกันระหว่างหลายสำเนาโปรเจกต์ ให้ระบุ absolute path เดียวกัน

ระบบตรวจข้อความซ้ำหลัง normalize, รูปแบบที่เปลี่ยนเฉพาะตัวเลข และข้อความใกล้เคียง
ตาม `near_duplicate_threshold` ค่าเริ่มต้น 0.90 รายการที่พบจะถูกกันออกและบันทึกใน
`review_queue.csv` พร้อม ID/แหล่งข้อมูล/split ของโจทย์เดิม การ export รอบเดิมซ้ำ
ไม่ถือว่าซ้ำกับตัวเอง และการตรวจพร้อมกันถูกควบคุมด้วย SQLite transaction

การสร้างรอบใหม่ให้เปลี่ยน `dataset_id` และ `seed` ใน config สำเนา ใช้ output ใหม่
แต่ใช้ registry เดิม ประวัติโจทย์เก่าต้อง import เข้าฐานก่อนจึงจะนำมาเทียบได้
ฐานข้อมูลนี้ไม่ถูก commit เข้า Git จึงต้องสำรองหรือส่งต่อประวัติข้อมูลให้ทีมด้วย

**ข้อจำกัด:** ยังไม่มี embeddings หรือการพิสูจน์ความสมมูลทางคณิตศาสตร์
ข้อที่เปลี่ยนถ้อยคำ/ชื่อตัวแปรมากอาจตรวจไม่พบ ส่วนข้อเปลี่ยนตัวเลขอาจถูก flag แม้
ตั้งใจสร้างเป็น variant ต้องตรวจยืนยันก่อนใช้งาน ไม่อ้างว่าไม่ซ้ำ 100%

## ผลลัพธ์และการนำไป train

- `dataset/all_in_one.csv`: โจทย์ เฉลย และ Rubric ที่ผ่านโครงสร้างและ AI Review เบื้องต้น
- `splits/`: ชุด train/validation/test ตาม family (จำนวนจริงอาจลดลงหลังคัดกรอง)
- `review_queue.csv`, `summary.json`, `stages/`: หลักฐานและรายการที่ต้องตรวจต่อ
- ทุกโจทย์ยังเป็น `label_review_status=unreviewed`

ยังต้องเพิ่มคำตอบนักเรียนหลายระดับคะแนนและตรวจยืนยัน labels ก่อนฝึก Grader
Answer Pipeline ปัจจุบันสร้าง PARTIAL เท่านั้น ยังไม่ได้สร้าง FULL/PARTIAL/WRONG
ครบสัดส่วน และ synthetic test ไม่ใช่ชุดทดสอบจริงอิสระ

รายละเอียดเพิ่มเติม: [คู่มือ Bulk Generation](krugrade-questions-pipeline/CEDT_KruGradeAI_Direct_Pipeline/question_generation/BULK_GENERATION.md)

## ทดสอบ

จากโฟลเดอร์ `question_generation`:

```powershell
python -B -m unittest discover -s tests -v
```

ครอบคลุมแผน 1,000 ข้อ การแบ่ง family, prompt isolation, resume, validation,
duplicate registry ข้ามรอบ, import, idempotent export และ rollback
การทดสอบใช้ model mock ไม่ได้ยืนยันความถูกต้องของโจทย์ที่ AI สร้างจริง
