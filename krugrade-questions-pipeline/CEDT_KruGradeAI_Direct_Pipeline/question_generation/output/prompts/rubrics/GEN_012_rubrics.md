ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_012
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_012",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Rational kernels of different widths",
  "concept_tags": [
    "Fourier duality",
    "CTFT scaling",
    "convolution theorem",
    "transform uniqueness"
  ],
  "difficulty": "Hard",
  "question_type": "Mathematical Proof",
  "rubric_max_score": 6.0,
  "learning_objective": "Prove convolution of different-width rational kernels with CTFT methods.",
  "question_text": "Given \\(e^{-|t|}\\longleftrightarrow2/(1+\\omega^2)\\), use Fourier duality, scaling and the convolution theorem to prove\n\\[\\frac1{t^2+1}*\\frac1{t^2+4}=\\frac{3\\pi}{2(t^2+9)}.\\]\nDo not evaluate the convolution integral directly.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_012",
  "solution": "Step 1 — By CTFT duality,\n\\[F(j\\omega)=\\mathcal F\\{1/(t^2+1)\\}=\\pi e^{-|\\omega|}.\\]\nStep 2 — Since \\(g(t)=1/(t^2+4)=(1/4)f(t/2)\\), time scaling gives\n\\[G(j\\omega)=\\frac\\pi2e^{-2|\\omega|}.\\]\nStep 3 — Convolution in time transforms to multiplication:\n\\[Y(j\\omega)=F(j\\omega)G(j\\omega)=\\frac{\\pi^2}{2}e^{-3|\\omega|}.\\]\nStep 4 — By the same transform pair with scale 3,\n\\[\\mathcal F\\{1/(t^2+9)\\}=\\frac\\pi3e^{-3|\\omega|}.\\]\nMultiplying by 3π/2 gives \\((\\pi^2/2)e^{-3|\\omega|}\\), identical to Y. By uniqueness of CTFT, the proposed convolution identity holds.",
  "final_answer": "\\((1/(t^2+1))*(1/(t^2+4))=3\\pi/[2(t^2+9)]\\)."
}
