ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
Question slot: GEN_014
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_014",
  "reference_question_ids": [
    "REF_004"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "CTFT Convolution Identity",
  "subtopic": "Second-derivative convolution",
  "concept_tags": [
    "Time differentiation",
    "second derivative",
    "CTFT",
    "convolution theorem",
    "transform uniqueness"
  ],
  "learning_objective": "Prove a second-derivative convolution identity via the Fourier differentiation property.",
  "question_type": "Mathematical Proof",
  "difficulty": "Hard",
  "expected_methods": [
    "Differentiation",
    "Fourier derivative property",
    "convolution theorem",
    "uniqueness"
  ],
  "variation_strategy": "Higher derivative rational kernel",
  "rubric_max_score": 6.0
}
