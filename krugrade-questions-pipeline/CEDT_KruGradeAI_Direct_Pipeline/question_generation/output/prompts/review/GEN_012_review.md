ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_012
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_012",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Rational kernels of different widths",
  "concept_tags": [
    "Fourier duality",
    "CTFT scaling",
    "convolution theorem",
    "transform uniqueness"
  ],
  "learning_objective": "Prove convolution of different-width rational kernels with CTFT methods.",
  "question_type": "Mathematical Proof",
  "difficulty": "Hard",
  "expected_methods": [
    "Fourier duality",
    "time scaling",
    "product theorem",
    "uniqueness"
  ],
  "variation_strategy": "Change rational kernel scales",
  "rubric_max_score": 6.0
}
QUESTION:
{
  "question_id": "GEN_012",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Rational kernels of different widths",
  "concept_tags": [
    "Fourier duality",
    "CTFT scaling",
    "convolution theorem",
    "transform uniqueness"
  ],
  "difficulty": "Hard",
  "question_type": "Mathematical Proof",
  "rubric_max_score": 6.0,
  "learning_objective": "Prove convolution of different-width rational kernels with CTFT methods.",
  "question_text": "Given \\(e^{-|t|}\\longleftrightarrow2/(1+\\omega^2)\\), use Fourier duality, scaling and the convolution theorem to prove\n\\[\\frac1{t^2+1}*\\frac1{t^2+4}=\\frac{3\\pi}{2(t^2+9)}.\\]\nDo not evaluate the convolution integral directly.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_012",
  "solution": "Step 1 — By CTFT duality,\n\\[F(j\\omega)=\\mathcal F\\{1/(t^2+1)\\}=\\pi e^{-|\\omega|}.\\]\nStep 2 — Since \\(g(t)=1/(t^2+4)=(1/4)f(t/2)\\), time scaling gives\n\\[G(j\\omega)=\\frac\\pi2e^{-2|\\omega|}.\\]\nStep 3 — Convolution in time transforms to multiplication:\n\\[Y(j\\omega)=F(j\\omega)G(j\\omega)=\\frac{\\pi^2}{2}e^{-3|\\omega|}.\\]\nStep 4 — By the same transform pair with scale 3,\n\\[\\mathcal F\\{1/(t^2+9)\\}=\\frac\\pi3e^{-3|\\omega|}.\\]\nMultiplying by 3π/2 gives \\((\\pi^2/2)e^{-3|\\omega|}\\), identical to Y. By uniqueness of CTFT, the proposed convolution identity holds.",
  "final_answer": "\\((1/(t^2+1))*(1/(t^2+4))=3\\pi/[2(t^2+9)]\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_012",
    "criterion_id": "GEN_012_R1",
    "rubric_order": 1,
    "criterion": "Duality",
    "description": "Duality",
    "max_points": 1.0,
    "full_credit": "Correct transform of 1/(t²+1)",
    "partial_credit": "0.5 for duality setup with coefficient error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_012",
    "criterion_id": "GEN_012_R2",
    "rubric_order": 2,
    "criterion": "Scaling",
    "description": "Scaling",
    "max_points": 1.0,
    "full_credit": "Correct transform of 1/(t²+4)",
    "partial_credit": "0.5 for exponential factor with scaling error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_012",
    "criterion_id": "GEN_012_R3",
    "rubric_order": 3,
    "criterion": "Convolution theorem",
    "description": "Convolution theorem",
    "max_points": 1.0,
    "full_credit": "Correct product and exponential exponent",
    "partial_credit": "0.5 for correct theorem with arithmetic error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_012",
    "criterion_id": "GEN_012_R4",
    "rubric_order": 4,
    "criterion": "RHS transform",
    "description": "RHS transform",
    "max_points": 2.0,
    "full_credit": "Correct transform of proposed result",
    "partial_credit": "1 for correct setup with factor error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_012",
    "criterion_id": "GEN_012_R5",
    "rubric_order": 5,
    "criterion": "Proof conclusion",
    "description": "Proof conclusion",
    "max_points": 1.0,
    "full_credit": "Correct CTFT uniqueness argument",
    "partial_credit": "0.5 for correct conclusion without reason",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  }
]
