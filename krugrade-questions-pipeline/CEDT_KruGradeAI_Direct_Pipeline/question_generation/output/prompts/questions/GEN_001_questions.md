ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
Question slot: GEN_001
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_001",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Multi-bandwidth sinc signal",
  "concept_tags": [
    "CTFT",
    "sinc",
    "time-domain sampling",
    "impulse train",
    "spectral replication",
    "frequency-domain interpretation"
  ],
  "learning_objective": "Derive and interpret the sampled spectrum of a signal composed of components with different bandwidths.",
  "question_type": "Derivation + Sketching",
  "difficulty": "Medium",
  "expected_methods": [
    "CTFT pairs",
    "time scaling",
    "distribution sampling",
    "convolution theorem",
    "spectral support comparison"
  ],
  "variation_strategy": "Change mathematical object to multi-bandwidth sinc sum",
  "rubric_max_score": 5.0
}
