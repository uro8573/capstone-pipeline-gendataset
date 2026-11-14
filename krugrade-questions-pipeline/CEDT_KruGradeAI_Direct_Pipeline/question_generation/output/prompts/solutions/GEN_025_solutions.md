ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_025
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
{
  "question_id": "GEN_025",
  "reference_question_ids": [
    "REF_007"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "First-Order Frequency Response",
  "subtopic": "Identify ODE parameters from frequency data",
  "concept_tags": [
    "First-order ODE",
    "frequency-response identification",
    "magnitude",
    "phase",
    "low-pass filter"
  ],
  "difficulty": "Medium",
  "question_type": "System Identification + Calculation",
  "rubric_max_score": 6.0,
  "learning_objective": "Recover unknown first-order parameters from two measured magnitudes and predict an output.",
  "question_text": "Stable LTI system: \\[\\frac{dy}{dt}+ay(t)=Ku(t),\\quad a>0,K>0.\\]\nMeasurements: \\(|H(0)|=2\\), \\(|H(j3)|=8/5\\).\n1. (2 points) Determine a, K and H(jω).\n2. (2 points) Derive magnitude and phase and explain low-pass behavior.\n3. (2 points) Find steady-state output for \\(u(t)=5\\cos3t\\).",
  "question_language": "English",
  "math_notation": "LaTeX"
}
