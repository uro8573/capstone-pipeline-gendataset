ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_008
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
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
  "learning_objective": "Understand how cancellation permits distinct input-filter pairs to produce the same linear and circular outputs.",
  "question_type": "Matching + Cancellation Explanation",
  "difficulty": "Medium",
  "expected_methods": [
    "Finite difference filter",
    "linear convolution",
    "circular folding",
    "cancellation"
  ],
  "variation_strategy": "Nonuniqueness and signal cancellation",
  "rubric_max_score": 8.0
}
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
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_008",
  "solution": "Step 1 — Convolution with \\(h_+\\) implements \\(y[n]=x[n]+x[n-1]\\), and with \\(h_-\\) implements \\(y[n]=x[n]-x[n-1]\\).\nThe four linear results are:\n\\[r*h_+=(1,2,2,2,1),\\quad r*h_-=(1,0,0,0,-1),\\]\n\\[s*h_+=(1,0,0,0,-1),\\quad s*h_-=(1,-2,2,-2,1).\\]\nStep 2 — Accordingly, \\(Y_A=r*h_-\\) OR \\(s*h_+\\), \\(Y_B=r*h_+\\), \\(Y_C=s*h_-\\). YA is not uniquely identifiable.\nStep 3 — A 4-point circular convolution folds the length-5 linear output's last sample into the first: \\(y_4[0]=y[0]+y[4]\\), remaining indices 1–3 unchanged. Thus\n\\[r*_4h_+=(2,2,2,2),\\quad r*_4h_-=(0,0,0,0),\\]\n\\[s*_4h_+=(0,0,0,0),\\quad s*_4h_-=(2,-2,2,-2).\\]\nStep 4 — \\(Y_D\\) can arise from \\(r*_4h_-\\) OR \\(s*_4h_+\\). In each, the nonzero linear end values +1 and -1 fold to the same circular index and cancel.",
  "final_answer": "YA = r*h- or s*h+; YB = r*h+; YC = s*h-; YD = r*_4 h- or s*_4 h+ (zero from circular cancellation)."
}
RUBRIC:
[
  {
    "question_id": "GEN_008",
    "criterion_id": "GEN_008_R1",
    "rubric_order": 1,
    "criterion": "Ambiguous linear output",
    "description": "Ambiguous linear output",
    "max_points": 2.0,
    "full_credit": "Both valid YA combinations with cancellation reasoning",
    "partial_credit": "1 for only one correct combination",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_002"
    ]
  },
  {
    "question_id": "GEN_008",
    "criterion_id": "GEN_008_R2",
    "rubric_order": 2,
    "criterion": "First unique match",
    "description": "First unique match",
    "max_points": 2.0,
    "full_credit": "YB=r*h+ with computation",
    "partial_credit": "1 for correct match without calculation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_002"
    ]
  },
  {
    "question_id": "GEN_008",
    "criterion_id": "GEN_008_R3",
    "rubric_order": 3,
    "criterion": "Second unique match",
    "description": "Second unique match",
    "max_points": 2.0,
    "full_credit": "YC=s*h- with computation",
    "partial_credit": "1 for correct match without calculation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_002"
    ]
  },
  {
    "question_id": "GEN_008",
    "criterion_id": "GEN_008_R4",
    "rubric_order": 4,
    "criterion": "Zero circular output",
    "description": "Zero circular output",
    "max_points": 2.0,
    "full_credit": "Both YD combinations and correct circular cancellation",
    "partial_credit": "1 for both without explanation or one with correct reasoning",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_002"
    ]
  }
]
