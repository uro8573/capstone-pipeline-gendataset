ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_001
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_001",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Multi-bandwidth sinc signal",
  "concept_tags": [
    "CTFT",
    "sinc",
    "time-domain sampling",
    "impulse train",
    "spectral replication",
    "frequency-domain interpretation"
  ],
  "difficulty": "Medium",
  "question_type": "Derivation + Sketching",
  "rubric_max_score": 5.0,
  "learning_objective": "Derive and interpret the sampled spectrum of a signal composed of components with different bandwidths.",
  "question_text": "Consider the continuous-time signal\n\\[x(t)=\\operatorname{sinc}\\left(\\frac{\\pi t}{\\tau}\\right)+\\frac12\\operatorname{sinc}\\left(\\frac{2\\pi t}{\\tau}\\right),\\quad \\tau>0.\\]\nIt is uniformly sampled by \\[p(t)=\\sum_{m=-\\infty}^{\\infty}\\delta\\left(t-\\frac{m\\tau}{5}\\right),\\qquad g(t)=x(t)p(t).\\]\nUse \\(X(j\\omega)=\\int_{-\\infty}^{\\infty}x(t)e^{-j\\omega t}\\,dt\\) and \\(\\operatorname{sinc}(u)=\\sin(u)/u\\) (with sinc(0)=1).\n1. (1 point) Derive \\(X(j\\omega)\\) and identify its frequency support.\n2. (1 point) Derive \\(P(j\\omega)\\) and identify frequency spacing between impulses.\n3. (1 point) Express \\(g(t)\\) as a weighted impulse train. Determine impulse weights at \\(t=0\\) and \\(t=\\pm\\tau\\).\n4. (1 point) Derive \\(G(j\\omega)\\) in terms of shifted copies of \\(X(j\\omega)\\).\n5. (1 point) Sketch the magnitude spectra of \\(X\\) and \\(G\\), labeling heights, boundaries and replica centers. Explain whether spectral overlapping occurs.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
