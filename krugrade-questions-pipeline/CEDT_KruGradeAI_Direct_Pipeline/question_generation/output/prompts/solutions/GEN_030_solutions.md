ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_030
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_030",
  "reference_question_ids": [
    "REF_008"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "LTI Inverse & Echo Cancellation",
  "subtopic": "Finite inverse approximation and residual echo",
  "concept_tags": [
    "Inverse convolution",
    "geometric recurrence",
    "finite inverse filter",
    "residual echo",
    "approximation error"
  ],
  "difficulty": "Hard",
  "question_type": "Proof + Approximation",
  "rubric_max_score": 5.0,
  "learning_objective": "Derive a finite inverse approximation and quantify residual echoes due to truncation.",
  "question_text": "Echo channel\n\\[h(t)=\\delta(t)+\\frac23\\delta(t-T),\\quad T>0.\\]\nApproximate ideal inverse by \\(g_M(t)=\\sum_{k=0}^Mg_k\\delta(t-kT)\\).\n1. (1 point) State/justify perfect inverse condition.\n2. (1 point) Derive recurrence for ideal gk.\n3. (2 points) For M=2, obtain g2(t) and compute overall h*g2.\n4. (1 point) Find smallest integer M≥0 for which residual echo coefficient magnitude is strictly below 0.1.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
