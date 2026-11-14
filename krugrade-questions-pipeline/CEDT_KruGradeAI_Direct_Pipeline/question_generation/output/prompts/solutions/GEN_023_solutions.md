ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_023
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
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
