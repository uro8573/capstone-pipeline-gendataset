ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_010
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_010",
  "reference_question_ids": [
    "REF_003"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Series",
  "subtopic": "Triangular pulse properties",
  "concept_tags": [
    "Fourier coefficients",
    "even symmetry",
    "triangular pulse",
    "coefficient decay",
    "time shifting",
    "continuity"
  ],
  "difficulty": "Medium",
  "question_type": "True/False with Justification",
  "rubric_max_score": 5.0,
  "learning_objective": "Analyze symmetry, continuity and time shifting of a periodic triangular pulse.",
  "question_text": "Periodic \\(x(t)\\) of period \\(T=4\\), defined for \\(-2\\le t<2\\):\n\\[x(t)=\\begin{cases}1-|t|,&|t|\\le1,\\\\0,&1<|t|<2.\\end{cases}\\]\nLet \\(a_k\\) be the complex Fourier coefficients. Define \\(y(t)=x(t-1)\\) with coefficients \\(b_k\\). True/False with mathematical justification (1 point each):\n10.1 \\(a_0=1/4\\).\n10.2 Every \\(a_k\\) is real.\n10.3 \\(a_k=O(1/k^2)\\) as \\(|k|\\to\\infty\\).\n10.4 At \\(t=1\\) Fourier series converges to 1/2.\n10.5 \\(b_1=2j/\\pi^2\\).",
  "question_language": "English",
  "math_notation": "LaTeX"
}
