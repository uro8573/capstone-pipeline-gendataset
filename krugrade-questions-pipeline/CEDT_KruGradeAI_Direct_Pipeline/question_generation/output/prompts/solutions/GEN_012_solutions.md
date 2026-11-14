ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_012
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_012",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Rational kernels of different widths",
  "concept_tags": [
    "Fourier duality",
    "CTFT scaling",
    "convolution theorem",
    "transform uniqueness"
  ],
  "difficulty": "Hard",
  "question_type": "Mathematical Proof",
  "rubric_max_score": 6.0,
  "learning_objective": "Prove convolution of different-width rational kernels with CTFT methods.",
  "question_text": "Given \\(e^{-|t|}\\longleftrightarrow2/(1+\\omega^2)\\), use Fourier duality, scaling and the convolution theorem to prove\n\\[\\frac1{t^2+1}*\\frac1{t^2+4}=\\frac{3\\pi}{2(t^2+9)}.\\]\nDo not evaluate the convolution integral directly.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
