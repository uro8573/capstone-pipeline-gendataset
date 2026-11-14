ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_025
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
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
  "learning_objective": "Recover unknown first-order parameters from two measured magnitudes and predict an output.",
  "question_type": "System Identification + Calculation",
  "difficulty": "Medium",
  "expected_methods": [
    "ODE CTFT",
    "magnitude equations",
    "parameter solving",
    "sinusoidal response"
  ],
  "variation_strategy": "Inverse system identification from measurements",
  "rubric_max_score": 6.0
}
QUESTION:
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
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_025",
  "solution": "Step 1 — ODE CTFT gives \\(H(j\\omega)=K/(a+j\\omega)\\), \\(|H|=K/\\sqrt{a^2+\\omega^2}\\). DC measurement implies K/a=2, so K=2a. At ω=3:\n\\[2a/\\sqrt{a^2+9}=8/5.\\]\nSquaring: \\(100a^2=64(a^2+9)\\) ⇒ \\(36a^2=576\\), so \\(a=4\\), \\(K=8\\). Thus \\(H=8/(4+j\\omega)\\).\nStep 2 — \\(|H|=8/\\sqrt{16+\\omega^2}\\), \\(\\angle H=-\\tan^{-1}(\\omega/4)\\). Magnitude has DC value 2, decreases with |ω| and tends to 0, so low-pass. Phase odd, zero at origin, tends to -π/2 for large positive ω.\nStep 3 — At ω=3, gain 8/5 and phase \\(-\\tan^{-1}(3/4)\\). Input amplitude 5 gives output amplitude 8:\n\\[y_{ss}(t)=8\\cos(3t-\\tan^{-1}(3/4)).\\]",
  "final_answer": "\\(a=4,K=8,H(j\\omega)=8/(4+j\\omega)\\); \\(y_{ss}(t)=8\\cos(3t-\\tan^{-1}(3/4))\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_025",
    "criterion_id": "GEN_025_R1",
    "rubric_order": 1,
    "criterion": "Parameter identification",
    "description": "Parameter identification",
    "max_points": 2.0,
    "full_credit": "Correct a=4 K=8 and transfer function",
    "partial_credit": "1 for setup with arithmetic error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_007"
    ]
  },
  {
    "question_id": "GEN_025",
    "criterion_id": "GEN_025_R2",
    "rubric_order": 2,
    "criterion": "Frequency response",
    "description": "Frequency response",
    "max_points": 2.0,
    "full_credit": "Correct magnitude phase and low-pass explanation",
    "partial_credit": "1 for formulas without interpretation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_007"
    ]
  },
  {
    "question_id": "GEN_025",
    "criterion_id": "GEN_025_R3",
    "rubric_order": 3,
    "criterion": "Output calculation",
    "description": "Output calculation",
    "max_points": 2.0,
    "full_credit": "Correct amplitude and phase",
    "partial_credit": "1 for one component correct",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_007"
    ]
  }
]
