ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_018
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_018",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Time-advanced finite and infinite sequences",
  "concept_tags": [
    "DTFT time shifting",
    "impulse index signs",
    "partial fractions",
    "causal expansion",
    "left-sided advancement"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "rubric_max_score": 8.0,
  "learning_objective": "Apply frequency-domain time advance to both finite and infinite DTFT sequences.",
  "question_text": "Find the inverse DTFTs:\nPart A (3 points): \\[X_A(e^{j\\omega})=e^{j2\\omega}(1-\\cos2\\omega).\\]\nPart B (5 points): \\[X_B(e^{j\\omega})=e^{j2\\omega}\\frac{1+e^{-j\\omega}}{(1-\\frac12e^{-j\\omega})(1+\\frac14e^{-j\\omega})}.\\]\nFor Part B invert the rational factor with the causal expansion first, then use time shifting.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
