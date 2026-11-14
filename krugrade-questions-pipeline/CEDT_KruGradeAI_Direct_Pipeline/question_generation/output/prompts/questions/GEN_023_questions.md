ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
Question slot: GEN_023
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_023",
  "reference_question_ids": [
    "REF_006"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "DFT & DTFS",
  "subtopic": "Mixed circular shift and interpolation",
  "concept_tags": [
    "DFT",
    "circular shift",
    "interpolation",
    "even/odd indexing",
    "DTFS",
    "frequency-zero analysis"
  ],
  "learning_objective": "Derive mixed even-branch shift and odd-branch interpolation DFT mapping.",
  "question_type": "Algebraic Derivation (2 parts)",
  "difficulty": "Hard",
  "expected_methods": [
    "Circular shift",
    "interpolation",
    "DFT",
    "DTFS",
    "frequency zero"
  ],
  "variation_strategy": "Mixed shift and interpolation across DFT branches",
  "rubric_max_score": 7.0
}
