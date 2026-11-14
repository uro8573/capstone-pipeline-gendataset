ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_021
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
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
