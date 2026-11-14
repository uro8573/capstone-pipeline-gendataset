ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_027
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_027",
  "reference_question_ids": [
    "REF_007"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "First-Order Frequency Response",
  "subtopic": "Two-tone steady-state response",
  "concept_tags": [
    "Fourier transform of ODE",
    "frequency response",
    "sinusoidal steady state",
    "superposition",
    "low-pass filtering"
  ],
  "difficulty": "Medium",
  "question_type": "Modeling + Superposition",
  "rubric_max_score": 6.0,
  "learning_objective": "Predict response of a first-order LTI system to a two-frequency input.",
  "question_text": "A first-order LTI system satisfies \\[2\\frac{dy}{dt}+6y(t)=4u(t).\\]\nInput: \\(u(t)=3\\cos t+5\\sin4t\\). Assume zero initial conditions for frequency-response determination.\n1. (2 points) Derive H(jω), magnitude and phase.\n2. (2 points) Calculate the steady-state response to each sinusoidal component separately.\n3. (2 points) Sum to obtain complete steady-state response and identify which component is attenuated more strongly.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_027",
  "solution": "Step 1 — Transform ODE: \\((2j\\omega+6)Y=4U\\), hence\n\\[H(j\\omega)=4/(6+2j\\omega)=2/(3+j\\omega).\\]\nThus \\(|H|=2/\\sqrt{9+\\omega^2}\\), \\(\\angle H=-\\tan^{-1}(\\omega/3)\\).\nStep 2 — At ω=1, gain \\(2/\\sqrt{10}\\), phase \\(-\\tan^{-1}(1/3)\\). For \\(3\\cos t\\),\n\\[y_{1,ss}(t)=6/\\sqrt{10}\\cos(t-\\tan^{-1}(1/3)).\\]\nAt ω=4, gain \\(2/\\sqrt{25}=2/5\\), phase \\(-\\tan^{-1}(4/3)\\). For \\(5\\sin4t\\),\n\\[y_{2,ss}(t)=2\\sin(4t-\\tan^{-1}(4/3)).\\]\nStep 3 — By LTI superposition,\n\\[y_{ss}(t)=6/\\sqrt{10}\\cos(t-\\tan^{-1}(1/3))+2\\sin(4t-\\tan^{-1}(4/3)).\\]\nAt ω=1, magnitude gain ≈0.632; at ω=4 it is 0.4, so higher frequency experiences greater relative attenuation.",
  "final_answer": "\\(H(j\\omega)=2/(3+j\\omega)\\), \\(y_{ss}(t)=6/\\sqrt{10}\\cos(t-\\tan^{-1}(1/3))+2\\sin(4t-\\tan^{-1}(4/3))\\). Greater relative attenuation at ω=4."
}
