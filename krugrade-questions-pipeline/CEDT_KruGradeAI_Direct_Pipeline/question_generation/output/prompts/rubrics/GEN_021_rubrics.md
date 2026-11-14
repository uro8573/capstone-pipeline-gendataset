ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_021
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
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
SOLUTION:
{
  "question_id": "GEN_021",
  "solution": "Step 1 — With \\(\\theta=\\pi k/4\\),\n\\[B[k]=\\sum_ra[r]e^{-j2\\theta r}+\\tfrac12e^{-j\\theta}\\sum_r(a[r]-a[r+1])e^{-j2\\theta r}.\\]\nStep 2 — Even term equals \\(A[k\\bmod4]\\).\nStep 3 — By circular shift of a, \\(\\sum_ra[r+1]e^{-j2\\theta r}=e^{j2\\theta}A\\). Then\n\\[B_{odd}=\\tfrac12e^{-j\\theta}(1-e^{j2\\theta})A=\\tfrac12(e^{-j\\theta}-e^{j\\theta})A=-j\\sin\\theta A.\\]\nStep 4 — Combine:\n\\[B[k]=(1-j\\sin(\\pi k/4))A[k\\bmod4].\\]\nStep 5 — DTFS \\(c_k=\\frac18(1-j\\sin(\\pi k/4))A[k\\bmod4]\\). At k=0 and k=4, sine vanishes and k mod 4=0, so \\(B[0]=B[4]=A[0]\\), and \\(c_0=c_4=A[0]/8\\). This also follows because sum of periodic neighbor differences is 0.",
  "final_answer": "\\(B[k]=(1-j\\sin(\\pi k/4))A[k\\bmod4]\\); \\(c_k=B[k]/8\\); \\(c_0=c_4=A[0]/8\\)."
}
