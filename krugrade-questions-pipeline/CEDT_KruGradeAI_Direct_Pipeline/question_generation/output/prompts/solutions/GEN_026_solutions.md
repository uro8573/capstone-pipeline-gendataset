ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_026
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_026",
  "reference_question_ids": [
    "REF_007"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "First-Order Frequency Response",
  "subtopic": "Compare two low-pass systems",
  "concept_tags": [
    "Transfer functions",
    "magnitude comparison",
    "phase shift",
    "low-pass behavior",
    "sinusoidal response"
  ],
  "difficulty": "Medium",
  "question_type": "Comparison + Calculation",
  "rubric_max_score": 6.0,
  "learning_objective": "Compare attenuation and phase of two first-order systems having equal DC gain.",
  "question_text": "System A: \\[\\frac{dy_A}{dt}+y_A=u(t).\\]\nSystem B: \\[\\frac{dy_B}{dt}+4y_B=4u(t).\\]\n1. (2 points) Derive HA(jω), HB(jω) and compare DC gains.\n2. (2 points) Find magnitudes and phases at ω=2; determine which attenuates less.\n3. (2 points) For \\(u(t)=6\\cos2t\\), find both steady-state outputs and explain low-pass behavior.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
