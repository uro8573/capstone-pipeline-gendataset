ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_019
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_019",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Mixed harmonics and three-pole rational inverse",
  "concept_tags": [
    "Inverse DTFT",
    "trigonometric products",
    "complex exponentials",
    "three-term partial fractions",
    "causal sequences"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "rubric_max_score": 8.0,
  "learning_objective": "Recover finite impulse output from mixed harmonics and causal output from three-factor rational DTFT.",
  "question_text": "Find inverse DTFTs:\nPart A (3 points): \\[X_A(e^{j\\omega})=(1-j\\sin2\\omega)\\cos\\omega.\\]\nPart B (5 points): For \\(z=e^{-j\\omega}\\), \\[X_B(z)=\\frac{2+\\frac54z-\\frac58z^2}{(1-\\frac12z)(1+\\frac12z)(1-\\frac14z)}.\\]\nAssume causal expansion for Part B.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
