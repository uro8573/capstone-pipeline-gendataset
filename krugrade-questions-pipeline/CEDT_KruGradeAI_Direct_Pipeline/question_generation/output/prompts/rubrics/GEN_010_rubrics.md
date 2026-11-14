ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_010
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
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
SOLUTION:
{
  "question_id": "GEN_010",
  "solution": "Step 1 — \\(\\omega_0=\\pi/2\\). By evenness,\n\\[a_k=\\frac12\\int_0^1(1-t)\\cos(k\\pi t/2)dt.\\]\nFor k≠0, integration by parts yields\n\\[\\int_0^1(1-t)\\cos(\\alpha t)dt=(1-\\cos\\alpha)/\\alpha^2,\\quad\\alpha=k\\pi/2.\\]\nHence \\(a_k=2(1-\\cos(k\\pi/2))/(k^2\\pi^2)\\), k≠0. The area of the triangle is 1, giving \\(a_0=1/4\\).\n10.1 TRUE by area/period.\n10.2 TRUE because real-even signals have real Fourier coefficients, confirmed by cosine integral.\n10.3 TRUE because \\(0\\le1-\\cos(k\\pi/2)\\le2\\), so \\(|a_k|\\le4/(k^2\\pi^2)\\).\n10.4 FALSE: at t=1 both one-sided limits and x(1) equal 0, so series converges to 0.\n10.5 FALSE: \\(a_1=2/\\pi^2\\), \\(b_1=a_1e^{-j\\pi/2}=-2j/\\pi^2\\), not +2j/π².",
  "final_answer": "10.1 True; 10.2 True; 10.3 True; 10.4 False; 10.5 False. \\(a_0=1/4\\), \\(a_k=2(1-\\cos(k\\pi/2))/(k^2\\pi^2)\\) (k≠0)."
}
