ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_021
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_021",
  "reference_question_ids": [
    "REF_006"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "DFT & DTFS",
  "subtopic": "Neighbor-difference interleaving",
  "concept_tags": [
    "DFT",
    "neighbor differencing",
    "circular indexing",
    "frequency multiplier",
    "DTFS"
  ],
  "learning_objective": "Derive DFT relationship for odd samples formed by differences instead of averages.",
  "question_type": "Algebraic Derivation (2 parts)",
  "difficulty": "Hard",
  "expected_methods": [
    "DFT index separation",
    "circular difference",
    "Fourier phase",
    "DTFS"
  ],
  "variation_strategy": "Odd-index difference operator",
  "rubric_max_score": 7.0
}
QUESTION:
{
  "question_id": "GEN_021",
  "reference_question_ids": [
    "REF_006"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "DFT & DTFS",
  "subtopic": "Neighbor-difference interleaving",
  "concept_tags": [
    "DFT",
    "neighbor differencing",
    "circular indexing",
    "frequency multiplier",
    "DTFS"
  ],
  "difficulty": "Hard",
  "question_type": "Algebraic Derivation (2 parts)",
  "rubric_max_score": 7.0,
  "learning_objective": "Derive DFT relationship for odd samples formed by differences instead of averages.",
  "question_text": "Let \\(a[n]\\) be length 4, modulo-4 indexing, with 4-point DFT \\(A[k]\\). Construct length-8 \\(b\\):\n\\[b[2r]=a[r],\\qquad b[2r+1]=\\tfrac12(a[r]-a[r+1]),\\qquad r=0,1,2,3.\\]\n1. (5 points) Derive \\(B[k]\\) in terms of \\(A[k\\bmod4]\\) and show\n\\[B[k]=(1-j\\sin(\\pi k/4))A[k\\bmod4].\\]\n2. (2 points) Find DTFS coefficients and explain why \\(B[0]=B[4]=A[0]\\).",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_021",
  "solution": "Step 1 — With \\(\\theta=\\pi k/4\\),\n\\[B[k]=\\sum_ra[r]e^{-j2\\theta r}+\\tfrac12e^{-j\\theta}\\sum_r(a[r]-a[r+1])e^{-j2\\theta r}.\\]\nStep 2 — Even term equals \\(A[k\\bmod4]\\).\nStep 3 — By circular shift of a, \\(\\sum_ra[r+1]e^{-j2\\theta r}=e^{j2\\theta}A\\). Then\n\\[B_{odd}=\\tfrac12e^{-j\\theta}(1-e^{j2\\theta})A=\\tfrac12(e^{-j\\theta}-e^{j\\theta})A=-j\\sin\\theta A.\\]\nStep 4 — Combine:\n\\[B[k]=(1-j\\sin(\\pi k/4))A[k\\bmod4].\\]\nStep 5 — DTFS \\(c_k=\\frac18(1-j\\sin(\\pi k/4))A[k\\bmod4]\\). At k=0 and k=4, sine vanishes and k mod 4=0, so \\(B[0]=B[4]=A[0]\\), and \\(c_0=c_4=A[0]/8\\). This also follows because sum of periodic neighbor differences is 0.",
  "final_answer": "\\(B[k]=(1-j\\sin(\\pi k/4))A[k\\bmod4]\\); \\(c_k=B[k]/8\\); \\(c_0=c_4=A[0]/8\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_021",
    "criterion_id": "GEN_021_R1",
    "rubric_order": 1,
    "criterion": "DFT setup",
    "description": "DFT setup",
    "max_points": 0.5,
    "full_credit": "Correct even/odd separation",
    "partial_credit": "0.25 for partial setup",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_021",
    "criterion_id": "GEN_021_R2",
    "rubric_order": 2,
    "criterion": "Even contribution",
    "description": "Even contribution",
    "max_points": 1.5,
    "full_credit": "Correct A[k mod4]",
    "partial_credit": "0.75 for incomplete index mapping",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_021",
    "criterion_id": "GEN_021_R3",
    "rubric_order": 3,
    "criterion": "Difference contribution",
    "description": "Difference contribution",
    "max_points": 2.0,
    "full_credit": "Correct -j sinθ factor",
    "partial_credit": "1 for structure with sign or phase error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_021",
    "criterion_id": "GEN_021_R4",
    "rubric_order": 4,
    "criterion": "Combined expression",
    "description": "Combined expression",
    "max_points": 1.0,
    "full_credit": "Correct B[k]",
    "partial_credit": "0.5 for right multiplier structure with small error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  },
  {
    "question_id": "GEN_021",
    "criterion_id": "GEN_021_R5",
    "rubric_order": 5,
    "criterion": "DTFS and special indices",
    "description": "DTFS and special indices",
    "max_points": 2.0,
    "full_credit": "Correct DTFS and B[0]=B[4] reasoning",
    "partial_credit": "1 for correct DTFS only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_006"
    ]
  }
]
