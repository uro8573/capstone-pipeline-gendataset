ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
Question slot: GEN_004
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_004",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Reconstructing bandpass from sampled spectrum",
  "concept_tags": [
    "Inverse CTFT",
    "spectral replication",
    "frequency shifting",
    "bandpass signals",
    "sampling reconstruction"
  ],
  "learning_objective": "Infer the original signal and sampling parameters from a known nonoverlapping sampled spectrum.",
  "question_type": "Inverse Reasoning + Sketching",
  "difficulty": "Medium",
  "expected_methods": [
    "Spectral replica identification",
    "inverse CTFT",
    "modulation",
    "sampling"
  ],
  "variation_strategy": "Infer unknown original from sampled frequency domain",
  "rubric_max_score": 5.0
}
