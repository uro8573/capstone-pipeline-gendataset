ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_029
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
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
SOLUTION:
{
  "question_id": "GEN_029",
  "solution": "Step 1 — Exact recovery requires \\(h*g=\\delta\\). The channel has earliest support at t=T>0; convolving it with a causal g (support t≥0) cannot produce an impulse at t=0. Hence no causal zero-delay inverse.\nStep 2 — With \\(g(t)=\\sum_{n=-1}^{\\infty}g_n\\delta(t-nT)\\), the coefficient of \\(\\delta(t-mT)\\) in h*g is \\(g_{m-1}+(1/3)g_{m-2}\\), with coefficients below -1 zero.\nStep 3 — At m=0, \\(g_{-1}=1\\). For m≥1, \\(g_{m-1}+(1/3)g_{m-2}=0\\), or \\(g_n=-(1/3)g_{n-1}\\) for n≥0. Thus \\(g_{-1}=1,g_0=-1/3,g_1=1/9,g_2=-1/27\\).\nStep 4 — Closed form\n\\[g_n=(-1/3)^{n+1},\\quad n\\ge-1,\\]\n\\[g(t)=\\sum_{n=-1}^\\infty(-1/3)^{n+1}\\delta(t-nT).\\]\nEquivalently \\(g(t)=\\delta(t+T)-(1/3)\\delta(t)+(1/9)\\delta(t-T)-\\cdots\\). Delay-transform verification: \\(H(z)=z(1+z/3)\\), \\(G(z)=z^{-1}/(1+z/3)\\), product 1.",
  "final_answer": "No causal perfect zero-delay inverse exists. \\(g(t)=\\sum_{n=-1}^{\\infty}(-1/3)^{n+1}\\delta(t-nT)\\), with a required impulse at t=-T."
}
