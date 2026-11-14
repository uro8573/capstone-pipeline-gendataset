ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_019
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_019",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Mixed harmonics and three-pole rational inverse",
  "concept_tags": [
    "Inverse DTFT",
    "trigonometric products",
    "complex exponentials",
    "three-term partial fractions",
    "causal sequences"
  ],
  "learning_objective": "Recover finite impulse output from mixed harmonics and causal output from three-factor rational DTFT.",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "difficulty": "Medium",
  "expected_methods": [
    "Trig products",
    "exponentials",
    "three-term partial fractions",
    "causal DTFT"
  ],
  "variation_strategy": "Three-pole inverse and overlapping harmonics",
  "rubric_max_score": 8.0
}
QUESTION:
{
  "question_id": "GEN_019",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Mixed harmonics and three-pole rational inverse",
  "concept_tags": [
    "Inverse DTFT",
    "trigonometric products",
    "complex exponentials",
    "three-term partial fractions",
    "causal sequences"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "rubric_max_score": 8.0,
  "learning_objective": "Recover finite impulse output from mixed harmonics and causal output from three-factor rational DTFT.",
  "question_text": "Find inverse DTFTs:\nPart A (3 points): \\[X_A(e^{j\\omega})=(1-j\\sin2\\omega)\\cos\\omega.\\]\nPart B (5 points): For \\(z=e^{-j\\omega}\\), \\[X_B(z)=\\frac{2+\\frac54z-\\frac58z^2}{(1-\\frac12z)(1+\\frac12z)(1-\\frac14z)}.\\]\nAssume causal expansion for Part B.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_019",
  "solution": "Part A — Step 1: \\(\\sin2\\omega\\cos\\omega=(\\sin3\\omega+\\sin\\omega)/2\\), so\n\\[X_A=\\cos\\omega-\\frac j2\\sin3\\omega-\\frac j2\\sin\\omega.\\]\nStep 2: Convert each harmonic to Euler exponentials, combine overlapping order-1 terms:\n\\[X_A=\\tfrac14e^{j\\omega}+\\tfrac34e^{-j\\omega}-\\tfrac14e^{j3\\omega}+\\tfrac14e^{-j3\\omega}.\\]\nStep 3: Invert:\n\\[x_A[n]=\\tfrac14\\delta[n+1]+\\tfrac34\\delta[n-1]-\\tfrac14\\delta[n+3]+\\tfrac14\\delta[n-3].\\]\nPart B — Step 1: Assume\n\\[X_B(z)=\\frac A{1-z/2}+\\frac B{1+z/2}+\\frac C{1-z/4}.\\]\nStep 2: Numerator matching yields\n\\[A+B+C=2,\\quad A/4-3B/4=5/4,\\quad-A/8+B/8-C/4=-5/8.\\]\nThus \\(A=2,B=-1,C=1\\).\nStep 3: The rational function equals\n\\[2/(1-z/2)-1/(1+z/2)+1/(1-z/4).\\]\nUsing causal pairs,\n\\[x_B[n]=[2(1/2)^n-(-1/2)^n+(1/4)^n]u[n].\\]",
  "final_answer": "\\(x_A[n]=\\tfrac14\\delta[n+1]+\\tfrac34\\delta[n-1]-\\tfrac14\\delta[n+3]+\\tfrac14\\delta[n-3]\\); \\(x_B[n]=[2(1/2)^n-(-1/2)^n+(1/4)^n]u[n]\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_019",
    "criterion_id": "GEN_019_R1",
    "rubric_order": 1,
    "criterion": "Trig identity",
    "description": "Trig identity",
    "max_points": 1.0,
    "full_credit": "Correct harmonic decomposition",
    "partial_credit": "0.5 for method with sign error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_019",
    "criterion_id": "GEN_019_R2",
    "rubric_order": 2,
    "criterion": "Exponential combination",
    "description": "Exponential combination",
    "max_points": 1.0,
    "full_credit": "Correct combined coefficients",
    "partial_credit": "0.5 for correct terms but incomplete combination",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_019",
    "criterion_id": "GEN_019_R3",
    "rubric_order": 3,
    "criterion": "Impulse sequence",
    "description": "Impulse sequence",
    "max_points": 1.0,
    "full_credit": "Correct indices and amplitudes",
    "partial_credit": "0.5 for isolated index/sign error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_019",
    "criterion_id": "GEN_019_R4",
    "rubric_order": 4,
    "criterion": "Partial-fraction setup",
    "description": "Partial-fraction setup",
    "max_points": 1.0,
    "full_credit": "Correct three-factor decomposition",
    "partial_credit": "0.5 for incomplete matching equations",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_019",
    "criterion_id": "GEN_019_R5",
    "rubric_order": 5,
    "criterion": "Coefficient solution",
    "description": "Coefficient solution",
    "max_points": 2.0,
    "full_credit": "Correct A=2 B=-1 C=1",
    "partial_credit": "1 for correct setup with arithmetic error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_019",
    "criterion_id": "GEN_019_R6",
    "rubric_order": 6,
    "criterion": "Causal pairs",
    "description": "Causal pairs",
    "max_points": 0.5,
    "full_credit": "Correct geometric pairs",
    "partial_credit": "0.25 for partial correctness",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  },
  {
    "question_id": "GEN_019",
    "criterion_id": "GEN_019_R7",
    "rubric_order": 7,
    "criterion": "Final sequence",
    "description": "Final sequence",
    "max_points": 1.5,
    "full_credit": "Correct coefficients powers and unit step",
    "partial_credit": "Up to 1 for mostly correct sequence",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_005"
    ]
  }
]
