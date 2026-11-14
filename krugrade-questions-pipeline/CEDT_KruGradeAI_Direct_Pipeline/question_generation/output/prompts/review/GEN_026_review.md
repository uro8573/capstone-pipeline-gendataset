ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_026
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_026",
  "reference_question_ids": [
    "REF_007"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "First-Order Frequency Response",
  "subtopic": "Compare two low-pass systems",
  "concept_tags": [
    "Transfer functions",
    "magnitude comparison",
    "phase shift",
    "low-pass behavior",
    "sinusoidal response"
  ],
  "learning_objective": "Compare attenuation and phase of two first-order systems having equal DC gain.",
  "question_type": "Comparison + Calculation",
  "difficulty": "Medium",
  "expected_methods": [
    "ODE transform",
    "gain/phase evaluation",
    "side-by-side sinusoidal outputs"
  ],
  "variation_strategy": "Two-system attenuation and phase comparison",
  "rubric_max_score": 6.0
}
QUESTION:
{
  "question_id": "GEN_026",
  "reference_question_ids": [
    "REF_007"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "First-Order Frequency Response",
  "subtopic": "Compare two low-pass systems",
  "concept_tags": [
    "Transfer functions",
    "magnitude comparison",
    "phase shift",
    "low-pass behavior",
    "sinusoidal response"
  ],
  "difficulty": "Medium",
  "question_type": "Comparison + Calculation",
  "rubric_max_score": 6.0,
  "learning_objective": "Compare attenuation and phase of two first-order systems having equal DC gain.",
  "question_text": "System A: \\[\\frac{dy_A}{dt}+y_A=u(t).\\]\nSystem B: \\[\\frac{dy_B}{dt}+4y_B=4u(t).\\]\n1. (2 points) Derive HA(jω), HB(jω) and compare DC gains.\n2. (2 points) Find magnitudes and phases at ω=2; determine which attenuates less.\n3. (2 points) For \\(u(t)=6\\cos2t\\), find both steady-state outputs and explain low-pass behavior.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_026",
  "solution": "Step 1 — Fourier-transform ODEs:\n\\[H_A(j\\omega)=1/(1+j\\omega),\\quad H_B(j\\omega)=4/(4+j\\omega).\\]\nBoth have DC gain 1.\nStep 2 — At ω=2:\n\\[|H_A(j2)|=1/\\sqrt5,\\quad \\phi_A=-\\tan^{-1}2,\\]\n\\[|H_B(j2)|=4/\\sqrt{20}=2/\\sqrt5,\\quad\\phi_B=-\\tan^{-1}(1/2).\\]\nB has twice A's magnitude at ω=2, so attenuates less.\nStep 3 — For amplitude-6 cosine input:\n\\[y_{A,ss}(t)=6/\\sqrt5\\cos(2t-\\tan^{-1}2),\\]\n\\[y_{B,ss}(t)=12/\\sqrt5\\cos(2t-\\tan^{-1}(1/2)).\\]\nBoth systems are low-pass because |H| decreases as |ω| increases.",
  "final_answer": "\\(H_A=1/(1+j\\omega)\\), \\(H_B=4/(4+j\\omega)\\); both DC gain 1, but B attenuates less at ω=2. Outputs \\(6/\\sqrt5\\cos(2t-\\tan^{-1}2)\\), \\(12/\\sqrt5\\cos(2t-\\tan^{-1}(1/2))\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_026",
    "criterion_id": "GEN_026_R1",
    "rubric_order": 1,
    "criterion": "Transfer functions",
    "description": "Transfer functions",
    "max_points": 2.0,
    "full_credit": "Correct models and equal DC gains",
    "partial_credit": "1 for transfer functions without DC comparison",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_007"
    ]
  },
  {
    "question_id": "GEN_026",
    "criterion_id": "GEN_026_R2",
    "rubric_order": 2,
    "criterion": "Magnitude and phase",
    "description": "Magnitude and phase",
    "max_points": 2.0,
    "full_credit": "Correct values and attenuation comparison",
    "partial_credit": "1 for magnitudes with incomplete phase analysis",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_007"
    ]
  },
  {
    "question_id": "GEN_026",
    "criterion_id": "GEN_026_R3",
    "rubric_order": 3,
    "criterion": "Outputs",
    "description": "Outputs",
    "max_points": 2.0,
    "full_credit": "Both steady-state outputs and low-pass reasoning",
    "partial_credit": "1 for one correct output",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_007"
    ]
  }
]
