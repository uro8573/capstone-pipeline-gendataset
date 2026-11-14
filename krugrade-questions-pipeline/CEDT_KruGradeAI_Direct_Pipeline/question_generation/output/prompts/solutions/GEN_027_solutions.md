ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_027
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_027",
  "reference_question_ids": [
    "REF_007"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "First-Order Frequency Response",
  "subtopic": "Two-tone steady-state response",
  "concept_tags": [
    "Fourier transform of ODE",
    "frequency response",
    "sinusoidal steady state",
    "superposition",
    "low-pass filtering"
  ],
  "difficulty": "Medium",
  "question_type": "Modeling + Superposition",
  "rubric_max_score": 6.0,
  "learning_objective": "Predict response of a first-order LTI system to a two-frequency input.",
  "question_text": "A first-order LTI system satisfies \\[2\\frac{dy}{dt}+6y(t)=4u(t).\\]\nInput: \\(u(t)=3\\cos t+5\\sin4t\\). Assume zero initial conditions for frequency-response determination.\n1. (2 points) Derive H(jω), magnitude and phase.\n2. (2 points) Calculate the steady-state response to each sinusoidal component separately.\n3. (2 points) Sum to obtain complete steady-state response and identify which component is attenuated more strongly.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
