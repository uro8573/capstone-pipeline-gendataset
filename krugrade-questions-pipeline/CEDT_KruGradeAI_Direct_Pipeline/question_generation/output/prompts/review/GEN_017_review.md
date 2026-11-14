ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_017
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_017",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Symmetric harmonics and alternating causal terms",
  "concept_tags": [
    "Product-to-sum",
    "symmetric impulse sequences",
    "partial fractions",
    "alternating geometric sequences"
  ],
  "learning_objective": "Use symmetry to invert trigonometric spectra and distinguish geometric components.",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "difficulty": "Medium",
  "expected_methods": [
    "Trig product-to-sum",
    "Euler expansion",
    "partial fractions",
    "geometric series"
  ],
  "variation_strategy": "Symmetric harmonics and alternating causal ratio",
  "rubric_max_score": 8.0
}
QUESTION:
{
  "question_id": "GEN_017",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Symmetric harmonics and alternating causal terms",
  "concept_tags": [
    "Product-to-sum",
    "symmetric impulse sequences",
    "partial fractions",
    "alternating geometric sequences"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "rubric_max_score": 8.0,
  "learning_objective": "Use symmetry to invert trigonometric spectra and distinguish geometric components.",
  "question_text": "Find both inverse DTFT sequences.\nPart A (3 points): \\[X_A(e^{j\\omega})=2\\cos\\omega\\cos2\\omega.\\]\nPart B (5 points): \\[X_B(e^{j\\omega})=\\frac{3+\\frac16e^{-j\\omega}}{(1-\\frac12e^{-j\\omega})(1+\\frac13e^{-j\\omega})}.\\]\nUse the causal expansion in Part B.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_017",
  "solution": "Part A — Step 1: \\(2\\cos\\omega\\cos2\\omega=\\cos3\\omega+\\cos\\omega\\).\nStep 2: \\(X_A=(e^{j3\\omega}+e^{-j3\\omega}+e^{j\\omega}+e^{-j\\omega})/2\\).\nStep 3: Thus\n\\[x_A[n]=\\tfrac12(\\delta[n+3]+\\delta[n-3]+\\delta[n+1]+\\delta[n-1]).\\]\nPart B — Step 1: With \\(z=e^{-j\\omega}\\), write\n\\[X_B(z)=(3+z/6)/((1-z/2)(1+z/3))=A/(1-z/2)+B/(1+z/3).\\]\nStep 2: Equate \\(A+B=3\\), \\(A/3-B/2=1/6\\). Solve \\(A=2,B=1\\).\nStep 3: Using causal geometric DTFT pairs,\n\\[X_B(z)=2/(1-z/2)+1/(1+z/3)\\]\nbecomes\n\\[x_B[n]=[2(1/2)^n+(-1/3)^n]u[n].\\]\nThe second component alternates sign because its base is negative.",
  "final_answer": "\\(x_A[n]=[\\delta[n+3]+\\delta[n-3]+\\delta[n+1]+\\delta[n-1]]/2\\); \\(x_B[n]=[2(1/2)^n+(-1/3)^n]u[n]\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_017",
    "criterion_id": "GEN_017_R1",
    "rubric_order": 1,
    "criterion": "Trig identity",
    "description": "Trig identity",
    "max_points": 1.0,
    "full_credit": "Correct cos3ω+cosω",
    "partial_credit": "0.5 for method with angle error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_017",
    "criterion_id": "GEN_017_R2",
    "rubric_order": 2,
    "criterion": "Complex exponentials",
    "description": "Complex exponentials",
    "max_points": 1.0,
    "full_credit": "Four correct exponential terms",
    "partial_credit": "0.5 for method with coefficient errors",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_017",
    "criterion_id": "GEN_017_R3",
    "rubric_order": 3,
    "criterion": "Inverse indices",
    "description": "Inverse indices",
    "max_points": 1.0,
    "full_credit": "Correct symmetric impulses",
    "partial_credit": "0.5 for correct support with scaling error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_017",
    "criterion_id": "GEN_017_R4",
    "rubric_order": 4,
    "criterion": "Rational setup",
    "description": "Rational setup",
    "max_points": 1.0,
    "full_credit": "Correct substitution and factors",
    "partial_credit": "0.5 for correct z substitution only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_017",
    "criterion_id": "GEN_017_R5",
    "rubric_order": 5,
    "criterion": "Partial fractions",
    "description": "Partial fractions",
    "max_points": 2.0,
    "full_credit": "Correct A=2,B=1",
    "partial_credit": "1 for setup but coefficient error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_017",
    "criterion_id": "GEN_017_R6",
    "rubric_order": 6,
    "criterion": "Causal pair",
    "description": "Causal pair",
    "max_points": 0.5,
    "full_credit": "Correct geometric interpretation",
    "partial_credit": "0.25 for incomplete interpretation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_017",
    "criterion_id": "GEN_017_R7",
    "rubric_order": 7,
    "criterion": "Final sequence",
    "description": "Final sequence",
    "max_points": 1.5,
    "full_credit": "Correct powers signs and u[n]",
    "partial_credit": "Up to 1 for mostly correct sequence",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  }
]
