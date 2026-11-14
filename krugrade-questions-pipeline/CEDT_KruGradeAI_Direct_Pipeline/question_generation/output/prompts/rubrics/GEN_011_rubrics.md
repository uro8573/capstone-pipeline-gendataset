ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_011
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_011",
  "reference_question_ids": [
    "REF_003"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Series",
  "subtopic": "Odd periodic square-wave properties",
  "concept_tags": [
    "Odd symmetry",
    "Fourier coefficients",
    "DC component",
    "harmonic zeros",
    "time shifting",
    "convergence",
    "coefficient decay"
  ],
  "difficulty": "Medium",
  "question_type": "True/False with Justification",
  "rubric_max_score": 5.0,
  "learning_objective": "Analyze Fourier-series properties of an odd periodic signal including harmonic structure and convergence.",
  "question_text": "Consider the \\(T=2\\pi\\) periodic signal defined over \\(-\\pi<t<\\pi\\):\n\\[x(t)=\\begin{cases}-1,&-\\pi<t<0,\\\\1,&0<t<\\pi,\\\\0,&t=0.\\end{cases}\\]\nLet \\(a_k\\) denote its complex Fourier-series coefficients and \\(y(t)=x(t-\\pi/2)\\) have coefficients \\(b_k\\). Determine True/False and justify (1 point each):\n11.1 \\(a_0=0\\).\n11.2 Every nonzero even-harmonic coefficient \\(a_{2m}\\) is zero.\n11.3 Shifted first-harmonic coefficient \\(b_1=-2/\\pi\\).\n11.4 At t=0, Fourier series converges to 1.\n11.5 \\(a_k=O(1/k^2)\\) as |k|→∞.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_011",
  "solution": "Step 1 — Fundamental frequency \\(\\omega_0=1\\). From the definition,\n\\[a_k=\\frac{1}{2\\pi}\\int_{-\\pi}^{\\pi}x(t)e^{-jkt}dt.\\]\nAverage is zero by oddness: \\(a_0=0\\). For k≠0,\n\\[a_k=\\frac{1}{2\\pi}\\left[-\\int_{-\\pi}^0e^{-jkt}dt+\\int_0^\\pi e^{-jkt}dt\\right]=\\frac{1-(-1)^k}{j\\pi k}.\\]\n11.1 TRUE: zero DC.\n11.2 TRUE: for even k≠0, numerator 1−1=0.\n11.3 TRUE: \\(a_1=2/(j\\pi)=-2j/\\pi\\). Shift theorem \\(b_1=a_1e^{-j\\pi/2}=(-2j/\\pi)(-j)=-2/\\pi\\).\n11.4 FALSE: one-sided limits at zero are -1 and +1, yielding midpoint 0, not 1.\n11.5 FALSE: for odd k, \\(|a_k|=2/(\\pi|k|)\\) (1/k decay), not 1/k².",
  "final_answer": "11.1 T; 11.2 T; 11.3 T; 11.4 F; 11.5 F. \\(a_0=0\\), \\(a_k=(1-(-1)^k)/(j\\pi k)\\) for nonzero k."
}
