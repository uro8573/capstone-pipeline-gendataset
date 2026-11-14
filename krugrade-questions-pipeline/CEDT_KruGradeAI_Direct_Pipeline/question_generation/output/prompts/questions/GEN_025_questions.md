ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
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
