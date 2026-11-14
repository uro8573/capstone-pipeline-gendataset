ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_004
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_004",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Reconstructing bandpass from sampled spectrum",
  "concept_tags": [
    "Inverse CTFT",
    "spectral replication",
    "frequency shifting",
    "bandpass signals",
    "sampling reconstruction"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse Reasoning + Sketching",
  "rubric_max_score": 5.0,
  "learning_objective": "Infer the original signal and sampling parameters from a known nonoverlapping sampled spectrum.",
  "question_text": "An unknown real continuous-time signal \\(x(t)\\) is sampled by \\(p(t)=\\sum_m\\delta(t-mT_s)\\), giving \\(g=xp\\). The original signal is bandlimited to \\(|\\omega|<5\\pi/\\tau\\), \\(\\tau>0\\). The measured \\(G(j\\omega)\\) consists of rectangular bands of height 5, repeated every \\(20\\pi/\\tau\\). In the central spectral group, the nonzero intervals are \\((-4\\pi/\\tau,-2\\pi/\\tau)\\) and \\((2\\pi/\\tau,4\\pi/\\tau)\\). Every other group is an identical copy shifted by integer multiples of \\(20\\pi/\\tau\\); assume no overlap.\n1. (1 point) Find \\(T_s\\) and \\(P(j\\omega)\\).\n2. (1 point) Recover \\(X(j\\omega)\\).\n3. (1 point) Find \\(x(t)\\) explicitly.\n4. (1 point) Express \\(g(t)\\) as a weighted impulse train; give weights \\(m=0,\\pm5\\).\n5. (1 point) Sketch central and nearest groups, explain recovery without aliasing.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
