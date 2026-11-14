ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
Question slot: GEN_026
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_026",
  "reference_question_ids": [
    "REF_007"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "First-Order Frequency Response",
  "subtopic": "Compare two low-pass systems",
  "concept_tags": [
    "Transfer functions",
    "magnitude comparison",
    "phase shift",
    "low-pass behavior",
    "sinusoidal response"
  ],
  "learning_objective": "Compare attenuation and phase of two first-order systems having equal DC gain.",
  "question_type": "Comparison + Calculation",
  "difficulty": "Medium",
  "expected_methods": [
    "ODE transform",
    "gain/phase evaluation",
    "side-by-side sinusoidal outputs"
  ],
  "variation_strategy": "Two-system attenuation and phase comparison",
  "rubric_max_score": 6.0
}
