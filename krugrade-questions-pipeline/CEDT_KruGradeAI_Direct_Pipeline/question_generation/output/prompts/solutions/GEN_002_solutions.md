ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_002
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_002",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Inverse CTFT and sampling",
  "concept_tags": [
    "Inverse CTFT",
    "time shifting",
    "cosine modulation in frequency",
    "sampling",
    "spectral replication"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse Derivation + Sketching",
  "rubric_max_score": 5.0,
  "learning_objective": "Recover a time-domain signal from its frequency-domain representation and predict its sampled spectrum.",
  "question_text": "A continuous-time signal has frequency representation\n\\[X(j\\omega)=\\tau\\operatorname{rect}\\left(\\frac{\\omega\\tau}{2\\pi}\\right)\\left[1+\\cos\\left(\\frac{\\omega\\tau}{2}\\right)\\right],\\quad\\tau>0.\\]\nSample using an impulse train of period \\(T_s=\\tau/4\\).\n1. (1 point) Find \\(x(t)\\).\n2. (1 point) Express \\(g(t)\\) as an impulse train and determine weights for \\(m=0,\\pm2\\).\n3. (1 point) Derive \\(P(j\\omega)\\) and replica spacing.\n4. (1 point) Derive \\(G(j\\omega)\\).\n5. (1 point) Sketch central and nearest two replicas, label heights/support and determine aliasing.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
