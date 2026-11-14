ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_005
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_005",
  "reference_question_ids": [
    "REF_002"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Linear / Circular Convolution",
  "subtopic": "Missing-sample convolution matching",
  "concept_tags": [
    "Discrete convolution",
    "circular convolution",
    "missing sample reconstruction",
    "signal matching",
    "convolution sum property"
  ],
  "difficulty": "Medium",
  "question_type": "Matching + Calculation + Proof",
  "rubric_max_score": 8.0,
  "learning_objective": "Identify convolution operations from partially observed outputs, recover missing samples, and detect an inconsistent output.",
  "question_text": "Three sequences indexed from n=0 to 3 are\n\\[a[n]=(1,-1,2,0),\\quad b[n]=(1,1,-1,0),\\quad c[n]=(2,0,-1,1).\\]\nFour recordings are produced; each valid output uses either full linear or 4-point circular convolution of two DISTINCT sequences from a,b,c. Some measurements are missing (□); one output is inconsistent with all permitted convolutions:\n\\[Y_1=(2,2,-3,\\square,2,-1,0),\\]\n\\[Y_2=(2,-2,3,2,\\square,2,0),\\]\n\\[Y_3=(\\square,0,0,3),\\]\n\\[Y_4=(1,0,0,2,-2,0,0).\\]\n1. (2 points) Identify pair/type for Y1, recover missing sample.\n2. (2 points) Identify pair/type for Y2, recover missing sample.\n3. (2 points) Identify pair/type for Y3, recover missing sample.\n4. (2 points) Is Y4 possible? Justify using a mathematical property of convolution. Show calculations; circular convolution length N=4.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_005",
  "solution": "Step 1 — Full linear convolution of two length-4 sequences has length 7; 4-point circular convolution has length 4.\nStep 2 — Polynomial representations \\(A(z)=1-z+2z^2\\), \\(B(z)=1+z-z^2\\), \\(C(z)=2-z^2+z^3\\). Their products give\n\\[B(z)C(z)=2+2z-3z^2+2z^4-z^5,\\]\nso \\(b*c=(2,2,-3,0,2,-1,0)\\). Hence \\(Y_1=b*c\\) and missing value 0.\nLikewise\n\\[A(z)C(z)=2-2z+3z^2+2z^3-3z^4+2z^5,\\]\nso \\(a*c=(2,-2,3,2,-3,2,0)\\). Hence \\(Y_2=a*c\\) and missing value -3.\nStep 3 — \\(a*b=(1,0,0,3,-2,0,0)\\). Folding indices modulo 4 gives \\(a*_4b=(1+(-2),0,0,3)=(-1,0,0,3)\\). Hence \\(Y_3=a*_4b\\) and missing value -1.\nStep 4 — Convolution preserves the total-sum product: \\(\\sum_ny[n]=(\\sum_nx[n])(\\sum_nh[n])\\), for linear or circular (over one period). Input sums: \\(\\sum a=2\\), \\(\\sum b=1\\), \\(\\sum c=2\\); distinct-pair sums are 2 or 4. But \\(\\sum Y_4=1\\), so Y4 cannot arise from any allowed pair/type.",
  "final_answer": "Y1 = b*c (linear), □=0; Y2=a*c (linear), □=-3; Y3=a*_4b (circular), □=-1; Y4 invalid by sum property (sum=1, allowed sums 2 or 4)."
}
