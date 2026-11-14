ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_008
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
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
SOLUTION:
{
  "question_id": "GEN_008",
  "solution": "Step 1 — Convolution with \\(h_+\\) implements \\(y[n]=x[n]+x[n-1]\\), and with \\(h_-\\) implements \\(y[n]=x[n]-x[n-1]\\).\nThe four linear results are:\n\\[r*h_+=(1,2,2,2,1),\\quad r*h_-=(1,0,0,0,-1),\\]\n\\[s*h_+=(1,0,0,0,-1),\\quad s*h_-=(1,-2,2,-2,1).\\]\nStep 2 — Accordingly, \\(Y_A=r*h_-\\) OR \\(s*h_+\\), \\(Y_B=r*h_+\\), \\(Y_C=s*h_-\\). YA is not uniquely identifiable.\nStep 3 — A 4-point circular convolution folds the length-5 linear output's last sample into the first: \\(y_4[0]=y[0]+y[4]\\), remaining indices 1–3 unchanged. Thus\n\\[r*_4h_+=(2,2,2,2),\\quad r*_4h_-=(0,0,0,0),\\]\n\\[s*_4h_+=(0,0,0,0),\\quad s*_4h_-=(2,-2,2,-2).\\]\nStep 4 — \\(Y_D\\) can arise from \\(r*_4h_-\\) OR \\(s*_4h_+\\). In each, the nonzero linear end values +1 and -1 fold to the same circular index and cancel.",
  "final_answer": "YA = r*h- or s*h+; YB = r*h+; YC = s*h-; YD = r*_4 h- or s*_4 h+ (zero from circular cancellation)."
}
