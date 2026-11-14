ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_003
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_003",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Squared sinc and sampling comparison",
  "concept_tags": [
    "CTFT",
    "convolution theorem",
    "squared sinc",
    "triangular spectrum",
    "sampling frequency",
    "spectral replicas"
  ],
  "difficulty": "Medium",
  "question_type": "Derivation + Comparison + Sketching",
  "rubric_max_score": 5.0,
  "learning_objective": "Derive the spectrum of a squared-sinc signal and compare the effects of two sampling intervals.",
  "question_text": "Consider \\[x(t)=\\operatorname{sinc}^2(\\pi t/\\tau),\\quad\\tau>0.\\]\nSystem A samples at \\(T_A=\\tau/3\\); System B samples at \\(T_B=\\tau/4\\). In both cases \\(p_i(t)=\\sum_m\\delta(t-mT_i)\\), \\(g_i(t)=x(t)p_i(t)\\). You may use the sinc transform pair and multiplication-convolution theorem.\n1. (1 point) Derive \\(X(j\\omega)\\) in terms of \\(\\Lambda(u)=\\max(1-|u|,0)\\).\n2. (1 point) Express \\(g_A,g_B\\) as weighted impulse trains and find first positive zero-weight indices.\n3. (1 point) Derive \\(G_A,G_B\\).\n4. (1 point) Find replica centers, peak heights and bandwidths of both systems.\n5. (1 point) Sketch both spectra, compare replica separation and identify aliasing.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_003",
  "solution": "Step 1 — Let \\(s(t)=\\operatorname{sinc}(\\pi t/\\tau)\\), with \\(S(j\\omega)=\\tau\\operatorname{rect}(\\omega\\tau/(2\\pi))\\). Since \\(x=s^2\\), \\(X=(S*S)/(2\\pi)\\). Convolution of two identical rectangles gives\n\\[X(j\\omega)=\\tau\\Lambda(\\omega\\tau/(2\\pi)),\\]\npeak \\(\\tau\\), support \\(|\\omega|\\le2\\pi/\\tau\\), full width \\(4\\pi/\\tau\\).\nStep 2 —\n\\[g_A(t)=\\sum_m\\operatorname{sinc}^2(\\pi m/3)\\delta(t-m\\tau/3),\\]\n\\[g_B(t)=\\sum_m\\operatorname{sinc}^2(\\pi m/4)\\delta(t-m\\tau/4).\\]\nThe first positive zero-weight indices are \\(m=3\\) and \\(m=4\\), respectively; at \\(m=0\\) both weights equal 1.\nStep 3 — With \\(\\omega_{s,A}=6\\pi/\\tau\\) and \\(\\omega_{s,B}=8\\pi/\\tau\\),\n\\[G_A(j\\omega)=3\\sum_k\\Lambda((\\omega-6\\pi k/\\tau)\\tau/(2\\pi)),\\]\n\\[G_B(j\\omega)=4\\sum_k\\Lambda((\\omega-8\\pi k/\\tau)\\tau/(2\\pi)).\\]\nStep 4 — A replicas centered at \\(6\\pi k/\\tau\\), peak 3, width \\(4\\pi/\\tau\\), gaps \\(2\\pi/\\tau\\). B replicas centered at \\(8\\pi k/\\tau\\), peak 4, width \\(4\\pi/\\tau\\), gaps \\(4\\pi/\\tau\\).\nStep 5 — Sketch triangular replicas with linear slopes extending \\(2\\pi/\\tau\\) each side. In both systems \\(\\omega_s>4\\pi/\\tau\\), so no overlap/aliasing. System B has larger gaps.",
  "final_answer": "\\(X(j\\omega)=\\tau\\Lambda(\\omega\\tau/(2\\pi))\\). Both systems yield nonoverlapping triangular replicas. A: spacing \\(6\\pi/\\tau\\), peak 3; B: spacing \\(8\\pi/\\tau\\), peak 4. B has greater separation."
}
