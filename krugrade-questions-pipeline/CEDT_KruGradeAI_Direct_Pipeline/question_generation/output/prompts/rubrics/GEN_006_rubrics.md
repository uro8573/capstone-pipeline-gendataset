ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_006
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_006",
  "reference_question_ids": [
    "REF_002"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Linear / Circular Convolution",
  "subtopic": "Same-pair linear vs circular",
  "concept_tags": [
    "Linear convolution",
    "circular convolution",
    "time-domain aliasing",
    "modular indexing",
    "output interpretation"
  ],
  "difficulty": "Medium",
  "question_type": "Calculation + Matching + Explanation",
  "rubric_max_score": 8.0,
  "learning_objective": "Distinguish full linear versus circular convolution and explain circular folding instead of truncation.",
  "question_text": "Given \\(a[n]=(2,-1,1,2)\\), \\(b[n]=(1,2,-1,1)\\), both on \\(0\\le n\\le3\\), zero elsewhere. A lab produces\n\\[R_A=(2,3,-3,7,2,-1,2),\\quad R_B=(4,2,\\square,7),\\quad R_C=(2,3,-3,7).\\]\nPermitted operations are full linear convolution or 4-point circular convolution of a,b; a recording may be an incorrect or truncated representation.\n1. (2 points) Calculate all seven samples of \\(y=a*b\\).\n2. (2 points) Calculate the four samples of \\(z=a*_4b\\).\n3. (2 points) Classify RA,RB,RC and recover missing RB value.\n4. (2 points) Determine whether circular convolution is just the first four samples of linear convolution, with mathematical justification.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_006",
  "solution": "Step 1 — Full linear convolution \\(y[n]=\\sum_k a[k]b[n-k]\\), length 7. Direct evaluations:\n\\[y[0]=2,\\ y[1]=4-1=3,\\ y[2]=-2-2+1=-3,\\]\n\\[y[3]=2+1+2+2=7,\\ y[4]=-1-1+4=2,\\ y[5]=1-2=-1,\\ y[6]=2.\\]\nSo \\(y=(2,3,-3,7,2,-1,2)\\).\nStep 2 — Circular convolution \\(z[n]=\\sum_{k=0}^3a[k]b[(n-k)\\bmod4]\\). Directly,\n\\[z[0]=2(1)+(-1)(1)+1(-1)+2(2)=4,\\]\n\\[z[1]=2(2)+(-1)(1)+1(1)+2(-1)=2,\\]\n\\[z[2]=2(-1)+(-1)(2)+1(1)+2(1)=-1,\\]\n\\[z[3]=2(1)+(-1)(-1)+1(2)+2(1)=7.\\]\nHence \\(z=(4,2,-1,7)\\).\nStep 3 — \\(R_A\\) is full linear convolution, \\(R_B\\) is circular convolution with missing -1, and \\(R_C\\) is a truncated linear output (not a valid full linear or circular result).\nStep 4 — In general \\(z[n]=\\sum_\\ell y[n+4\\ell]\\). For this example, \\(z=(y[0]+y[4],y[1]+y[5],y[2]+y[6],y[3])=(4,2,-1,7)\\). First four linear samples are \\((2,3,-3,7)\\). Thus simple truncation is incorrect: circular convolution folds the tail into the beginning.",
  "final_answer": "\\(a*b=(2,3,-3,7,2,-1,2)\\); \\(a*_4b=(4,2,-1,7)\\). RA linear, RB circular with □=-1, RC truncated/incorrect. Circular convolution uses folding, not truncation."
}
