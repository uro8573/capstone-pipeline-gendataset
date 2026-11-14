ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_016
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_016",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Mixed harmonics and two geometric terms",
  "concept_tags": [
    "Trigonometric identities",
    "complex exponentials",
    "inverse DTFT",
    "partial fractions",
    "causal sequences"
  ],
  "learning_objective": "Invert DTFT using harmonic expansion and rational partial fractions.",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "difficulty": "Medium",
  "expected_methods": [
    "Product-to-sum",
    "Euler expansion",
    "partial fractions",
    "causal inverse DTFT"
  ],
  "variation_strategy": "Different harmonic interactions and rational factors",
  "rubric_max_score": 8.0
}
QUESTION:
{
  "question_id": "GEN_016",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Mixed harmonics and two geometric terms",
  "concept_tags": [
    "Trigonometric identities",
    "complex exponentials",
    "inverse DTFT",
    "partial fractions",
    "causal sequences"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "rubric_max_score": 8.0,
  "learning_objective": "Invert DTFT using harmonic expansion and rational partial fractions.",
  "question_text": "Find the inverse DTFT of both expressions, showing all steps.\nPart A (3 points): \\[X_A(e^{j\\omega})=(1+j\\sin\\omega)\\cos3\\omega.\\]\nPart B (5 points): \\[X_B(e^{j\\omega})=\\frac{1+2e^{-j\\omega}}{(1-\\frac12e^{-j\\omega})(1+\\frac13e^{-j\\omega})}.\\]\nFor Part B assume the causal geometric-series expansion.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_016",
  "solution": "Part A — Step 1: \\(\\sin\\omega\\cos3\\omega=(\\sin4\\omega-\\sin2\\omega)/2\\), so\n\\[X_A=\\cos3\\omega+\\frac j2\\sin4\\omega-\\frac j2\\sin2\\omega.\\]\nStep 2: Use Euler expansions:\n\\[X_A=\\tfrac12(e^{j3\\omega}+e^{-j3\\omega})+\\tfrac14(e^{j4\\omega}-e^{-j4\\omega})-\\tfrac14(e^{j2\\omega}-e^{-j2\\omega}).\\]\nStep 3: Since \\(e^{-j\\omega n_0}\\leftrightarrow\\delta[n-n_0]\\),\n\\[x_A[n]=\\tfrac12\\delta[n+3]+\\tfrac12\\delta[n-3]+\\tfrac14\\delta[n+4]-\\tfrac14\\delta[n-4]-\\tfrac14\\delta[n+2]+\\tfrac14\\delta[n-2].\\]\nPart B — Step 1: Set \\(z=e^{-j\\omega}\\). Then\n\\[X_B(z)=(1+2z)/((1-z/2)(1+z/3)).\\]\nStep 2: Write \\(X_B=A/(1-z/2)+B/(1+z/3)\\), giving \\(A+B=1\\), \\(A/3-B/2=2\\), hence \\(A=3,B=-2\\).\nStep 3: \\(X_B=3/(1-z/2)-2/(1+z/3)\\). Causal transform \\(1/(1-az)\\leftrightarrow a^nu[n]\\) gives\n\\[x_B[n]=[3(1/2)^n-2(-1/3)^n]u[n].\\]",
  "final_answer": "\\(x_A[n]=\\frac12\\delta[n+3]+\\frac12\\delta[n-3]+\\frac14\\delta[n+4]-\\frac14\\delta[n-4]-\\frac14\\delta[n+2]+\\frac14\\delta[n-2]\\); \\(x_B[n]=[3(1/2)^n-2(-1/3)^n]u[n]\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_016",
    "criterion_id": "GEN_016_R1",
    "rubric_order": 1,
    "criterion": "Trigonometric identity",
    "description": "Trigonometric identity",
    "max_points": 1.0,
    "full_credit": "Correct product-to-sum expansion",
    "partial_credit": "0.5 for correct approach with sign error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_016",
    "criterion_id": "GEN_016_R2",
    "rubric_order": 2,
    "criterion": "Exponential expansion",
    "description": "Exponential expansion",
    "max_points": 1.0,
    "full_credit": "Correct coefficients and exponents",
    "partial_credit": "0.5 for substantially correct expansion",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_016",
    "criterion_id": "GEN_016_R3",
    "rubric_order": 3,
    "criterion": "Index mapping",
    "description": "Index mapping",
    "max_points": 1.0,
    "full_credit": "Correct impulse locations and signs",
    "partial_credit": "0.5 for structure with index errors",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_016",
    "criterion_id": "GEN_016_R4",
    "rubric_order": 4,
    "criterion": "Rational setup",
    "description": "Rational setup",
    "max_points": 1.0,
    "full_credit": "Correct z substitution and denominator",
    "partial_credit": "0.5 for substitution with incomplete setup",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_016",
    "criterion_id": "GEN_016_R5",
    "rubric_order": 5,
    "criterion": "Partial fractions",
    "description": "Partial fractions",
    "max_points": 2.0,
    "full_credit": "Correct A=3,B=-2",
    "partial_credit": "1 for decomposition with coefficient error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_016",
    "criterion_id": "GEN_016_R6",
    "rubric_order": 6,
    "criterion": "Geometric pairs",
    "description": "Geometric pairs",
    "max_points": 0.5,
    "full_credit": "Correct causal pair and alternating sign",
    "partial_credit": "0.25 for partially correct pair",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_016",
    "criterion_id": "GEN_016_R7",
    "rubric_order": 7,
    "criterion": "Final sequence",
    "description": "Final sequence",
    "max_points": 1.5,
    "full_credit": "Correct coefficients powers and u[n]",
    "partial_credit": "Up to 1 for structure with arithmetic error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  }
]
