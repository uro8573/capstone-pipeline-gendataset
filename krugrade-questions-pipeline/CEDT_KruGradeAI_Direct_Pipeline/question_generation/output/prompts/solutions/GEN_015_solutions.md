ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_015
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_015",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Opposite time shifts",
  "concept_tags": [
    "CTFT time shifting",
    "scaling",
    "convolution theorem",
    "phase factors",
    "transform uniqueness"
  ],
  "difficulty": "Hard",
  "question_type": "Mathematical Proof",
  "rubric_max_score": 6.0,
  "learning_objective": "Prove convolution identity for independently shifted rational kernels and explain center shifts.",
  "question_text": "Let \\(f(t)=1/((t-1)^2+1)\\) and \\(g(t)=1/((t+2)^2+4)\\). Given \\(\\mathcal F\\{1/(t^2+a^2)\\}=(\\pi/a)e^{-a|\\omega|}\\), prove\n\\[(f*g)(t)=\\frac{3\\pi}{2((t+1)^2+9)}.\\]\nExplain why the resulting convolution is centered at t=-1.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
