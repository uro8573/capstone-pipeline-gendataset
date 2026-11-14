ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_013
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_013",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Difference of rational kernels",
  "concept_tags": [
    "CTFT linearity",
    "scaling",
    "convolution theorem",
    "superposition",
    "transform uniqueness"
  ],
  "difficulty": "Hard",
  "question_type": "Mathematical Proof",
  "rubric_max_score": 6.0,
  "learning_objective": "Prove convolution of a linear combination of rational functions by Fourier superposition.",
  "question_text": "Let \\(f(t)=1/(t^2+1)-2/(t^2+4)\\) and \\(g(t)=1/(t^2+9)\\). Given\n\\[\\mathcal F\\{1/(t^2+a^2)\\}=(\\pi/a)e^{-a|\\omega|},\\quad a>0,\\]\nprove\n\\[(f*g)(t)=\\frac{4\\pi}{3(t^2+16)}-\\frac{5\\pi}{3(t^2+25)}.\\]",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_013",
  "solution": "Step 1 — Linearity and the supplied transform pair give\n\\[F(j\\omega)=\\pi e^{-|\\omega|}-2(\\pi/2)e^{-2|\\omega|}=\\pi e^{-|\\omega|}-\\pi e^{-2|\\omega|}.\\]\nStep 2 — \\(G(j\\omega)=\\pi e^{-3|\\omega|}/3\\).\nStep 3 — Multiplication yields\n\\[Y(j\\omega)=\\frac{\\pi^2}{3}e^{-4|\\omega|}-\\frac{\\pi^2}{3}e^{-5|\\omega|}.\\]\nStep 4 — The first claimed RHS term transforms as\n\\[\\mathcal F\\{4\\pi/[3(t^2+16)]\\}=\\frac{4\\pi}{3}\\frac\\pi4e^{-4|\\omega|}=\\frac{\\pi^2}{3}e^{-4|\\omega|};\\]\nthe second transforms as\n\\[\\mathcal F\\{5\\pi/[3(t^2+25)]\\}=\\frac{\\pi^2}{3}e^{-5|\\omega|}.\\]\nThe difference equals Y. Therefore the identity follows from uniqueness of CTFT.",
  "final_answer": "\\((1/(t^2+1)-2/(t^2+4))*1/(t^2+9)=4\\pi/[3(t^2+16)]-5\\pi/[3(t^2+25)]\\)."
}
