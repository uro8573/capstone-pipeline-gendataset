ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_020
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_020",
  "reference_question_ids": [
    "REF_006"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "DFT & DTFS",
  "subtopic": "Weighted-neighbor interpolation",
  "concept_tags": [
    "DFT",
    "weighted interpolation",
    "even/odd decomposition",
    "index mapping",
    "DTFS"
  ],
  "learning_objective": "Derive DFT relation for unequal adjacent-sample interpolation and associated periodic DTFS.",
  "question_type": "Algebraic Derivation (2 parts)",
  "difficulty": "Hard",
  "expected_methods": [
    "DFT even/odd decomposition",
    "circular shift in DFT",
    "DTFS normalization"
  ],
  "variation_strategy": "Asymmetric weighted interpolation",
  "rubric_max_score": 7.0
}
QUESTION:
{
  "question_id": "GEN_020",
  "reference_question_ids": [
    "REF_006"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "DFT & DTFS",
  "subtopic": "Weighted-neighbor interpolation",
  "concept_tags": [
    "DFT",
    "weighted interpolation",
    "even/odd decomposition",
    "index mapping",
    "DTFS"
  ],
  "difficulty": "Hard",
  "question_type": "Algebraic Derivation (2 parts)",
  "rubric_max_score": 7.0,
  "learning_objective": "Derive DFT relation for unequal adjacent-sample interpolation and associated periodic DTFS.",
  "question_text": "Let \\(a[n]\\) be length 4 with modulo-4 indexing and \\(A[k]=\\sum_{r=0}^3a[r]e^{-j2\\pi kr/4}\\). Construct length-8 \\(b[n]\\) by\n\\[b[2r]=a[r],\\quad b[2r+1]=\\frac34a[r]+\\frac14a[r+1],\\quad r=0,1,2,3.\\]\nLet \\(B[k]\\) be its 8-point DFT.\n1. (5 points) Prove for k=0,…,7:\n\\[B[k]=(1+\\cos(\\pi k/4)-\\frac j2\\sin(\\pi k/4))A[k\\bmod4].\\]\n2. (2 points) Express period-8 DTFS coefficients \\(c_k\\) in terms of A and find \\(c_0\\).",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_020",
  "solution": "Step 1 — Put \\(\\theta=\\pi k/4\\), split \\(B[k]=\\sum_{r=0}^3a[r]e^{-j2\\theta r}+\\sum_{r=0}^3(\\tfrac34a[r]+\\tfrac14a[r+1])e^{-j\\theta(2r+1)}\\).\nStep 2 — Even contribution is \\(A[k\\bmod4]\\).\nStep 3 — Factor \\(e^{-j\\theta}\\) from odd part. Circular substitution gives \\(\\sum_ra[r+1]e^{-j2\\theta r}=e^{j2\\theta}A[k\\bmod4]\\). Thus\n\\[B_{odd}=(\\tfrac34e^{-j\\theta}+\\tfrac14e^{j\\theta})A=(\\cos\\theta-\\tfrac j2\\sin\\theta)A.\\]\nStep 4 — Adding even and odd contributions gives\n\\[B[k]=(1+\\cos(\\pi k/4)-\\tfrac j2\\sin(\\pi k/4))A[k\\bmod4].\\]\nStep 5 — For an 8-periodic sequence \\(c_k=B[k]/8\\), so\n\\[c_k=\\tfrac18(1+\\cos(\\pi k/4)-\\tfrac j2\\sin(\\pi k/4))A[k\\bmod4].\\]\nAt k=0 the multiplier is 2, hence \\(c_0=A[0]/4\\).",
  "final_answer": "\\(B[k]=(1+\\cos(\\pi k/4)-j\\sin(\\pi k/4)/2)A[k\\bmod4]\\); \\(c_k=B[k]/8\\); \\(c_0=A[0]/4\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_020",
    "criterion_id": "GEN_020_R1",
    "rubric_order": 1,
    "criterion": "DFT separation",
    "description": "DFT separation",
    "max_points": 0.5,
    "full_credit": "Correct even/odd decomposition",
    "partial_credit": "0.25 for partial setup",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_020",
    "criterion_id": "GEN_020_R2",
    "rubric_order": 2,
    "criterion": "Even terms",
    "description": "Even terms",
    "max_points": 1.5,
    "full_credit": "Correct A[k mod 4]",
    "partial_credit": "0.75 for correct sum with index error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_020",
    "criterion_id": "GEN_020_R3",
    "rubric_order": 3,
    "criterion": "Odd terms",
    "description": "Odd terms",
    "max_points": 2.0,
    "full_credit": "Correct weighted sums and phase factors",
    "partial_credit": "1 for correct structure with phase error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_020",
    "criterion_id": "GEN_020_R4",
    "rubric_order": 4,
    "criterion": "Combined formula",
    "description": "Combined formula",
    "max_points": 1.0,
    "full_credit": "Correct final multiplier",
    "partial_credit": "0.5 for form with coefficient error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_020",
    "criterion_id": "GEN_020_R5",
    "rubric_order": 5,
    "criterion": "DTFS",
    "description": "DTFS",
    "max_points": 2.0,
    "full_credit": "Correct ck and c0",
    "partial_credit": "1 for ck=B/8 only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  }
]
