ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
Question slot: GEN_008
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_008",
  "reference_question_ids": [
    "REF_002"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Linear / Circular Convolution",
  "subtopic": "Nonunique cancellation matching",
  "concept_tags": [
    "Linear convolution",
    "circular convolution",
    "signal cancellation",
    "finite differences",
    "periodicity",
    "nonunique matching"
  ],
  "learning_objective": "Understand how cancellation permits distinct input-filter pairs to produce the same linear and circular outputs.",
  "question_type": "Matching + Cancellation Explanation",
  "difficulty": "Medium",
  "expected_methods": [
    "Finite difference filter",
    "linear convolution",
    "circular folding",
    "cancellation"
  ],
  "variation_strategy": "Nonuniqueness and signal cancellation",
  "rubric_max_score": 8.0
}
