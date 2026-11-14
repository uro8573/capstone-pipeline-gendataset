ROLE: Math grading-rubric designer. Split the solution into independently observable criteria with full/partial-credit guidance and common mistakes. Sum max_points exactly to the question score. Do not add credit for final answer twice. Return ONLY JSON list of criterion rows containing question_id, criterion_id, rubric_order, criterion, description, max_points, full_credit, partial_credit, common_mistakes, reference_question_ids.
Question slot: GEN_002
Mathematical conventions: CTFT: X(jω)=∫x(t)e^{-jωt}dt; inverse CTFT factor 1/(2π). DTFT: X(e^{jω})=Σx[n]e^{-jωn}; sinc(u)=sin(u)/u, sinc(0)=1. Use LaTeX mathematical notation and preserve the target university midterm level.
QUESTION:
{
  "question_id": "GEN_002",
  "reference_question_ids": [
    "REF_001"
  ],
  "subject": "Computer Engineering Mathematics II",
  "topic": "Fourier Transform & Sampling",
  "subtopic": "Inverse CTFT and sampling",
  "concept_tags": [
    "Inverse CTFT",
    "time shifting",
    "cosine modulation in frequency",
    "sampling",
    "spectral replication"
  ],
  "difficulty": "Medium",
  "question_type": "Inverse Derivation + Sketching",
  "rubric_max_score": 5.0,
  "learning_objective": "Recover a time-domain signal from its frequency-domain representation and predict its sampled spectrum.",
  "question_text": "A continuous-time signal has frequency representation\n\\[X(j\\omega)=\\tau\\operatorname{rect}\\left(\\frac{\\omega\\tau}{2\\pi}\\right)\\left[1+\\cos\\left(\\frac{\\omega\\tau}{2}\\right)\\right],\\quad\\tau>0.\\]\nSample using an impulse train of period \\(T_s=\\tau/4\\).\n1. (1 point) Find \\(x(t)\\).\n2. (1 point) Express \\(g(t)\\) as an impulse train and determine weights for \\(m=0,\\pm2\\).\n3. (1 point) Derive \\(P(j\\omega)\\) and replica spacing.\n4. (1 point) Derive \\(G(j\\omega)\\).\n5. (1 point) Sketch central and nearest two replicas, label heights/support and determine aliasing.",
  "question_language": "English",
  "math_notation": "LaTeX"
}
SOLUTION:
{
  "question_id": "GEN_002",
  "solution": "Step 1 — Write \\(X=X_0+(e^{j\\omega\\tau/2}/2)X_0+(e^{-j\\omega\\tau/2}/2)X_0\\), where \\(X_0=\\tau\\operatorname{rect}(\\omega\\tau/(2\\pi))\\). Inverse CTFT with time shifting yields\n\\[x(t)=\\operatorname{sinc}(\\pi t/\\tau)+\\tfrac12\\operatorname{sinc}(\\pi(t+\\tau/2)/\\tau)+\\tfrac12\\operatorname{sinc}(\\pi(t-\\tau/2)/\\tau).\\]\nStep 2 — At \\(t_m=m\\tau/4\\), sample weights are\n\\[w_m=\\operatorname{sinc}(\\pi m/4)+\\tfrac12\\operatorname{sinc}(\\pi(m+2)/4)+\\tfrac12\\operatorname{sinc}(\\pi(m-2)/4).\\]\nThus \\(g(t)=\\sum_mw_m\\delta(t-m\\tau/4)\\). Using sinc(0)=1 and sinc(π/2)=2/π: \\(w_0=1+2/\\pi\\), \\(w_{\\pm2}=1/2+2/\\pi\\).\nStep 3 — \\(\\omega_s=2\\pi/T_s=8\\pi/\\tau\\), so\n\\[P(j\\omega)=\\frac{8\\pi}{\\tau}\\sum_k\\delta(\\omega-8\\pi k/\\tau).\\]\nStep 4 — Define \\(\\Omega_k=\\omega-8\\pi k/\\tau\\). Spectral sampling produces\n\\[G(j\\omega)=4\\sum_k\\operatorname{rect}(\\Omega_k\\tau/(2\\pi))[1+\\cos(\\Omega_k\\tau/2)].\\]\nStep 5 — Each copy is centered at \\(8\\pi k/\\tau\\), supported within \\(|\\omega-8\\pi k/\\tau|<\\pi/\\tau\\). At the center the height is 8; approaching the support boundary from within it is 4. Draw curved peaks over each rectangular support (with a jump to zero at the edge). Copies do not overlap because spacing \\(8\\pi/\\tau\\) exceeds support width \\(2\\pi/\\tau\\).",
  "final_answer": "\\(x(t)=\\operatorname{sinc}(\\pi t/\\tau)+\\tfrac12\\operatorname{sinc}(\\pi(t+\\tau/2)/\\tau)+\\tfrac12\\operatorname{sinc}(\\pi(t-\\tau/2)/\\tau)\\); sampled replicas centered at \\(8\\pi k/\\tau\\), peak 8, no aliasing."
}
