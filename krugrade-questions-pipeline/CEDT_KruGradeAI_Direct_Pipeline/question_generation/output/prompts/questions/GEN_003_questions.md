ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
Question slot: GEN_003
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_003",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Squared sinc and sampling comparison",
  "concept_tags": [
    "CTFT",
    "convolution theorem",
    "squared sinc",
    "triangular spectrum",
    "sampling frequency",
    "spectral replicas"
  ],
  "learning_objective": "Derive the spectrum of a squared-sinc signal and compare the effects of two sampling intervals.",
  "question_type": "Derivation + Comparison + Sketching",
  "difficulty": "Medium",
  "expected_methods": [
    "CTFT",
    "frequency convolution",
    "sampling replicas",
    "support comparison"
  ],
  "variation_strategy": "Change mathematical object and compare two parameter regimes",
  "rubric_max_score": 5.0
}
