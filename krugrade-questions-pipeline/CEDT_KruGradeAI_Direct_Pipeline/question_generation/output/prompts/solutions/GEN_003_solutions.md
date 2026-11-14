ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_003
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_003",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Squared sinc and sampling comparison",
  "concept_tags": [
    "CTFT",
    "convolution theorem",
    "squared sinc",
    "triangular spectrum",
    "sampling frequency",
    "spectral replicas"
  ],
  "difficulty": "Medium",
  "question_type": "Derivation + Comparison + Sketching",
  "rubric_max_score": 5.0,
  "learning_objective": "Derive the spectrum of a squared-sinc signal and compare the effects of two sampling intervals.",
  "question_text": "Consider \\[x(t)=\\operatorname{sinc}^2(\\pi t/\\tau),\\quad\\tau>0.\\]\nSystem A samples at \\(T_A=\\tau/3\\); System B samples at \\(T_B=\\tau/4\\). In both cases \\(p_i(t)=\\sum_m\\delta(t-mT_i)\\), \\(g_i(t)=x(t)p_i(t)\\). You may use the sinc transform pair and multiplication-convolution theorem.\n1. (1 point) Derive \\(X(j\\omega)\\) in terms of \\(\\Lambda(u)=\\max(1-|u|,0)\\).\n2. (1 point) Express \\(g_A,g_B\\) as weighted impulse trains and find first positive zero-weight indices.\n3. (1 point) Derive \\(G_A,G_B\\).\n4. (1 point) Find replica centers, peak heights and bandwidths of both systems.\n5. (1 point) Sketch both spectra, compare replica separation and identify aliasing.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
