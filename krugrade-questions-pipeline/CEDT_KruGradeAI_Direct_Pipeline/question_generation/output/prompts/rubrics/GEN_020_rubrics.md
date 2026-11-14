ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_020
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
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
SOLUTION:
{
  "question_id": "GEN_020",
  "solution": "Step 1 — Put \\(\\theta=\\pi k/4\\), split \\(B[k]=\\sum_{r=0}^3a[r]e^{-j2\\theta r}+\\sum_{r=0}^3(\\tfrac34a[r]+\\tfrac14a[r+1])e^{-j\\theta(2r+1)}\\).\nStep 2 — Even contribution is \\(A[k\\bmod4]\\).\nStep 3 — Factor \\(e^{-j\\theta}\\) from odd part. Circular substitution gives \\(\\sum_ra[r+1]e^{-j2\\theta r}=e^{j2\\theta}A[k\\bmod4]\\). Thus\n\\[B_{odd}=(\\tfrac34e^{-j\\theta}+\\tfrac14e^{j\\theta})A=(\\cos\\theta-\\tfrac j2\\sin\\theta)A.\\]\nStep 4 — Adding even and odd contributions gives\n\\[B[k]=(1+\\cos(\\pi k/4)-\\tfrac j2\\sin(\\pi k/4))A[k\\bmod4].\\]\nStep 5 — For an 8-periodic sequence \\(c_k=B[k]/8\\), so\n\\[c_k=\\tfrac18(1+\\cos(\\pi k/4)-\\tfrac j2\\sin(\\pi k/4))A[k\\bmod4].\\]\nAt k=0 the multiplier is 2, hence \\(c_0=A[0]/4\\).",
  "final_answer": "\\(B[k]=(1+\\cos(\\pi k/4)-j\\sin(\\pi k/4)/2)A[k\\bmod4]\\); \\(c_k=B[k]/8\\); \\(c_0=A[0]/4\\)."
}
