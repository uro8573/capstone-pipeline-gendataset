ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_013
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_013",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Difference of rational kernels",
  "concept_tags": [
    "CTFT linearity",
    "scaling",
    "convolution theorem",
    "superposition",
    "transform uniqueness"
  ],
  "learning_objective": "Prove convolution of a linear combination of rational functions by Fourier superposition.",
  "question_type": "Mathematical Proof",
  "difficulty": "Hard",
  "expected_methods": [
    "CTFT linearity",
    "scaling",
    "convolution multiplication",
    "inverse transform"
  ],
  "variation_strategy": "Superposition of rational kernel components",
  "rubric_max_score": 6.0
}
QUESTION:
{
  "question_id": "GEN_013",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Difference of rational kernels",
  "concept_tags": [
    "CTFT linearity",
    "scaling",
    "convolution theorem",
    "superposition",
    "transform uniqueness"
  ],
  "difficulty": "Hard",
  "question_type": "Mathematical Proof",
  "rubric_max_score": 6.0,
  "learning_objective": "Prove convolution of a linear combination of rational functions by Fourier superposition.",
  "question_text": "Let \\(f(t)=1/(t^2+1)-2/(t^2+4)\\) and \\(g(t)=1/(t^2+9)\\). Given\n\\[\\mathcal F\\{1/(t^2+a^2)\\}=(\\pi/a)e^{-a|\\omega|},\\quad a>0,\\]\nprove\n\\[(f*g)(t)=\\frac{4\\pi}{3(t^2+16)}-\\frac{5\\pi}{3(t^2+25)}.\\]",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_013",
  "solution": "Step 1 — Linearity and the supplied transform pair give\n\\[F(j\\omega)=\\pi e^{-|\\omega|}-2(\\pi/2)e^{-2|\\omega|}=\\pi e^{-|\\omega|}-\\pi e^{-2|\\omega|}.\\]\nStep 2 — \\(G(j\\omega)=\\pi e^{-3|\\omega|}/3\\).\nStep 3 — Multiplication yields\n\\[Y(j\\omega)=\\frac{\\pi^2}{3}e^{-4|\\omega|}-\\frac{\\pi^2}{3}e^{-5|\\omega|}.\\]\nStep 4 — The first claimed RHS term transforms as\n\\[\\mathcal F\\{4\\pi/[3(t^2+16)]\\}=\\frac{4\\pi}{3}\\frac\\pi4e^{-4|\\omega|}=\\frac{\\pi^2}{3}e^{-4|\\omega|};\\]\nthe second transforms as\n\\[\\mathcal F\\{5\\pi/[3(t^2+25)]\\}=\\frac{\\pi^2}{3}e^{-5|\\omega|}.\\]\nThe difference equals Y. Therefore the identity follows from uniqueness of CTFT.",
  "final_answer": "\\((1/(t^2+1)-2/(t^2+4))*1/(t^2+9)=4\\pi/[3(t^2+16)]-5\\pi/[3(t^2+25)]\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_013",
    "criterion_id": "GEN_013_R1",
    "rubric_order": 1,
    "criterion": "Linearity",
    "description": "Linearity",
    "max_points": 1.0,
    "full_credit": "Correct transforms of both f terms",
    "partial_credit": "0.5 for one correct term",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_013",
    "criterion_id": "GEN_013_R2",
    "rubric_order": 2,
    "criterion": "Kernel transform",
    "description": "Kernel transform",
    "max_points": 1.0,
    "full_credit": "Correct G(jω)",
    "partial_credit": "0.5 for correct exponent with wrong scaling",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_013",
    "criterion_id": "GEN_013_R3",
    "rubric_order": 3,
    "criterion": "Convolution",
    "description": "Convolution",
    "max_points": 1.0,
    "full_credit": "Correct product and distribution",
    "partial_credit": "0.5 for setup with arithmetic error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_013",
    "criterion_id": "GEN_013_R4",
    "rubric_order": 4,
    "criterion": "Inversion",
    "description": "Inversion",
    "max_points": 2.0,
    "full_credit": "Correct inverse transforms of both terms",
    "partial_credit": "1 for one term correct",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  },
  {
    "question_id": "GEN_013",
    "criterion_id": "GEN_013_R5",
    "rubric_order": 5,
    "criterion": "Proof",
    "description": "Proof",
    "max_points": 1.0,
    "full_credit": "Correct uniqueness argument",
    "partial_credit": "0.5 for unsubstantiated conclusion",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_004"
    ]
  }
]
