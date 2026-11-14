ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_018
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_018",
  "reference_question_ids": [
    "REF_005"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Inverse DTFT",
  "subtopic": "Time-advanced finite and infinite sequences",
  "concept_tags": [
    "DTFT time shifting",
    "impulse index signs",
    "partial fractions",
    "causal expansion",
    "left-sided advancement"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse DTFT Calculation (2 parts)",
  "rubric_max_score": 8.0,
  "learning_objective": "Apply frequency-domain time advance to both finite and infinite DTFT sequences.",
  "question_text": "Find the inverse DTFTs:\nPart A (3 points): \\[X_A(e^{j\\omega})=e^{j2\\omega}(1-\\cos2\\omega).\\]\nPart B (5 points): \\[X_B(e^{j\\omega})=e^{j2\\omega}\\frac{1+e^{-j\\omega}}{(1-\\frac12e^{-j\\omega})(1+\\frac14e^{-j\\omega})}.\\]\nFor Part B invert the rational factor with the causal expansion first, then use time shifting.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_018",
  "solution": "Part A — Step 1: \\(1-\\cos2\\omega=1-\\tfrac12e^{j2\\omega}-\\tfrac12e^{-j2\\omega}\\).\nStep 2: Multiply by \\(e^{j2\\omega}\\): \\(X_A=e^{j2\\omega}-\\tfrac12e^{j4\\omega}-\\tfrac12\\).\nStep 3: Inverse mapping gives\n\\[x_A[n]=\\delta[n+2]-\\tfrac12\\delta[n+4]-\\tfrac12\\delta[n].\\]\nPart B — Step 1: Set \\(z=e^{-j\\omega}\\), define \\(W(z)=(1+z)/((1-z/2)(1+z/4))\\).\nStep 2: Decompose \\(W=A/(1-z/2)+B/(1+z/4)\\). Matching \\(A+B=1\\), \\(A/4-B/2=1\\) gives \\(A=2,B=-1\\).\nStep 3: Causal sequence of W:\n\\[w[n]=[2(1/2)^n-(-1/4)^n]u[n].\\]\nStep 4: Since multiplication by \\(e^{j2\\omega}\\) advances by two samples,\n\\[x_B[n]=w[n+2]=[2(1/2)^{n+2}-(-1/4)^{n+2}]u[n+2].\\]\nThe resulting sequence begins at n=-2 even though the unshifted rational factor had a causal inverse.",
  "final_answer": "\\(x_A[n]=\\delta[n+2]-\\frac12\\delta[n+4]-\\frac12\\delta[n]\\); \\(x_B[n]=[2(1/2)^{n+2}-(-1/4)^{n+2}]u[n+2]\\)."
}
