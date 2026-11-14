ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_009
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_009",
  "reference_question_ids": [
    "REF_003"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Series",
  "subtopic": "Periodic rectangular pulse properties",
  "concept_tags": [
    "Complex Fourier series",
    "DC component",
    "harmonic coefficients",
    "time shifting",
    "discontinuity",
    "coefficient decay"
  ],
  "learning_objective": "Evaluate coefficient and convergence claims for a periodic rectangular signal.",
  "question_type": "True/False with Justification",
  "difficulty": "Medium",
  "expected_methods": [
    "Complex Fourier coefficients",
    "phase shifting",
    "convergence at jump",
    "asymptotic decay"
  ],
  "variation_strategy": "Different rectangular-pulse parameters and harmonic structure",
  "rubric_max_score": 5.0
}
QUESTION:
{
  "question_id": "GEN_009",
  "reference_question_ids": [
    "REF_003"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Series",
  "subtopic": "Periodic rectangular pulse properties",
  "concept_tags": [
    "Complex Fourier series",
    "DC component",
    "harmonic coefficients",
    "time shifting",
    "discontinuity",
    "coefficient decay"
  ],
  "difficulty": "Medium",
  "question_type": "True/False with Justification",
  "rubric_max_score": 5.0,
  "learning_objective": "Evaluate coefficient and convergence claims for a periodic rectangular signal.",
  "question_text": "A continuous-time periodic signal has \\(T=6\\), defined on \\(-3\\le t<3\\):\n\\[x(t)=\\begin{cases}2,&|t|<1,\\\\0,&1\\le|t|<3.\\end{cases}\\]\nLet \\(a_k\\) be complex Fourier-series coefficients and \\(y(t)=x(t-1)\\) have coefficients \\(b_k\\). Classify each as True or False and justify (1 point each):\n9.1 DC coefficient \\(a_0=2/3\\).\n9.2 Third harmonic \\(a_3=0\\).\n9.3 First shifted coefficient \\(b_1\\) is purely imaginary.\n9.4 At \\(t=1\\), Fourier series converges to 1.\n9.5 Coefficients decay at least as fast as \\(1/k^2\\), i.e. \\(a_k=O(1/k^2)\\).",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_009",
  "solution": "Step 1 — \\(\\omega_0=\\pi/3\\). For k≠0,\n\\[a_k=\\frac16\\int_{-1}^1 2e^{-jk\\pi t/3}dt=\\frac{2\\sin(k\\pi/3)}{k\\pi}.\\]\nThe DC value is \\(a_0=(1/6)(2)(2)=2/3\\).\n9.1 TRUE: mean value is 2/3.\n9.2 TRUE: \\(a_3=2\\sin\\pi/(3\\pi)=0\\).\n9.3 FALSE: \\(b_k=a_ke^{-jk\\omega_0}\\). \\(a_1=\\sqrt3/\\pi\\), hence \\(b_1=\\sqrt3/(2\\pi)-j3/(2\\pi)\\), with nonzero real and imaginary components.\n9.4 TRUE: at jump t=1, left/right limits 2 and 0, so Fourier series converges to (2+0)/2=1 (even though x(1)=0 by definition).\n9.5 FALSE: \\(a_k\\) contains bounded sine over k, and along \\(k=6m+1\\), \\(|a_k|=\\sqrt3/(\\pi|k|)\\); so not O(1/k²).",
  "final_answer": "9.1 True; 9.2 True; 9.3 False; 9.4 True; 9.5 False. \\(a_0=2/3\\), \\(a_k=2\\sin(k\\pi/3)/(k\\pi)\\) for k≠0."
}
RUBRIC:
[
  {
    "question_id": "GEN_009",
    "criterion_id": "GEN_009_R1",
    "rubric_order": 1,
    "criterion": "DC coefficient",
    "description": "DC coefficient",
    "max_points": 1.0,
    "full_credit": "True with correct average-value calculation",
    "partial_credit": "0.5 for correct label only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_009",
    "criterion_id": "GEN_009_R2",
    "rubric_order": 2,
    "criterion": "Harmonic coefficient",
    "description": "Harmonic coefficient",
    "max_points": 1.0,
    "full_credit": "True with a3 evaluation",
    "partial_credit": "0.5 for correct label only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_009",
    "criterion_id": "GEN_009_R3",
    "rubric_order": 3,
    "criterion": "Time shifting",
    "description": "Time shifting",
    "max_points": 1.0,
    "full_credit": "False with correct bk and b1",
    "partial_credit": "0.5 for label without explanation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_009",
    "criterion_id": "GEN_009_R4",
    "rubric_order": 4,
    "criterion": "Convergence",
    "description": "Convergence",
    "max_points": 1.0,
    "full_credit": "True with midpoint limits",
    "partial_credit": "0.5 for label without reasoning",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_009",
    "criterion_id": "GEN_009_R5",
    "rubric_order": 5,
    "criterion": "Coefficient decay",
    "description": "Coefficient decay",
    "max_points": 1.0,
    "full_credit": "False with 1/abs(k) behavior",
    "partial_credit": "0.5 for label without derivation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  }
]
