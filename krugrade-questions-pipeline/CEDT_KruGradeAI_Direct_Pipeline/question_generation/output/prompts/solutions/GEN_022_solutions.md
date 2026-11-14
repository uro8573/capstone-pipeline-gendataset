ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_022
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
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
