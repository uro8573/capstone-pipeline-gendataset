ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_016
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_016",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Mixed harmonics and two geometric terms",
  "concept_tags": [
    "Trigonometric identities",
    "complex exponentials",
    "inverse DTFT",
    "partial fractions",
    "causal sequences"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "rubric_max_score": 8.0,
  "learning_objective": "Invert DTFT using harmonic expansion and rational partial fractions.",
  "question_text": "Find the inverse DTFT of both expressions, showing all steps.\nPart A (3 points): \\[X_A(e^{j\\omega})=(1+j\\sin\\omega)\\cos3\\omega.\\]\nPart B (5 points): \\[X_B(e^{j\\omega})=\\frac{1+2e^{-j\\omega}}{(1-\\frac12e^{-j\\omega})(1+\\frac13e^{-j\\omega})}.\\]\nFor Part B assume the causal geometric-series expansion.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_016",
  "solution": "Part A — Step 1: \\(\\sin\\omega\\cos3\\omega=(\\sin4\\omega-\\sin2\\omega)/2\\), so\n\\[X_A=\\cos3\\omega+\\frac j2\\sin4\\omega-\\frac j2\\sin2\\omega.\\]\nStep 2: Use Euler expansions:\n\\[X_A=\\tfrac12(e^{j3\\omega}+e^{-j3\\omega})+\\tfrac14(e^{j4\\omega}-e^{-j4\\omega})-\\tfrac14(e^{j2\\omega}-e^{-j2\\omega}).\\]\nStep 3: Since \\(e^{-j\\omega n_0}\\leftrightarrow\\delta[n-n_0]\\),\n\\[x_A[n]=\\tfrac12\\delta[n+3]+\\tfrac12\\delta[n-3]+\\tfrac14\\delta[n+4]-\\tfrac14\\delta[n-4]-\\tfrac14\\delta[n+2]+\\tfrac14\\delta[n-2].\\]\nPart B — Step 1: Set \\(z=e^{-j\\omega}\\). Then\n\\[X_B(z)=(1+2z)/((1-z/2)(1+z/3)).\\]\nStep 2: Write \\(X_B=A/(1-z/2)+B/(1+z/3)\\), giving \\(A+B=1\\), \\(A/3-B/2=2\\), hence \\(A=3,B=-2\\).\nStep 3: \\(X_B=3/(1-z/2)-2/(1+z/3)\\). Causal transform \\(1/(1-az)\\leftrightarrow a^nu[n]\\) gives\n\\[x_B[n]=[3(1/2)^n-2(-1/3)^n]u[n].\\]",
  "final_answer": "\\(x_A[n]=\\frac12\\delta[n+3]+\\frac12\\delta[n-3]+\\frac14\\delta[n+4]-\\frac14\\delta[n-4]-\\frac14\\delta[n+2]+\\frac14\\delta[n-2]\\); \\(x_B[n]=[3(1/2)^n-2(-1/3)^n]u[n]\\)."
}
