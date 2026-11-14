ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_001
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_001",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Multi-bandwidth sinc signal",
  "concept_tags": [
    "CTFT",
    "sinc",
    "time-domain sampling",
    "impulse train",
    "spectral replication",
    "frequency-domain interpretation"
  ],
  "learning_objective": "Derive and interpret the sampled spectrum of a signal composed of components with different bandwidths.",
  "question_type": "Derivation + Sketching",
  "difficulty": "Medium",
  "expected_methods": [
    "CTFT pairs",
    "time scaling",
    "distribution sampling",
    "convolution theorem",
    "spectral support comparison"
  ],
  "variation_strategy": "Change mathematical object to multi-bandwidth sinc sum",
  "rubric_max_score": 5.0
}
QUESTION:
{
  "question_id": "GEN_001",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Multi-bandwidth sinc signal",
  "concept_tags": [
    "CTFT",
    "sinc",
    "time-domain sampling",
    "impulse train",
    "spectral replication",
    "frequency-domain interpretation"
  ],
  "difficulty": "Medium",
  "question_type": "Derivation + Sketching",
  "rubric_max_score": 5.0,
  "learning_objective": "Derive and interpret the sampled spectrum of a signal composed of components with different bandwidths.",
  "question_text": "Consider the continuous-time signal\n\\[x(t)=\\operatorname{sinc}\\left(\\frac{\\pi t}{\\tau}\\right)+\\frac12\\operatorname{sinc}\\left(\\frac{2\\pi t}{\\tau}\\right),\\quad \\tau>0.\\]\nIt is uniformly sampled by \\[p(t)=\\sum_{m=-\\infty}^{\\infty}\\delta\\left(t-\\frac{m\\tau}{5}\\right),\\qquad g(t)=x(t)p(t).\\]\nUse \\(X(j\\omega)=\\int_{-\\infty}^{\\infty}x(t)e^{-j\\omega t}\\,dt\\) and \\(\\operatorname{sinc}(u)=\\sin(u)/u\\) (with sinc(0)=1).\n1. (1 point) Derive \\(X(j\\omega)\\) and identify its frequency support.\n2. (1 point) Derive \\(P(j\\omega)\\) and identify frequency spacing between impulses.\n3. (1 point) Express \\(g(t)\\) as a weighted impulse train. Determine impulse weights at \\(t=0\\) and \\(t=\\pm\\tau\\).\n4. (1 point) Derive \\(G(j\\omega)\\) in terms of shifted copies of \\(X(j\\omega)\\).\n5. (1 point) Sketch the magnitude spectra of \\(X\\) and \\(G\\), labeling heights, boundaries and replica centers. Explain whether spectral overlapping occurs.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_001",
  "solution": "Step 1 — Apply the sinc transform pair and time scaling:\n\\[\\mathcal F\\{\\operatorname{sinc}(\\pi t/\\tau)\\}=\\tau\\operatorname{rect}(\\omega\\tau/(2\\pi)),\\]\n\\[\\mathcal F\\{\\tfrac12\\operatorname{sinc}(2\\pi t/\\tau)\\}=\\tfrac\\tau4\\operatorname{rect}(\\omega\\tau/(4\\pi)).\\]\nTherefore \\[X(j\\omega)=\\tau\\operatorname{rect}(\\omega\\tau/(2\\pi))+\\tfrac\\tau4\\operatorname{rect}(\\omega\\tau/(4\\pi)).\\]\nIts levels are \\(5\\tau/4\\) for \\(|\\omega|<\\pi/\\tau\\), \\(\\tau/4\\) for \\(\\pi/\\tau<|\\omega|<2\\pi/\\tau\\), and 0 outside \\(|\\omega|>2\\pi/\\tau\\).\nStep 2 — Sampling period \\(T_s=\\tau/5\\), angular spacing \\(\\omega_s=10\\pi/\\tau\\):\n\\[P(j\\omega)=\\frac{10\\pi}{\\tau}\\sum_k\\delta(\\omega-10\\pi k/\\tau).\\]\nStep 3 — Sample weights:\n\\[g(t)=\\sum_m w_m\\delta(t-m\\tau/5),\\quad w_m=\\operatorname{sinc}(\\pi m/5)+\\tfrac12\\operatorname{sinc}(2\\pi m/5).\\]\nAt \\(m=0\\), \\(w_0=3/2\\). At \\(m=\\pm5\\), both sinc terms vanish, so \\(w_{\\pm5}=0\\).\nStep 4 — Multiplication in time corresponds to frequency convolution:\n\\[G(j\\omega)=\\frac1{T_s}\\sum_kX(j(\\omega-\\omega_s k))=\\frac5\\tau\\sum_k X(j(\\omega-10\\pi k/\\tau)).\\]\nLet \\(\\Omega_k=\\omega-10\\pi k/\\tau\\). Then\n\\[G(j\\omega)=\\sum_k\\left[5\\operatorname{rect}(\\Omega_k\\tau/(2\\pi))+\\tfrac54\\operatorname{rect}(\\Omega_k\\tau/(4\\pi))\\right].\\]\nStep 5 — For each center \\(\\omega_k=10\\pi k/\\tau\\), height is \\(25/4\\) within \\(|\\omega-\\omega_k|<\\pi/\\tau\\), \\(5/4\\) in the outer band up to \\(2\\pi/\\tau\\), and 0 beyond. Sketch each replica with these two levels. Since \\(\\omega_s=10\\pi/\\tau>4\\pi/\\tau\\), replicas do not overlap (no aliasing).",
  "final_answer": "\\(w_0=3/2,\\;w_{\\pm5}=0\\). \\(G(j\\omega)=\\frac5\\tau\\sum_kX(j(\\omega-10\\pi k/\\tau))\\), with two-level nonoverlapping replicas centered at \\(10\\pi k/\\tau\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_001",
    "criterion_id": "GEN_001_R1",
    "rubric_order": 1,
    "criterion": "Original CTFT",
    "description": "Original CTFT",
    "max_points": 1.0,
    "full_credit": "Correct two rectangle terms, amplitudes and support",
    "partial_credit": "0.5 for correct transform of only one component or correct support with scale error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_001"
    ]
  },
  {
    "question_id": "GEN_001",
    "criterion_id": "GEN_001_R2",
    "rubric_order": 2,
    "criterion": "Sampling transform",
    "description": "Sampling transform",
    "max_points": 1.0,
    "full_credit": "Correct impulse locations and 10π/τ coefficient",
    "partial_credit": "0.5 for correct spacing with incorrect coefficient",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_001"
    ]
  },
  {
    "question_id": "GEN_001",
    "criterion_id": "GEN_001_R3",
    "rubric_order": 3,
    "criterion": "Sampled signal",
    "description": "Sampled signal",
    "max_points": 1.0,
    "full_credit": "Correct weighted train and specified weights",
    "partial_credit": "0.5 for correct train with one weight error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_001"
    ]
  },
  {
    "question_id": "GEN_001",
    "criterion_id": "GEN_001_R4",
    "rubric_order": 4,
    "criterion": "Sampled CTFT",
    "description": "Sampled CTFT",
    "max_points": 1.0,
    "full_credit": "Correct replication formula and scaling",
    "partial_credit": "0.5 for replication formula with missing scale",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_001"
    ]
  },
  {
    "question_id": "GEN_001",
    "criterion_id": "GEN_001_R5",
    "rubric_order": 5,
    "criterion": "Interpretation",
    "description": "Interpretation",
    "max_points": 1.0,
    "full_credit": "Both spectra correctly labeled and no-overlap justification",
    "partial_credit": "0.5 for mostly correct shape with incomplete heights or explanation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_001"
    ]
  }
]
