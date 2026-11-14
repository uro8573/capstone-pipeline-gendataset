ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_015
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
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
SOLUTION:
{
  "question_id": "GEN_015",
  "solution": "Step 1 — \\(f\\) is delayed 1 relative to \\(1/(t^2+1)\\), hence\n\\[F(j\\omega)=\\pi e^{-|\\omega|}e^{-j\\omega}.\\]\nStep 2 — \\(g\\) is advanced 2 relative to \\(1/(t^2+4)\\), hence\n\\[G(j\\omega)=\\frac\\pi2e^{-2|\\omega|}e^{j2\\omega}.\\]\nStep 3 — Convolution theorem gives\n\\[Y(j\\omega)=\\frac{\\pi^2}{2}e^{-3|\\omega|}e^{j\\omega}.\\]\nStep 4 — Unshifted \\(2\\pi/(t^2+9)\\) has CTFT \\((2\\pi)(\\pi/3)e^{-3|\\omega|}\\); using \\(3\\pi/[2(t^2+9)]\\) instead gives \\((\\pi^2/2)e^{-3|\\omega|}\\). Multiplication by \\(e^{j\\omega}\\) advances this result by 1: \\(y(t)=3\\pi/[2((t+1)^2+9)]\\).\nStep 5 — The shift centers add under convolution: +1 + (-2) = -1. Both sides have the same CTFT, proving the identity.",
  "final_answer": "\\(f*g=3\\pi/[2((t+1)^2+9)]\\), centered at t=-1."
}
