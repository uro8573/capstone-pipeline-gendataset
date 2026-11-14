ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_008
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_008",
  "reference_question_ids": [
    "REF_002"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Linear / Circular Convolution",
  "subtopic": "Nonunique cancellation matching",
  "concept_tags": [
    "Linear convolution",
    "circular convolution",
    "signal cancellation",
    "finite differences",
    "periodicity",
    "nonunique matching"
  ],
  "difficulty": "Medium",
  "question_type": "Matching + Cancellation Explanation",
  "rubric_max_score": 8.0,
  "learning_objective": "Understand how cancellation permits distinct input-filter pairs to produce the same linear and circular outputs.",
  "question_text": "Inputs \\(r[n]=(1,1,1,1)\\), \\(s[n]=(1,-1,1,-1)\\), and filters \\(h_+[n]=(1,1)\\), \\(h_-[n]=(1,-1)\\); all start at n=0 and are zero elsewhere.\nRecorded outputs: \\(Y_A=(1,0,0,0,-1)\\), \\(Y_B=(1,2,2,2,1)\\), \\(Y_C=(1,-2,2,-2,1)\\), \\(Y_D=(0,0,0,0)\\).\nRecords A–C are linear convolution; D is one period of 4-point circular convolution. More than one pair may be correct.\n1. (2 points) Identify ALL input-filter combinations for YA.\n2. (2 points) Identify combination for YB.\n3. (2 points) Identify combination for YC.\n4. (2 points) Identify ALL combinations for YD and explain cancellation.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
