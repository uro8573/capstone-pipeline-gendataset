ROLE: University mathematics examination writer. Generate exactly ONE ORIGINAL question. Follow the approved blueprint slot. Change mathematical structure, representation, constraints, or reasoning requirement; changing numbers only is prohibited. Do not introduce unsupported topics. Do not show official reference solutions or simulated student answers. Return ONLY a JSON object with question_id, question_text, question_type, learning_objective, topic, subtopic, difficulty, concept_tags, reference_question_ids, rubric_max_score. Keep rubric_max_score consistent with the slot.
Question slot: GEN_009
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_009",
  "reference_question_ids": [
    "REF_003"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Series",
  "subtopic": "Periodic rectangular pulse properties",
  "concept_tags": [
    "Complex Fourier series",
    "DC component",
    "harmonic coefficients",
    "time shifting",
    "discontinuity",
    "coefficient decay"
  ],
  "learning_objective": "Evaluate coefficient and convergence claims for a periodic rectangular signal.",
  "question_type": "True/False with Justification",
  "difficulty": "Medium",
  "expected_methods": [
    "Complex Fourier coefficients",
    "phase shifting",
    "convergence at jump",
    "asymptotic decay"
  ],
  "variation_strategy": "Different rectangular-pulse parameters and harmonic structure",
  "rubric_max_score": 5.0
}
