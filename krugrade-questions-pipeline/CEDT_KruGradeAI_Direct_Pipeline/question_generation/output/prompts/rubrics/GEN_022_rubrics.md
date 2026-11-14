ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_022
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_022",
  "reference_question_ids": [
    "REF_006"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "DFT & DTFS",
  "subtopic": "Circularly shifted interleaving",
  "concept_tags": [
    "DFT",
    "circular shift",
    "interleaving",
    "modular indices",
    "phase rotation",
    "DTFS"
  ],
  "difficulty": "Hard",
  "question_type": "Algebraic Derivation (2 parts)",
  "rubric_max_score": 7.0,
  "learning_objective": "Derive how circular shifting an interleaved branch affects a longer DFT and DTFS.",
  "question_text": "Let a[n] be length 4 and indexed modulo 4, with DFT A[k]. Construct b[n] of length 8:\n\\[b[2r]=a[r],\\qquad b[2r+1]=a[(r+2)\\bmod4],\\quad r=0,1,2,3.\\]\n1. (5 points) Prove \\[B[k]=(1+(-1)^ke^{-j\\pi k/4})A[k\\bmod4].\\]\n2. (2 points) For \\(a[n]=(1,0,-1,2)\\), find period-8 DTFS coefficients \\(c_0,c_4\\) and explain why the latter is zero.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_022",
  "solution": "Step 1 — Let \\(\\theta=\\pi k/4\\). Separate even/odd terms:\n\\[B[k]=\\sum_ra[r]e^{-j2\\theta r}+e^{-j\\theta}\\sum_ra[r+2]e^{-j2\\theta r}.\\]\nStep 2 — First sum is \\(A[k\\bmod4]\\).\nStep 3 — Circular substitution m=r+2 yields \\(\\sum_ra[r+2]e^{-j2\\theta r}=e^{j4\\theta}A=e^{j\\pi k}A=(-1)^kA\\).\nStep 4 — Hence \\(B[k]=(1+(-1)^ke^{-j\\pi k/4})A[k\\bmod4]\\).\nStep 5 — For input (1,0,-1,2), \\(A[0]=2\\). Then \\(B[0]=2A[0]=4\\) and \\(c_0=B[0]/8=1/2\\). At k=4, \\(B[4]=(1+e^{-j\\pi})A[0]=0\\), so \\(c_4=0\\). Even and odd branches have equal total sums, which cancel at alternating 8-point DFT index k=4.",
  "final_answer": "\\(B[k]=(1+(-1)^ke^{-j\\pi k/4})A[k\\bmod4]\\), \\(c_k=B[k]/8\\), \\(c_0=1/2\\), \\(c_4=0\\)."
}
