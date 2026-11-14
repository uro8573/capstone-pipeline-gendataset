ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_011
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_011",
  "reference_question_ids": [
    "REF_003"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Series",
  "subtopic": "Odd periodic square-wave properties",
  "concept_tags": [
    "Odd symmetry",
    "Fourier coefficients",
    "DC component",
    "harmonic zeros",
    "time shifting",
    "convergence",
    "coefficient decay"
  ],
  "learning_objective": "Analyze Fourier-series properties of an odd periodic signal including harmonic structure and convergence.",
  "question_type": "True/False with Justification",
  "difficulty": "Medium",
  "expected_methods": [
    "Fourier coefficient integral",
    "oddness",
    "shift property",
    "jump convergence",
    "asymptotic decay"
  ],
  "variation_strategy": "Change waveform to bipolar odd square wave",
  "rubric_max_score": 5.0
}
QUESTION:
{
  "question_id": "GEN_011",
  "reference_question_ids": [
    "REF_003"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Series",
  "subtopic": "Odd periodic square-wave properties",
  "concept_tags": [
    "Odd symmetry",
    "Fourier coefficients",
    "DC component",
    "harmonic zeros",
    "time shifting",
    "convergence",
    "coefficient decay"
  ],
  "difficulty": "Medium",
  "question_type": "True/False with Justification",
  "rubric_max_score": 5.0,
  "learning_objective": "Analyze Fourier-series properties of an odd periodic signal including harmonic structure and convergence.",
  "question_text": "Consider the \\(T=2\\pi\\) periodic signal defined over \\(-\\pi<t<\\pi\\):\n\\[x(t)=\\begin{cases}-1,&-\\pi<t<0,\\\\1,&0<t<\\pi,\\\\0,&t=0.\\end{cases}\\]\nLet \\(a_k\\) denote its complex Fourier-series coefficients and \\(y(t)=x(t-\\pi/2)\\) have coefficients \\(b_k\\). Determine True/False and justify (1 point each):\n11.1 \\(a_0=0\\).\n11.2 Every nonzero even-harmonic coefficient \\(a_{2m}\\) is zero.\n11.3 Shifted first-harmonic coefficient \\(b_1=-2/\\pi\\).\n11.4 At t=0, Fourier series converges to 1.\n11.5 \\(a_k=O(1/k^2)\\) as |k|→∞.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_011",
  "solution": "Step 1 — Fundamental frequency \\(\\omega_0=1\\). From the definition,\n\\[a_k=\\frac{1}{2\\pi}\\int_{-\\pi}^{\\pi}x(t)e^{-jkt}dt.\\]\nAverage is zero by oddness: \\(a_0=0\\). For k≠0,\n\\[a_k=\\frac{1}{2\\pi}\\left[-\\int_{-\\pi}^0e^{-jkt}dt+\\int_0^\\pi e^{-jkt}dt\\right]=\\frac{1-(-1)^k}{j\\pi k}.\\]\n11.1 TRUE: zero DC.\n11.2 TRUE: for even k≠0, numerator 1−1=0.\n11.3 TRUE: \\(a_1=2/(j\\pi)=-2j/\\pi\\). Shift theorem \\(b_1=a_1e^{-j\\pi/2}=(-2j/\\pi)(-j)=-2/\\pi\\).\n11.4 FALSE: one-sided limits at zero are -1 and +1, yielding midpoint 0, not 1.\n11.5 FALSE: for odd k, \\(|a_k|=2/(\\pi|k|)\\) (1/k decay), not 1/k².",
  "final_answer": "11.1 T; 11.2 T; 11.3 T; 11.4 F; 11.5 F. \\(a_0=0\\), \\(a_k=(1-(-1)^k)/(j\\pi k)\\) for nonzero k."
}
RUBRIC:
[
  {
    "question_id": "GEN_011",
    "criterion_id": "GEN_011_R1",
    "rubric_order": 1,
    "criterion": "DC",
    "description": "DC",
    "max_points": 1.0,
    "full_credit": "True with odd-symmetry/zero-average reasoning",
    "partial_credit": "0.5 for correct label only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_011",
    "criterion_id": "GEN_011_R2",
    "rubric_order": 2,
    "criterion": "Harmonics",
    "description": "Harmonics",
    "max_points": 1.0,
    "full_credit": "True showing even harmonic zeros",
    "partial_credit": "0.5 for label only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_011",
    "criterion_id": "GEN_011_R3",
    "rubric_order": 3,
    "criterion": "Time shift",
    "description": "Time shift",
    "max_points": 1.0,
    "full_credit": "True and b1=-2/π with phase derivation",
    "partial_credit": "0.5 for correct label without computation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_011",
    "criterion_id": "GEN_011_R4",
    "rubric_order": 4,
    "criterion": "Convergence",
    "description": "Convergence",
    "max_points": 1.0,
    "full_credit": "False with midpoint at discontinuity 0",
    "partial_credit": "0.5 for correct label only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  },
  {
    "question_id": "GEN_011",
    "criterion_id": "GEN_011_R5",
    "rubric_order": 5,
    "criterion": "Decay",
    "description": "Decay",
    "max_points": 1.0,
    "full_credit": "False establishing 1/abs(k) decay",
    "partial_credit": "0.5 for correct label only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_003"
    ]
  }
]
