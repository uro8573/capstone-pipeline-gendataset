ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_009
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_009",
  "reference_question_ids": [
    "REF_003"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Series",
  "subtopic": "Periodic rectangular pulse properties",
  "concept_tags": [
    "Complex Fourier series",
    "DC component",
    "harmonic coefficients",
    "time shifting",
    "discontinuity",
    "coefficient decay"
  ],
  "difficulty": "Medium",
  "question_type": "True/False with Justification",
  "rubric_max_score": 5.0,
  "learning_objective": "Evaluate coefficient and convergence claims for a periodic rectangular signal.",
  "question_text": "A continuous-time periodic signal has \\(T=6\\), defined on \\(-3\\le t<3\\):\n\\[x(t)=\\begin{cases}2,&|t|<1,\\\\0,&1\\le|t|<3.\\end{cases}\\]\nLet \\(a_k\\) be complex Fourier-series coefficients and \\(y(t)=x(t-1)\\) have coefficients \\(b_k\\). Classify each as True or False and justify (1 point each):\n9.1 DC coefficient \\(a_0=2/3\\).\n9.2 Third harmonic \\(a_3=0\\).\n9.3 First shifted coefficient \\(b_1\\) is purely imaginary.\n9.4 At \\(t=1\\), Fourier series converges to 1.\n9.5 Coefficients decay at least as fast as \\(1/k^2\\), i.e. \\(a_k=O(1/k^2)\\).",
  "question_language": "English",
  "math_notation": "LaTeX"
}
