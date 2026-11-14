ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_019
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_019",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Mixed harmonics and three-pole rational inverse",
  "concept_tags": [
    "Inverse DTFT",
    "trigonometric products",
    "complex exponentials",
    "three-term partial fractions",
    "causal sequences"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "rubric_max_score": 8.0,
  "learning_objective": "Recover finite impulse output from mixed harmonics and causal output from three-factor rational DTFT.",
  "question_text": "Find inverse DTFTs:\nPart A (3 points): \\[X_A(e^{j\\omega})=(1-j\\sin2\\omega)\\cos\\omega.\\]\nPart B (5 points): For \\(z=e^{-j\\omega}\\), \\[X_B(z)=\\frac{2+\\frac54z-\\frac58z^2}{(1-\\frac12z)(1+\\frac12z)(1-\\frac14z)}.\\]\nAssume causal expansion for Part B.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_019",
  "solution": "Part A — Step 1: \\(\\sin2\\omega\\cos\\omega=(\\sin3\\omega+\\sin\\omega)/2\\), so\n\\[X_A=\\cos\\omega-\\frac j2\\sin3\\omega-\\frac j2\\sin\\omega.\\]\nStep 2: Convert each harmonic to Euler exponentials, combine overlapping order-1 terms:\n\\[X_A=\\tfrac14e^{j\\omega}+\\tfrac34e^{-j\\omega}-\\tfrac14e^{j3\\omega}+\\tfrac14e^{-j3\\omega}.\\]\nStep 3: Invert:\n\\[x_A[n]=\\tfrac14\\delta[n+1]+\\tfrac34\\delta[n-1]-\\tfrac14\\delta[n+3]+\\tfrac14\\delta[n-3].\\]\nPart B — Step 1: Assume\n\\[X_B(z)=\\frac A{1-z/2}+\\frac B{1+z/2}+\\frac C{1-z/4}.\\]\nStep 2: Numerator matching yields\n\\[A+B+C=2,\\quad A/4-3B/4=5/4,\\quad-A/8+B/8-C/4=-5/8.\\]\nThus \\(A=2,B=-1,C=1\\).\nStep 3: The rational function equals\n\\[2/(1-z/2)-1/(1+z/2)+1/(1-z/4).\\]\nUsing causal pairs,\n\\[x_B[n]=[2(1/2)^n-(-1/2)^n+(1/4)^n]u[n].\\]",
  "final_answer": "\\(x_A[n]=\\tfrac14\\delta[n+1]+\\tfrac34\\delta[n-1]-\\tfrac14\\delta[n+3]+\\tfrac14\\delta[n-3]\\); \\(x_B[n]=[2(1/2)^n-(-1/2)^n+(1/4)^n]u[n]\\)."
}
