ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_017
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_017",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Symmetric harmonics and alternating causal terms",
  "concept_tags": [
    "Product-to-sum",
    "symmetric impulse sequences",
    "partial fractions",
    "alternating geometric sequences"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "rubric_max_score": 8.0,
  "learning_objective": "Use symmetry to invert trigonometric spectra and distinguish geometric components.",
  "question_text": "Find both inverse DTFT sequences.\nPart A (3 points): \\[X_A(e^{j\\omega})=2\\cos\\omega\\cos2\\omega.\\]\nPart B (5 points): \\[X_B(e^{j\\omega})=\\frac{3+\\frac16e^{-j\\omega}}{(1-\\frac12e^{-j\\omega})(1+\\frac13e^{-j\\omega})}.\\]\nUse the causal expansion in Part B.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_017",
  "solution": "Part A — Step 1: \\(2\\cos\\omega\\cos2\\omega=\\cos3\\omega+\\cos\\omega\\).\nStep 2: \\(X_A=(e^{j3\\omega}+e^{-j3\\omega}+e^{j\\omega}+e^{-j\\omega})/2\\).\nStep 3: Thus\n\\[x_A[n]=\\tfrac12(\\delta[n+3]+\\delta[n-3]+\\delta[n+1]+\\delta[n-1]).\\]\nPart B — Step 1: With \\(z=e^{-j\\omega}\\), write\n\\[X_B(z)=(3+z/6)/((1-z/2)(1+z/3))=A/(1-z/2)+B/(1+z/3).\\]\nStep 2: Equate \\(A+B=3\\), \\(A/3-B/2=1/6\\). Solve \\(A=2,B=1\\).\nStep 3: Using causal geometric DTFT pairs,\n\\[X_B(z)=2/(1-z/2)+1/(1+z/3)\\]\nbecomes\n\\[x_B[n]=[2(1/2)^n+(-1/3)^n]u[n].\\]\nThe second component alternates sign because its base is negative.",
  "final_answer": "\\(x_A[n]=[\\delta[n+3]+\\delta[n-3]+\\delta[n+1]+\\delta[n-1]]/2\\); \\(x_B[n]=[2(1/2)^n+(-1/3)^n]u[n]\\)."
}
