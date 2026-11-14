ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_011
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
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
