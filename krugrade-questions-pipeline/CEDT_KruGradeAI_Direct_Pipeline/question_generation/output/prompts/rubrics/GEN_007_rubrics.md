ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_007
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_007",
  "reference_question_ids": [
    "REF_002"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Linear / Circular Convolution",
  "subtopic": "Sparse support and periodicity",
  "concept_tags": [
    "Discrete impulses",
    "linear convolution",
    "circular convolution",
    "support analysis",
    "periodic indexing",
    "output validity"
  ],
  "difficulty": "Medium",
  "question_type": "Matching + Support Proof",
  "rubric_max_score": 8.0,
  "learning_objective": "Use impulse support and modular indexing to determine which convolution operation can produce each recording.",
  "question_text": "\\[x[n]=\\delta[n]+2\\delta[n-4],\\quad h_1[n]=\\delta[n]-\\delta[n-3],\\quad h_2[n]=\\delta[n]+\\delta[n-2].\\]\nEach valid lab recording comes from full linear or 6-point circular convolution of x with h1 or h2:\nA: finite output nonzero at (index,value) {(0,1),(3,-1),(4,2),(7,-2)}.\nB: 6-periodic, one period (1,-2,0,-1,2,0).\nC: 6-periodic, one period (3,0,1,0,2,0).\nD: 6-periodic, one period (3,0,1,0,0,2).\nUnspecified finite-output samples are zero; periodic outputs repeat indefinitely.\n1. (2 points) Identify operation/filter for A.\n2. (2 points) Identify B and justify nonzero locations.\n3. (2 points) Identify C and explain wrap-around.\n4. (2 points) Determine whether D can be produced; justify by convolution support.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_007",
  "solution": "Step 1 — Delta convolution shifts impulses:\n\\[x*h_1=\\delta[n]-\\delta[n-3]+2\\delta[n-4]-2\\delta[n-7].\\]\n\\[x*h_2=\\delta[n]+\\delta[n-2]+2\\delta[n-4]+2\\delta[n-6].\\]\nStep 2 — The support and values of \\(x*h_1\\) match A exactly, so \\(A=x*h_1\\) (linear).\nStep 3 — Fold \\(x*h_1\\) modulo 6: indices 0→0,3→3,4→4,7→1. The circular period is \\((1,-2,0,-1,2,0)\\). So \\(B=x*_6h_1\\).\nStep 4 — Fold \\(x*h_2\\) modulo 6: indices 0 and 6 collide at index 0, giving 1+2=3; 2 has 1 and 4 has 2. Period \\((3,0,1,0,2,0)\\). So \\(C=x*_6h_2\\).\nStep 5 — D is nonzero at index 5. Circularly folded support for h1 is {0,1,3,4} and h2 is {0,2,4}; neither permits index 5. Neither full linear convolution is nonzero at n=5 either. Therefore D is impossible.",
  "final_answer": "A = x*h1 (linear), B = x*_6 h1 (circular), C = x*_6 h2 (circular), D invalid (index 5 cannot be nonzero)."
}
