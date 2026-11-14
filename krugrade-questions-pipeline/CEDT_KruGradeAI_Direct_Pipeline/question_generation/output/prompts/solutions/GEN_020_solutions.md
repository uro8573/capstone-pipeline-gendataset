ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_020
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
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
