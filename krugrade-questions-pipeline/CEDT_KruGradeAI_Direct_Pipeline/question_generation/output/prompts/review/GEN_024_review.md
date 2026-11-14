ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_024
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_024",
  "reference_question_ids": [
    "REF_007"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "First-Order Frequency Response",
  "subtopic": "Mechanical system with nonunit derivative coefficient",
  "concept_tags": [
    "First-order ODE",
    "Fourier transform",
    "frequency response",
    "magnitude",
    "phase",
    "low-pass behavior"
  ],
  "learning_objective": "Derive first-order frequency response and predict sinusoidal steady-state response.",
  "question_type": "Modeling + Graph + Calculation",
  "difficulty": "Medium",
  "expected_methods": [
    "ODE transform",
    "magnitude/phase",
    "sinusoidal steady state",
    "frequency interpretation"
  ],
  "variation_strategy": "Nonunit derivative coefficient and output phase",
  "rubric_max_score": 6.0
}
QUESTION:
{
  "question_id": "GEN_024",
  "reference_question_ids": [
    "REF_007"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "First-Order Frequency Response",
  "subtopic": "Mechanical system with nonunit derivative coefficient",
  "concept_tags": [
    "First-order ODE",
    "Fourier transform",
    "frequency response",
    "magnitude",
    "phase",
    "low-pass behavior"
  ],
  "difficulty": "Medium",
  "question_type": "Modeling + Graph + Calculation",
  "rubric_max_score": 6.0,
  "learning_objective": "Derive first-order frequency response and predict sinusoidal steady-state response.",
  "question_text": "The velocity v(t) satisfies \\[2\\frac{dv}{dt}+4v(t)=F(t).\\] Assume zero initial conditions and LTI behavior.\n1. (2 points) Derive \\(H(j\\omega)=V(j\\omega)/F(j\\omega)\\).\n2. (2 points) Find magnitude and phase response; sketch qualitative behavior for positive and negative frequencies.\n3. (2 points) For \\(F(t)=10\\cos3t\\), find steady-state velocity and identify low-pass behavior.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_024",
  "solution": "Step 1 — Fourier-transform ODE: \\((2j\\omega+4)V=F\\), hence\n\\[H(j\\omega)=1/(4+2j\\omega).\\]\nStep 2 — Denominator modulus is \\(\\sqrt{16+4\\omega^2}\\), phase angle \\(\\tan^{-1}(\\omega/2)\\). Therefore\n\\[|H(j\\omega)|=1/\\sqrt{16+4\\omega^2}=1/(2\\sqrt{4+\\omega^2}),\\quad \\angle H=-\\tan^{-1}(\\omega/2).\\]\nMagnitude is even, peaks at 1/4 for ω=0 and tends to 0 as |ω|→∞. Phase odd, 0 at origin, tends to −π/2 at positive infinity and +π/2 at negative infinity. Sketch with these values.\nStep 3 — At ω=3, gain \\(1/(2\\sqrt{13})\\), phase \\(-\\tan^{-1}(3/2)\\). Input amplitude 10 produces output amplitude \\(5/\\sqrt{13}\\). Thus\n\\[v_{ss}(t)=(5/\\sqrt{13})\\cos(3t-\\tan^{-1}(3/2)).\\]\nDecreasing magnitude as |ω| rises implies low-pass response.",
  "final_answer": "\\(H(j\\omega)=1/(4+2j\\omega)\\); \\(|H|=1/(2\\sqrt{4+\\omega^2})\\), \\(\\angle H=-\\tan^{-1}(\\omega/2)\\); \\(v_{ss}(t)=5/\\sqrt{13}\\cos(3t-\\tan^{-1}(3/2))\\). Low-pass."
}
RUBRIC:
[
  {
    "question_id": "GEN_024",
    "criterion_id": "GEN_024_R1",
    "rubric_order": 1,
    "criterion": "Transfer function",
    "description": "Transfer function",
    "max_points": 2.0,
    "full_credit": "Correct Fourier transform and H(jω)",
    "partial_credit": "1 for correct setup with algebra error",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_007"
    ]
  },
  {
    "question_id": "GEN_024",
    "criterion_id": "GEN_024_R2",
    "rubric_order": 2,
    "criterion": "Magnitude and phase",
    "description": "Magnitude and phase",
    "max_points": 2.0,
    "full_credit": "Correct formulas limits and qualitative sketches",
    "partial_credit": "1 for formulas without complete sketches",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_007"
    ]
  },
  {
    "question_id": "GEN_024",
    "criterion_id": "GEN_024_R3",
    "rubric_order": 3,
    "criterion": "Steady-state response",
    "description": "Steady-state response",
    "max_points": 2.0,
    "full_credit": "Correct amplitude phase and low-pass explanation",
    "partial_credit": "1 for amplitude or phase only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_007"
    ]
  }
]
