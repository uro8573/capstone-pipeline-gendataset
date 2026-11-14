ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_028
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_028",
  "reference_question_ids": [
    "REF_008"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "LTI Inverse & Echo Cancellation",
  "subtopic": "Two-echo inverse with second-order recurrence",
  "concept_tags": [
    "Inverse LTI system",
    "convolution identity",
    "multiple echoes",
    "second-order recurrence",
    "partial fractions"
  ],
  "difficulty": "Hard",
  "question_type": "Proof + Recurrence",
  "rubric_max_score": 5.0,
  "learning_objective": "Derive a closed-form causal inverse filter for a two-echo channel.",
  "question_text": "Acoustic channel\n\\[h(t)=\\delta(t)-\\frac34\\delta(t-T)+\\frac18\\delta(t-2T),\\quad T>0.\\]\nCompensation filter \\(g(t)=\\sum_{k=0}^{\\infty}g_k\\delta(t-kT)\\) should exactly recover arbitrary input.\n1. (2 points) Derive necessary and sufficient condition for perfect recovery.\n2. (1 point) Derive recurrence for gk, including g0,g1,g2.\n3. (2 points) Obtain closed form gk and write complete inverse impulse response.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
