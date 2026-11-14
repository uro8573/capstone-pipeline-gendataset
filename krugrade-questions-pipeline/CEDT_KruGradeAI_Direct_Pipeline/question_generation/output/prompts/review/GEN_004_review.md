ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_004
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_004",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Reconstructing bandpass from sampled spectrum",
  "concept_tags": [
    "Inverse CTFT",
    "spectral replication",
    "frequency shifting",
    "bandpass signals",
    "sampling reconstruction"
  ],
  "learning_objective": "Infer the original signal and sampling parameters from a known nonoverlapping sampled spectrum.",
  "question_type": "Inverse Reasoning + Sketching",
  "difficulty": "Medium",
  "expected_methods": [
    "Spectral replica identification",
    "inverse CTFT",
    "modulation",
    "sampling"
  ],
  "variation_strategy": "Infer unknown original from sampled frequency domain",
  "rubric_max_score": 5.0
}
QUESTION:
{
  "question_id": "GEN_004",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Reconstructing bandpass from sampled spectrum",
  "concept_tags": [
    "Inverse CTFT",
    "spectral replication",
    "frequency shifting",
    "bandpass signals",
    "sampling reconstruction"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse Reasoning + Sketching",
  "rubric_max_score": 5.0,
  "learning_objective": "Infer the original signal and sampling parameters from a known nonoverlapping sampled spectrum.",
  "question_text": "An unknown real continuous-time signal \\(x(t)\\) is sampled by \\(p(t)=\\sum_m\\delta(t-mT_s)\\), giving \\(g=xp\\). The original signal is bandlimited to \\(|\\omega|<5\\pi/\\tau\\), \\(\\tau>0\\). The measured \\(G(j\\omega)\\) consists of rectangular bands of height 5, repeated every \\(20\\pi/\\tau\\). In the central spectral group, the nonzero intervals are \\((-4\\pi/\\tau,-2\\pi/\\tau)\\) and \\((2\\pi/\\tau,4\\pi/\\tau)\\). Every other group is an identical copy shifted by integer multiples of \\(20\\pi/\\tau\\); assume no overlap.\n1. (1 point) Find \\(T_s\\) and \\(P(j\\omega)\\).\n2. (1 point) Recover \\(X(j\\omega)\\).\n3. (1 point) Find \\(x(t)\\) explicitly.\n4. (1 point) Express \\(g(t)\\) as a weighted impulse train; give weights \\(m=0,\\pm5\\).\n5. (1 point) Sketch central and nearest groups, explain recovery without aliasing.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_004",
  "solution": "Step 1 — Spectral replica spacing \\(\\omega_s=20\\pi/\\tau\\) implies \\(T_s=2\\pi/\\omega_s=\\tau/10\\). Thus\n\\[P(j\\omega)=\\frac{20\\pi}{\\tau}\\sum_k\\delta(\\omega-20\\pi k/\\tau).\\]\nStep 2 — With no overlap, central \\(G=X/T_s\\). Multiply band height 5 by \\(T_s=\\tau/10\\): original band height \\(\\tau/2\\). Hence\n\\[X(j\\omega)=\\frac\\tau2\\left[\\operatorname{rect}((\\omega-3\\pi/\\tau)\\tau/(2\\pi))+\\operatorname{rect}((\\omega+3\\pi/\\tau)\\tau/(2\\pi))\\right].\\]\nStep 3 — Inverse CTFT of shifted rectangles gives a modulated sinc:\n\\[x(t)=\\frac12(e^{j3\\pi t/\\tau}+e^{-j3\\pi t/\\tau})\\operatorname{sinc}(\\pi t/\\tau)=\\operatorname{sinc}(\\pi t/\\tau)\\cos(3\\pi t/\\tau).\\]\nStep 4 —\n\\[g(t)=\\sum_m\\operatorname{sinc}(\\pi m/10)\\cos(3\\pi m/10)\\delta(t-m\\tau/10).\\]\nWeights: \\(w_0=1\\), \\(w_{\\pm5}=\\operatorname{sinc}(\\pi/2)\\cos(3\\pi/2)=0\\).\nStep 5 — Central group has two height-5 bands on stated intervals. Other groups translate boundaries by \\(\\pm20\\pi/\\tau\\). Highest original nonzero frequency is \\(4\\pi/\\tau\\), so \\(\\omega_s=20\\pi/\\tau>8\\pi/\\tau\\); neighboring groups cannot overlap. Recover original \\(X\\) from central group by scaling by \\(T_s\\).",
  "final_answer": "\\(T_s=\\tau/10\\), \\(x(t)=\\operatorname{sinc}(\\pi t/\\tau)\\cos(3\\pi t/\\tau)\\). Sample weights \\(w_0=1,w_{\\pm5}=0\\), nonoverlapping pairs of rectangular replicas."
}
RUBRIC:
[
  {
    "question_id": "GEN_004",
    "criterion_id": "GEN_004_R1",
    "rubric_order": 1,
    "criterion": "Sampling parameters",
    "description": "Sampling parameters",
    "max_points": 1.0,
    "full_credit": "Correct Ts, P(jω) and impulse spacing",
    "partial_credit": "0.5 for correct Ts but incomplete transform",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_001"
    ]
  },
  {
    "question_id": "GEN_004",
    "criterion_id": "GEN_004_R2",
    "rubric_order": 2,
    "criterion": "Original spectrum",
    "description": "Original spectrum",
    "max_points": 1.0,
    "full_credit": "Correct two shifted rectangles, supports and heights",
    "partial_credit": "0.5 for correct supports but incorrect scaling",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_001"
    ]
  },
  {
    "question_id": "GEN_004",
    "criterion_id": "GEN_004_R3",
    "rubric_order": 3,
    "criterion": "Inverse CTFT",
    "description": "Inverse CTFT",
    "max_points": 1.0,
    "full_credit": "Correct sinc-cosine expression",
    "partial_credit": "0.5 for correct idea with shift or coefficient error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_001"
    ]
  },
  {
    "question_id": "GEN_004",
    "criterion_id": "GEN_004_R4",
    "rubric_order": 4,
    "criterion": "Sampled signal",
    "description": "Sampled signal",
    "max_points": 1.0,
    "full_credit": "Correct weighted impulse train and specified weights",
    "partial_credit": "0.5 for correct general expression but wrong values",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_001"
    ]
  },
  {
    "question_id": "GEN_004",
    "criterion_id": "GEN_004_R5",
    "rubric_order": 5,
    "criterion": "Spectral interpretation",
    "description": "Spectral interpretation",
    "max_points": 1.0,
    "full_credit": "Correct neighboring groups and nonoverlap explanation",
    "partial_credit": "0.5 for correct layout with incomplete reasoning",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_001"
    ]
  }
]
