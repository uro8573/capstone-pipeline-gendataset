ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_029
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_029",
  "reference_question_ids": [
    "REF_008"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "LTI Inverse & Echo Cancellation",
  "subtopic": "Noncausal inverse with unavoidable advance",
  "concept_tags": [
    "Delayed LTI system",
    "inverse convolution",
    "causality",
    "noncausal filter",
    "coefficient recurrence"
  ],
  "difficulty": "Hard",
  "question_type": "Causality Proof + Recurrence",
  "rubric_max_score": 5.0,
  "learning_objective": "Determine whether a causal inverse exists and derive one with a required time advance.",
  "question_text": "Acoustic channel\n\\[h(t)=\\delta(t-T)+\\frac13\\delta(t-2T),\\quad T>0.\\]\nCompensation filter requires exact zero-delay recovery \\(g*h*x=x\\) for arbitrary inputs.\n1. (2 points) Can a causal inverse achieve this without added delay? Justify.\n2. (3 points) Permit one advanced impulse:\n\\[g(t)=\\sum_{n=-1}^{\\infty}g_n\\delta(t-nT).\\]\nDerive coefficient recurrence and closed-form g_n.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
