ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_014
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_014",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Second-derivative convolution",
  "concept_tags": [
    "Time differentiation",
    "second derivative",
    "CTFT",
    "convolution theorem",
    "transform uniqueness"
  ],
  "learning_objective": "Prove a second-derivative convolution identity via the Fourier differentiation property.",
  "question_type": "Mathematical Proof",
  "difficulty": "Hard",
  "expected_methods": [
    "Differentiation",
    "Fourier derivative property",
    "convolution theorem",
    "uniqueness"
  ],
  "variation_strategy": "Higher derivative rational kernel",
  "rubric_max_score": 6.0
}
QUESTION:
{
  "question_id": "GEN_014",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Second-derivative convolution",
  "concept_tags": [
    "Time differentiation",
    "second derivative",
    "CTFT",
    "convolution theorem",
    "transform uniqueness"
  ],
  "difficulty": "Hard",
  "question_type": "Mathematical Proof",
  "rubric_max_score": 6.0,
  "learning_objective": "Prove a second-derivative convolution identity via the Fourier differentiation property.",
  "question_text": "Let \\(f(t)=1/(t^2+1)\\) and \\(\\mathcal F\\{f(t)\\}=\\pi e^{-|\\omega|}\\). Use the second derivative and convolution theorem to prove\n\\[\\frac{6t^2-2}{(t^2+1)^3}*\\frac1{t^2+1}=\\frac{4\\pi(3t^2-4)}{(t^2+4)^3}.\\]",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_014",
  "solution": "Step 1 — Differentiate \\(f(t)=1/(t^2+1)\\):\n\\[f'(t)=-2t/(t^2+1)^2,\\quad f''(t)=-2/(t^2+1)^2+8t^2/(t^2+1)^3=(6t^2-2)/(t^2+1)^3.\\]\nStep 2 — Second-derivative CTFT:\n\\[\\mathcal F\\{f''\\}=(j\\omega)^2F(j\\omega)=-\\pi\\omega^2e^{-|\\omega|}.\\]\nStep 3 — The left convolution therefore has transform\n\\[Y(j\\omega)=-\\pi\\omega^2e^{-|\\omega|}\\cdot\\pi e^{-|\\omega|}=-\\pi^2\\omega^2e^{-2|\\omega|}.\\]\nStep 4 — Scaling gives \\(\\mathcal F\\{2\\pi/(t^2+4)\\}=\\pi^2e^{-2|\\omega|}\\). Direct differentiation verifies\n\\[\\frac{d^2}{dt^2}\\frac{2\\pi}{t^2+4}=\\frac{4\\pi(3t^2-4)}{(t^2+4)^3}.\\]\nIts CTFT is \\(-\\pi^2\\omega^2e^{-2|\\omega|}\\), identical to the left. Uniqueness proves the identity.",
  "final_answer": "\\(((6t^2-2)/(t^2+1)^3)*(1/(t^2+1))=4\\pi(3t^2-4)/(t^2+4)^3\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_014",
    "criterion_id": "GEN_014_R1",
    "rubric_order": 1,
    "criterion": "Derivative recognition",
    "description": "Derivative recognition",
    "max_points": 1.0,
    "full_credit": "Correct f''(t)",
    "partial_credit": "0.5 for correct method with algebra error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_014",
    "criterion_id": "GEN_014_R2",
    "rubric_order": 2,
    "criterion": "CTFT differentiation",
    "description": "CTFT differentiation",
    "max_points": 1.0,
    "full_credit": "Correct -πω² exp(-abs(ω))",
    "partial_credit": "0.5 for property missing minus sign",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_014",
    "criterion_id": "GEN_014_R3",
    "rubric_order": 3,
    "criterion": "Convolution theorem",
    "description": "Convolution theorem",
    "max_points": 1.0,
    "full_credit": "Correct -π²ω² exp(-2abs(ω))",
    "partial_credit": "0.5 for setup with factor error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_014",
    "criterion_id": "GEN_014_R4",
    "rubric_order": 4,
    "criterion": "RHS transform",
    "description": "RHS transform",
    "max_points": 2.0,
    "full_credit": "Correct second derivative and scaled Fourier transform",
    "partial_credit": "1 for correct partial derivation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_014",
    "criterion_id": "GEN_014_R5",
    "rubric_order": 5,
    "criterion": "Proof conclusion",
    "description": "Proof conclusion",
    "max_points": 1.0,
    "full_credit": "Equal transforms and uniqueness",
    "partial_credit": "0.5 for result without explanation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  }
]
