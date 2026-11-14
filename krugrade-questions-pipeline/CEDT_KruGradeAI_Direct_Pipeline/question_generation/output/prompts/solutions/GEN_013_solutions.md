ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_013
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_013",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Difference of rational kernels",
  "concept_tags": [
    "CTFT linearity",
    "scaling",
    "convolution theorem",
    "superposition",
    "transform uniqueness"
  ],
  "difficulty": "Hard",
  "question_type": "Mathematical Proof",
  "rubric_max_score": 6.0,
  "learning_objective": "Prove convolution of a linear combination of rational functions by Fourier superposition.",
  "question_text": "Let \\(f(t)=1/(t^2+1)-2/(t^2+4)\\) and \\(g(t)=1/(t^2+9)\\). Given\n\\[\\mathcal F\\{1/(t^2+a^2)\\}=(\\pi/a)e^{-a|\\omega|},\\quad a>0,\\]\nprove\n\\[(f*g)(t)=\\frac{4\\pi}{3(t^2+16)}-\\frac{5\\pi}{3(t^2+25)}.\\]",
  "question_language": "English",
  "math_notation": "LaTeX"
}
