ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_028
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
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
SOLUTION:
{
  "question_id": "GEN_028",
  "solution": "Step 1 — Recorded output y=h*x; corrected signal z=g*y=(g*h)*x. Perfect recovery for every x iff \\(h*g=\\delta\\), the identity of convolution.\nStep 2 — Match coefficient of \\(\\delta(t-kT)\\): \\(g_k-(3/4)g_{k-1}+(1/8)g_{k-2}\\), with \\(g_{-1}=g_{-2}=0\\). Matching δ gives \\(g_0=1\\) and for k≥1\n\\[g_k=\\frac34g_{k-1}-\\frac18g_{k-2}.\\]\nThus \\(g_1=3/4\\) and \\(g_2=(3/4)^2-1/8=7/16\\).\nStep 3 — Formal delay transform \\(H(z)=1-(3/4)z+(1/8)z^2=(1-z/2)(1-z/4)\\). Invert:\n\\[G(z)=1/H(z)=\\frac2{1-z/2}-\\frac1{1-z/4}.\\]\nFor causal geometric powers, \\(g_k=2(1/2)^k-(1/4)^k\\) for k≥0, so\n\\[g(t)=\\sum_{k=0}^{\\infty}[2(1/2)^k-(1/4)^k]\\delta(t-kT).\\]\nBoth terms decay absolutely, so inverse is causal with summable coefficients.",
  "final_answer": "\\(h*g=\\delta\\), \\(g_0=1,g_1=3/4,g_2=7/16\\), \\(g_k=2(1/2)^k-(1/4)^k\\) for k≥0."
}
