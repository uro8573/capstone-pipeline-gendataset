ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_009
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
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
SOLUTION:
{
  "question_id": "GEN_009",
  "solution": "Step 1 — \\(\\omega_0=\\pi/3\\). For k≠0,\n\\[a_k=\\frac16\\int_{-1}^1 2e^{-jk\\pi t/3}dt=\\frac{2\\sin(k\\pi/3)}{k\\pi}.\\]\nThe DC value is \\(a_0=(1/6)(2)(2)=2/3\\).\n9.1 TRUE: mean value is 2/3.\n9.2 TRUE: \\(a_3=2\\sin\\pi/(3\\pi)=0\\).\n9.3 FALSE: \\(b_k=a_ke^{-jk\\omega_0}\\). \\(a_1=\\sqrt3/\\pi\\), hence \\(b_1=\\sqrt3/(2\\pi)-j3/(2\\pi)\\), with nonzero real and imaginary components.\n9.4 TRUE: at jump t=1, left/right limits 2 and 0, so Fourier series converges to (2+0)/2=1 (even though x(1)=0 by definition).\n9.5 FALSE: \\(a_k\\) contains bounded sine over k, and along \\(k=6m+1\\), \\(|a_k|=\\sqrt3/(\\pi|k|)\\); so not O(1/k²).",
  "final_answer": "9.1 True; 9.2 True; 9.3 False; 9.4 True; 9.5 False. \\(a_0=2/3\\), \\(a_k=2\\sin(k\\pi/3)/(k\\pi)\\) for k≠0."
}
