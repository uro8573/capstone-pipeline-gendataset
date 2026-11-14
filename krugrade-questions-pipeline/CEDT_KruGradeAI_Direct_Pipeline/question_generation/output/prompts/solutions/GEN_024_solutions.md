ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_024
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_024",
  "reference_question_ids": [
    "REF_007"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "First-Order Frequency Response",
  "subtopic": "Mechanical system with nonunit derivative coefficient",
  "concept_tags": [
    "First-order ODE",
    "Fourier transform",
    "frequency response",
    "magnitude",
    "phase",
    "low-pass behavior"
  ],
  "difficulty": "Medium",
  "question_type": "Modeling + Graph + Calculation",
  "rubric_max_score": 6.0,
  "learning_objective": "Derive first-order frequency response and predict sinusoidal steady-state response.",
  "question_text": "The velocity v(t) satisfies \\[2\\frac{dv}{dt}+4v(t)=F(t).\\] Assume zero initial conditions and LTI behavior.\n1. (2 points) Derive \\(H(j\\omega)=V(j\\omega)/F(j\\omega)\\).\n2. (2 points) Find magnitude and phase response; sketch qualitative behavior for positive and negative frequencies.\n3. (2 points) For \\(F(t)=10\\cos3t\\), find steady-state velocity and identify low-pass behavior.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
