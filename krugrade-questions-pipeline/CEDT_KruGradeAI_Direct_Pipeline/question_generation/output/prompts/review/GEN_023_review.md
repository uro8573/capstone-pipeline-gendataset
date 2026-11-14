ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_023
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_023",
  "reference_question_ids": [
    "REF_006"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "DFT & DTFS",
  "subtopic": "Mixed circular shift and interpolation",
  "concept_tags": [
    "DFT",
    "circular shift",
    "interpolation",
    "even/odd indexing",
    "DTFS",
    "frequency-zero analysis"
  ],
  "learning_objective": "Derive mixed even-branch shift and odd-branch interpolation DFT mapping.",
  "question_type": "Algebraic Derivation (2 parts)",
  "difficulty": "Hard",
  "expected_methods": [
    "Circular shift",
    "interpolation",
    "DFT",
    "DTFS",
    "frequency zero"
  ],
  "variation_strategy": "Mixed shift and interpolation across DFT branches",
  "rubric_max_score": 7.0
}
QUESTION:
{
  "question_id": "GEN_023",
  "reference_question_ids": [
    "REF_006"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "DFT & DTFS",
  "subtopic": "Mixed circular shift and interpolation",
  "concept_tags": [
    "DFT",
    "circular shift",
    "interpolation",
    "even/odd indexing",
    "DTFS",
    "frequency-zero analysis"
  ],
  "difficulty": "Hard",
  "question_type": "Algebraic Derivation (2 parts)",
  "rubric_max_score": 7.0,
  "learning_objective": "Derive mixed even-branch shift and odd-branch interpolation DFT mapping.",
  "question_text": "Let a[n] be length 4 modulo-indexed, with 4-point DFT A[k]. Construct length-8 b[n]:\n\\[b[2r]=a[(r-1)\\bmod4],\\qquad b[2r+1]=\\frac12(a[r]+a[r+1]),\\quad r=0,1,2,3.\\]\n1. (5 points) Prove\n\\[B[k]=(e^{-j\\pi k/2}+\\cos(\\pi k/4))A[k\\bmod4].\\]\n2. (2 points) Derive DTFS coefficients and show \\(B[4]=0\\) for arbitrary a[n].",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_023",
  "solution": "Step 1 — Let \\(\\theta=\\pi k/4\\). DFT separates as\n\\[B=\\sum_ra[r-1]e^{-j2\\theta r}+\\tfrac12e^{-j\\theta}\\sum_r(a[r]+a[r+1])e^{-j2\\theta r}.\\]\nStep 2 — With circular substitution m=r−1, \\(\\sum_ra[r-1]e^{-j2\\theta r}=e^{-j2\\theta}A[k\\bmod4]\\).\nStep 3 — For odd branch, \\(\\sum_ra[r+1]e^{-j2\\theta r}=e^{j2\\theta}A\\). Therefore\n\\[B_{odd}=\\tfrac12e^{-j\\theta}(1+e^{j2\\theta})A=\\cos\\theta A.\\]\nStep 4 — Combine:\n\\[B[k]=(e^{-j\\pi k/2}+\\cos(\\pi k/4))A[k\\bmod4].\\]\nStep 5 — Period-8 DTFS coefficients are \\(c_k=(e^{-j\\pi k/2}+\\cos(\\pi k/4))A[k\\bmod4]/8\\). At k=4, \\(e^{-j2\\pi}=1\\), \\(\\cos\\pi=-1\\); multiplier zero, so \\(B[4]=0\\) for any a[n].",
  "final_answer": "\\(B[k]=(e^{-j\\pi k/2}+\\cos(\\pi k/4))A[k\\bmod4]\\); \\(c_k=B[k]/8\\); \\(B[4]=0\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_023",
    "criterion_id": "GEN_023_R1",
    "rubric_order": 1,
    "criterion": "DFT setup",
    "description": "DFT setup",
    "max_points": 0.5,
    "full_credit": "Correct even/odd branches",
    "partial_credit": "0.25 for partial setup",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_023",
    "criterion_id": "GEN_023_R2",
    "rubric_order": 2,
    "criterion": "Even shift",
    "description": "Even shift",
    "max_points": 1.5,
    "full_credit": "Correct e^-jπk/2 phase",
    "partial_credit": "0.75 for shift idea with phase error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_023",
    "criterion_id": "GEN_023_R3",
    "rubric_order": 3,
    "criterion": "Odd interpolation",
    "description": "Odd interpolation",
    "max_points": 2.0,
    "full_credit": "Correct cosine multiplier",
    "partial_credit": "1 for correct sum with algebra error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_023",
    "criterion_id": "GEN_023_R4",
    "rubric_order": 4,
    "criterion": "Combined formula",
    "description": "Combined formula",
    "max_points": 1.0,
    "full_credit": "Correct B[k]",
    "partial_credit": "0.5 for structure with isolated error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_023",
    "criterion_id": "GEN_023_R5",
    "rubric_order": 5,
    "criterion": "DTFS and zero",
    "description": "DTFS and zero",
    "max_points": 2.0,
    "full_credit": "Correct ck and B[4]=0 proof",
    "partial_credit": "1 for DTFS without proof",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  }
]
