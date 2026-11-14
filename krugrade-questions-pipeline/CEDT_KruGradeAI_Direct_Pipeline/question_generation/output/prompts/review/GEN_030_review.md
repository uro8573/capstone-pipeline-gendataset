ROLE: Mathematical QA reviewer. Independently derive/check this new problem; verify numerical algebra, domain/conventions, final answer, rubric alignment, sum of points, difficulty and meaningful originality relative to the blueprint. Do NOT claim verification unless actually done. Return ONLY JSON with question_id, status (PASS/NEEDS_REVIEW/FAIL), issues, suggested_fixes, independent_checks_performed.
Question slot: GEN_030
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
BLUEPRINT SLOT:
{
  "question_id": "GEN_030",
  "reference_question_ids": [
    "REF_008"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "LTI Inverse & Echo Cancellation",
  "subtopic": "Finite inverse approximation and residual echo",
  "concept_tags": [
    "Inverse convolution",
    "geometric recurrence",
    "finite inverse filter",
    "residual echo",
    "approximation error"
  ],
  "learning_objective": "Derive a finite inverse approximation and quantify residual echoes due to truncation.",
  "question_type": "Proof + Approximation",
  "difficulty": "Hard",
  "expected_methods": [
    "Echo recurrence",
    "finite geometric series",
    "convolution",
    "logarithmic threshold"
  ],
  "variation_strategy": "Truncated echo inverse and residual error",
  "rubric_max_score": 5.0
}
QUESTION:
{
  "question_id": "GEN_030",
  "reference_question_ids": [
    "REF_008"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "LTI Inverse & Echo Cancellation",
  "subtopic": "Finite inverse approximation and residual echo",
  "concept_tags": [
    "Inverse convolution",
    "geometric recurrence",
    "finite inverse filter",
    "residual echo",
    "approximation error"
  ],
  "difficulty": "Hard",
  "question_type": "Proof + Approximation",
  "rubric_max_score": 5.0,
  "learning_objective": "Derive a finite inverse approximation and quantify residual echoes due to truncation.",
  "question_text": "Echo channel\n\\[h(t)=\\delta(t)+\\frac23\\delta(t-T),\\quad T>0.\\]\nApproximate ideal inverse by \\(g_M(t)=\\sum_{k=0}^Mg_k\\delta(t-kT)\\).\n1. (1 point) State/justify perfect inverse condition.\n2. (1 point) Derive recurrence for ideal gk.\n3. (2 points) For M=2, obtain g2(t) and compute overall h*g2.\n4. (1 point) Find smallest integer M≥0 for which residual echo coefficient magnitude is strictly below 0.1.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
GOLD SOLUTION (REVIEW STAGE ONLY):
{
  "question_id": "GEN_030",
  "solution": "Step 1 — For arbitrary input exact recovery requires \\(h*g=\\delta\\), since δ is convolution identity.\nStep 2 — Match coefficients in \\((\\delta+(2/3)\\delta_T)*\\sum_{k\\ge0}g_k\\delta_{kT}\\): \\(g_0=1\\), \\(g_k+(2/3)g_{k-1}=0\\) for k≥1. Hence \\(g_k=(-2/3)^k\\).\nStep 3 — For M=2: \\(g_0=1,g_1=-2/3,g_2=4/9\\), so\n\\[g_2(t)=\\delta(t)-\\tfrac23\\delta(t-T)+\\tfrac49\\delta(t-2T).\\]\nConvolution with h cancels coefficients at delays T and 2T, leaving\n\\[(h*g_2)(t)=\\delta(t)+\\frac8{27}\\delta(t-3T).\\]\nThus for input x, output \\(z(t)=x(t)+(8/27)x(t-3T)\\).\nStep 4 — The finite geometric identity \\((1+az)\\sum_{k=0}^M(-az)^k=1-(-az)^{M+1}\\) yields\n\\[(h*g_M)(t)=\\delta(t)-(-2/3)^{M+1}\\delta(t-(M+1)T).\\]\nResidual magnitude \\((2/3)^{M+1}\\). Require \\((2/3)^{M+1}<0.1\\), so \\(M+1>\\ln(0.1)/\\ln(2/3)\\approx5.68\\). Smallest integer M=5. Check \\((2/3)^6=64/729\\approx0.0878<0.1\\), but \\((2/3)^5\\approx0.1317\\ge0.1\\).",
  "final_answer": "\\(g_k=(-2/3)^k\\); \\(g_2(t)=\\delta(t)-(2/3)\\delta(t-T)+(4/9)\\delta(t-2T)\\); \\((h*g_2)(t)=\\delta(t)+(8/27)\\delta(t-3T)\\); \\(M_{min}=5\\)."
}
RUBRIC:
[
  {
    "question_id": "GEN_030",
    "criterion_id": "GEN_030_R1",
    "rubric_order": 1,
    "criterion": "Inverse condition",
    "description": "Inverse condition",
    "max_points": 1.0,
    "full_credit": "Correct h*g=δ with explanation",
    "partial_credit": "0.5 for condition only",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_008"
    ]
  },
  {
    "question_id": "GEN_030",
    "criterion_id": "GEN_030_R2",
    "rubric_order": 2,
    "criterion": "Recurrence",
    "description": "Recurrence",
    "max_points": 1.0,
    "full_credit": "Correct geometric coefficient formula",
    "partial_credit": "0.5 for recurrence without closed form",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_008"
    ]
  },
  {
    "question_id": "GEN_030",
    "criterion_id": "GEN_030_R3",
    "rubric_order": 3,
    "criterion": "Finite inverse",
    "description": "Finite inverse",
    "max_points": 2.0,
    "full_credit": "Correct g2 and residual impulse",
    "partial_credit": "1 for g2 without residual calculation",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_008"
    ]
  },
  {
    "question_id": "GEN_030",
    "criterion_id": "GEN_030_R4",
    "rubric_order": 4,
    "criterion": "Truncation requirement",
    "description": "Truncation requirement",
    "max_points": 1.0,
    "full_credit": "Correct M=5 with inequality",
    "partial_credit": "0.5 for residual formula but wrong integer",
    "common_mistakes": "",
    "reference_question_ids": [
      "REF_008"
    ]
  }
]
