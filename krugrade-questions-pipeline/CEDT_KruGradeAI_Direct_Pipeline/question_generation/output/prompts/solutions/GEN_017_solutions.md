ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_017
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_017",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Symmetric harmonics and alternating causal terms",
  "concept_tags": [
    "Product-to-sum",
    "symmetric impulse sequences",
    "partial fractions",
    "alternating geometric sequences"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "rubric_max_score": 8.0,
  "learning_objective": "Use symmetry to invert trigonometric spectra and distinguish geometric components.",
  "question_text": "Find both inverse DTFT sequences.\nPart A (3 points): \\[X_A(e^{j\\omega})=2\\cos\\omega\\cos2\\omega.\\]\nPart B (5 points): \\[X_B(e^{j\\omega})=\\frac{3+\\frac16e^{-j\\omega}}{(1-\\frac12e^{-j\\omega})(1+\\frac13e^{-j\\omega})}.\\]\nUse the causal expansion in Part B.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
