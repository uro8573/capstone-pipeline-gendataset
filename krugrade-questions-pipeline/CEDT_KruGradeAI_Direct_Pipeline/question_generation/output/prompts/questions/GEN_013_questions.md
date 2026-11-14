ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
Question slot: GEN_013
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_013",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Difference of rational kernels",
  "concept_tags": [
    "CTFT linearity",
    "scaling",
    "convolution theorem",
    "superposition",
    "transform uniqueness"
  ],
  "learning_objective": "Prove convolution of a linear combination of rational functions by Fourier superposition.",
  "question_type": "Mathematical Proof",
  "difficulty": "Hard",
  "expected_methods": [
    "CTFT linearity",
    "scaling",
    "convolution multiplication",
    "inverse transform"
  ],
  "variation_strategy": "Superposition of rational kernel components",
  "rubric_max_score": 6.0
}
