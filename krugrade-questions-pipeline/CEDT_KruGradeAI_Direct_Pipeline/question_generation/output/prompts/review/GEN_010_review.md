ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_010
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_010",
  "reference_question_ids": [
    "REF_003"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Series",
  "subtopic": "Triangular pulse properties",
  "concept_tags": [
    "Fourier coefficients",
    "even symmetry",
    "triangular pulse",
    "coefficient decay",
    "time shifting",
    "continuity"
  ],
  "learning_objective": "Analyze symmetry, continuity and time shifting of a periodic triangular pulse.",
  "question_type": "True/False with Justification",
  "difficulty": "Medium",
  "expected_methods": [
    "Complex Fourier series",
    "integration by parts",
    "asymptotic bound",
    "shift theorem"
  ],
  "variation_strategy": "Use continuous triangular pulse instead of discontinuous rectangle",
  "rubric_max_score": 5.0
}
QUESTION:
{
  "question_id": "GEN_010",
  "reference_question_ids": [
    "REF_003"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Series",
  "subtopic": "Triangular pulse properties",
  "concept_tags": [
    "Fourier coefficients",
    "even symmetry",
    "triangular pulse",
    "coefficient decay",
    "time shifting",
    "continuity"
  ],
  "difficulty": "Medium",
  "question_type": "True/False with Justification",
  "rubric_max_score": 5.0,
  "learning_objective": "Analyze symmetry, continuity and time shifting of a periodic triangular pulse.",
  "question_text": "Periodic \\(x(t)\\) of period \\(T=4\\), defined for \\(-2\\le t<2\\):\n\\[x(t)=\\begin{cases}1-|t|,&|t|\\le1,\\\\0,&1<|t|<2.\\end{cases}\\]\nLet \\(a_k\\) be the complex Fourier coefficients. Define \\(y(t)=x(t-1)\\) with coefficients \\(b_k\\). True/False with mathematical justification (1 point each):\n10.1 \\(a_0=1/4\\).\n10.2 Every \\(a_k\\) is real.\n10.3 \\(a_k=O(1/k^2)\\) as \\(|k|\\to\\infty\\).\n10.4 At \\(t=1\\) Fourier series converges to 1/2.\n10.5 \\(b_1=2j/\\pi^2\\).",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_010",
  "solution": "Step 1 — \\(\\omega_0=\\pi/2\\). By evenness,\n\\[a_k=\\frac12\\int_0^1(1-t)\\cos(k\\pi t/2)dt.\\]\nFor k≠0, integration by parts yields\n\\[\\int_0^1(1-t)\\cos(\\alpha t)dt=(1-\\cos\\alpha)/\\alpha^2,\\quad\\alpha=k\\pi/2.\\]\nHence \\(a_k=2(1-\\cos(k\\pi/2))/(k^2\\pi^2)\\), k≠0. The area of the triangle is 1, giving \\(a_0=1/4\\).\n10.1 TRUE by area/period.\n10.2 TRUE because real-even signals have real Fourier coefficients, confirmed by cosine integral.\n10.3 TRUE because \\(0\\le1-\\cos(k\\pi/2)\\le2\\), so \\(|a_k|\\le4/(k^2\\pi^2)\\).\n10.4 FALSE: at t=1 both one-sided limits and x(1) equal 0, so series converges to 0.\n10.5 FALSE: \\(a_1=2/\\pi^2\\), \\(b_1=a_1e^{-j\\pi/2}=-2j/\\pi^2\\), not +2j/π².",
  "final_answer": "10.1 True; 10.2 True; 10.3 True; 10.4 False; 10.5 False. \\(a_0=1/4\\), \\(a_k=2(1-\\cos(k\\pi/2))/(k^2\\pi^2)\\) (k≠0)."
}
RUBRIC:
[
  {
    "question_id": "GEN_010",
    "criterion_id": "GEN_010_R1",
    "rubric_order": 1,
    "criterion": "DC component",
    "description": "DC component",
    "max_points": 1.0,
    "full_credit": "True with average calculation",
    "partial_credit": "0.5 for correct label only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_010",
    "criterion_id": "GEN_010_R2",
    "rubric_order": 2,
    "criterion": "Even symmetry",
    "description": "Even symmetry",
    "max_points": 1.0,
    "full_credit": "True with real-even reasoning",
    "partial_credit": "0.5 for label without explanation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_010",
    "criterion_id": "GEN_010_R3",
    "rubric_order": 3,
    "criterion": "Coefficient decay",
    "description": "Coefficient decay",
    "max_points": 1.0,
    "full_credit": "True with O(1/k²) bound",
    "partial_credit": "0.5 for correct label but incomplete bound",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_010",
    "criterion_id": "GEN_010_R4",
    "rubric_order": 4,
    "criterion": "Series convergence",
    "description": "Series convergence",
    "max_points": 1.0,
    "full_credit": "False because x(1)=0 and continuous",
    "partial_credit": "0.5 for label without reasoning",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_010",
    "criterion_id": "GEN_010_R5",
    "rubric_order": 5,
    "criterion": "Time shifting",
    "description": "Time shifting",
    "max_points": 1.0,
    "full_credit": "False and b1=-2j/π²",
    "partial_credit": "0.5 for label with missing/incorrect intermediate calculation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  }
]
