ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_025
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
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
SOLUTION:
{
  "question_id": "GEN_025",
  "solution": "Step 1 — ODE CTFT gives \\(H(j\\omega)=K/(a+j\\omega)\\), \\(|H|=K/\\sqrt{a^2+\\omega^2}\\). DC measurement implies K/a=2, so K=2a. At ω=3:\n\\[2a/\\sqrt{a^2+9}=8/5.\\]\nSquaring: \\(100a^2=64(a^2+9)\\) ⇒ \\(36a^2=576\\), so \\(a=4\\), \\(K=8\\). Thus \\(H=8/(4+j\\omega)\\).\nStep 2 — \\(|H|=8/\\sqrt{16+\\omega^2}\\), \\(\\angle H=-\\tan^{-1}(\\omega/4)\\). Magnitude has DC value 2, decreases with |ω| and tends to 0, so low-pass. Phase odd, zero at origin, tends to -π/2 for large positive ω.\nStep 3 — At ω=3, gain 8/5 and phase \\(-\\tan^{-1}(3/4)\\). Input amplitude 5 gives output amplitude 8:\n\\[y_{ss}(t)=8\\cos(3t-\\tan^{-1}(3/4)).\\]",
  "final_answer": "\\(a=4,K=8,H(j\\omega)=8/(4+j\\omega)\\); \\(y_{ss}(t)=8\\cos(3t-\\tan^{-1}(3/4))\\)."
}
