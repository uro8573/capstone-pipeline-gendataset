ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
Question slot: GEN_018
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_018",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Time-advanced finite and infinite sequences",
  "concept_tags": [
    "DTFT time shifting",
    "impulse index signs",
    "partial fractions",
    "causal expansion",
    "left-sided advancement"
  ],
  "learning_objective": "Apply frequency-domain time advance to both finite and infinite DTFT sequences.",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "difficulty": "Medium",
  "expected_methods": [
    "Trig expansion",
    "partial fractions",
    "causal inverse",
    "DTFT time shifting"
  ],
  "variation_strategy": "Frequency-domain phase and shifted sequence support",
  "rubric_max_score": 8.0
}
