ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_014
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_014",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Second-derivative convolution",
  "concept_tags": [
    "Time differentiation",
    "second derivative",
    "CTFT",
    "convolution theorem",
    "transform uniqueness"
  ],
  "difficulty": "Hard",
  "question_type": "Mathematical Proof",
  "rubric_max_score": 6.0,
  "learning_objective": "Prove a second-derivative convolution identity via the Fourier differentiation property.",
  "question_text": "Let \\(f(t)=1/(t^2+1)\\) and \\(\\mathcal F\\{f(t)\\}=\\pi e^{-|\\omega|}\\). Use the second derivative and convolution theorem to prove\n\\[\\frac{6t^2-2}{(t^2+1)^3}*\\frac1{t^2+1}=\\frac{4\\pi(3t^2-4)}{(t^2+4)^3}.\\]",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_014",
  "solution": "Step 1 — Differentiate \\(f(t)=1/(t^2+1)\\):\n\\[f'(t)=-2t/(t^2+1)^2,\\quad f''(t)=-2/(t^2+1)^2+8t^2/(t^2+1)^3=(6t^2-2)/(t^2+1)^3.\\]\nStep 2 — Second-derivative CTFT:\n\\[\\mathcal F\\{f''\\}=(j\\omega)^2F(j\\omega)=-\\pi\\omega^2e^{-|\\omega|}.\\]\nStep 3 — The left convolution therefore has transform\n\\[Y(j\\omega)=-\\pi\\omega^2e^{-|\\omega|}\\cdot\\pi e^{-|\\omega|}=-\\pi^2\\omega^2e^{-2|\\omega|}.\\]\nStep 4 — Scaling gives \\(\\mathcal F\\{2\\pi/(t^2+4)\\}=\\pi^2e^{-2|\\omega|}\\). Direct differentiation verifies\n\\[\\frac{d^2}{dt^2}\\frac{2\\pi}{t^2+4}=\\frac{4\\pi(3t^2-4)}{(t^2+4)^3}.\\]\nIts CTFT is \\(-\\pi^2\\omega^2e^{-2|\\omega|}\\), identical to the left. Uniqueness proves the identity.",
  "final_answer": "\\(((6t^2-2)/(t^2+1)^3)*(1/(t^2+1))=4\\pi(3t^2-4)/(t^2+4)^3\\)."
}
