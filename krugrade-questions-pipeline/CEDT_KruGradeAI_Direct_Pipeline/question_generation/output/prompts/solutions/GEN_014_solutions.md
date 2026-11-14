ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_014
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_014",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Second-derivative convolution",
  "concept_tags": [
    "Time differentiation",
    "second derivative",
    "CTFT",
    "convolution theorem",
    "transform uniqueness"
  ],
  "difficulty": "Hard",
  "question_type": "Mathematical Proof",
  "rubric_max_score": 6.0,
  "learning_objective": "Prove a second-derivative convolution identity via the Fourier differentiation property.",
  "question_text": "Let \\(f(t)=1/(t^2+1)\\) and \\(\\mathcal F\\{f(t)\\}=\\pi e^{-|\\omega|}\\). Use the second derivative and convolution theorem to prove\n\\[\\frac{6t^2-2}{(t^2+1)^3}*\\frac1{t^2+1}=\\frac{4\\pi(3t^2-4)}{(t^2+4)^3}.\\]",
  "question_language": "English",
  "math_notation": "LaTeX"
}
