ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
Question slot: GEN_007
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_007",
  "reference_question_ids": [
    "REF_002"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Linear / Circular Convolution",
  "subtopic": "Sparse support and periodicity",
  "concept_tags": [
    "Discrete impulses",
    "linear convolution",
    "circular convolution",
    "support analysis",
    "periodic indexing",
    "output validity"
  ],
  "learning_objective": "Use impulse support and modular indexing to determine which convolution operation can produce each recording.",
  "question_type": "Matching + Support Proof",
  "difficulty": "Medium",
  "expected_methods": [
    "Delta convolution",
    "modular support reduction",
    "periodic output interpretation"
  ],
  "variation_strategy": "Sparse support and periodic invalid-output detection",
  "rubric_max_score": 8.0
}
