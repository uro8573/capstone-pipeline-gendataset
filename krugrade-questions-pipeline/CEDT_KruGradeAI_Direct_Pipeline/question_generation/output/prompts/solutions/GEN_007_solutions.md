ROLE: Independent mathematics solver. Solve this question thoroughly without consulting any previous/official solution. Check assumptions, boundary cases, signs, indices and final result; perform a second verification method if practical. If ambiguous or inconsistent, explain it rather than fabricating a solution. Return ONLY JSON with question_id, solution, final_answer, mathematical_review_notes.
Question slot: GEN_007
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION ONLY (NO GOLD ANSWER):
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
