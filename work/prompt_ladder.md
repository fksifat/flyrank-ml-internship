# Prompt Ladder: Explaining ML to Stakeholders

This document tracks the evolution of a single prompt from a lazy baseline to an engineered asset, testing one new layer at a time.

---

### Baseline Prompt (The Lazy Start)
**Prompt:** Explain random forests to me.

**Output (Excerpt):** 
> *A random forest is an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time. For classification tasks, the output of the random forest is the class selected by most trees...*

**Notes:**
*   **What changed in the prompt:** N/A (Baseline).
*   **What actually improved:** N/A.
*   **What still failed:** It reads like a Wikipedia article. It explains the math (ensemble, classification) but provides zero connection to what I am actually trying to do with it.
*   **What I will try next:** Add a specific audience layer so it stops using technical jargon.

---

### Version 1: Add Audience
**Prompt:** Explain random forests to an SEO Content Director who has no math background.

**Output (Excerpt):** 
> *Imagine a random forest as a committee of SEO experts. Instead of relying on one person's opinion (a single decision tree) to make a choice, you ask a hundred different experts. Each expert looks at slightly different information, and then they all vote...*

**Notes:**
*   **What changed in the prompt:** Added a specific audience constraint (SEO Content Director, no math background).
*   **What actually improved:** The jargon disappeared entirely. "Ensemble learning" was replaced with a highly understandable "committee" analogy. 
*   **What still failed:** It's a great analogy, but it's totally abstract. The Director doesn't know *what* the committee is voting on.
*   **What I will try next:** Add real business context.

---

### Version 2: Add Real Context
**Prompt:** Explain random forests to an SEO Content Director who has no math background. Context: We are using a random forest to predict which of our 30,000 pages are going to decline in traffic so we can prioritize our content refresh queue.

**Output (Excerpt):**
> *Think of the random forest as a committee of hundreds of content auditors. If you asked just one auditor to find decaying pages, they might only look at one thing, like page age, and make mistakes. The random forest looks at age, CTR drops, search volume, and engagement all at once. The "committee" votes, and the pages with the most "at-risk" votes get pushed to the top of your refresh queue.*

**Notes:**
*   **What changed in the prompt:** Added specific project context (predicting traffic decline for 30k pages to prioritize refreshes).
*   **What actually improved:** The output suddenly became highly relevant. It stopped talking about generic "decisions" and started talking specifically about finding decaying pages based on CTR and age.
*   **What still failed:** The AI generated a massive wall of text (4 long paragraphs). A busy Director won't read it.
*   **What I will try next:** Specify a strict output format.

---

### Version 3: Specify Output Format
**Prompt:** Explain random forests to an SEO Content Director who has no math background. Context: We are using a random forest to predict which of our 30,000 pages are going to decline in traffic so we can prioritize our content refresh queue. Format: Give me exactly three bullet points.

**Output (Excerpt):**
> * **The "Committee" Approach:** Instead of relying on one simple rule, the random forest acts like a committee of hundreds of virtual auditors voting on whether a page is decaying.
> * **Smarter Signal Reading:** It simultaneously looks at dozens of signals—like CTR drops, page age, and traffic patterns—to spot complex signs of decline that a human would miss.
> * **Actionable Prioritization:** It outputs a precise, ranked priority queue, telling your team exactly which of the 30,000 pages to refresh first for maximum impact.

**Notes:**
*   **What changed in the prompt:** Constrained the format to exactly three bullet points.
*   **What actually improved:** It is now instantly readable and scannable. The fluff is gone, leaving only the core value proposition.
*   **What still failed (Honest negative):** While concise, it doesn't really explain *why* this is better than what the Director is currently doing. It lacks contrast.
*   **What I will try next:** Add a constraint to contrast it with the baseline method.

---

### Version 4: Add Constraints (Contrast)
**Prompt:** Explain random forests to an SEO Content Director who has no math background. Context: We are using a random forest to predict which of our 30,000 pages are going to decline in traffic so we can prioritize our content refresh queue. Format: Give me exactly three bullet points. Constraint: You must explicitly contrast this model with our old method, which was a rigid rule ('update pages older than 6 months').

**Output (Excerpt):**
> * **Moves Beyond Rigid Rules:** Our old "update if older than 6 months" rule was blind; it updated fine pages and missed young, crashing pages. The random forest replaces this with dynamic intelligence.
> * **Multidimensional Analysis:** Like a committee of hundreds of auditors, it looks at age, CTR, and traffic simultaneously, rather than relying on one isolated metric.
> * **Hyper-Targeted Queue:** The result is a highly accurate priority list that ensures your team only spends time refreshing pages that genuinely need it, skyrocketing ROI.

**Notes:**
*   **What changed in the prompt:** Added a constraint requiring contrast with the old "6-month" rule.
*   **What actually improved:** The argument became incredibly persuasive. It didn't just explain the model; it proved its business value by attacking the flaws in the status quo.
*   **What still failed (Honest negative):** The tone got way too "salesy." Phrases like "skyrocketing ROI" and "dynamic intelligence" sound like a vendor pitch, not an internal update. Adding the constraint accidentally shifted the AI's persona.
*   **What I will try next:** Add a tone/quality criteria layer to fix the voice.

---

### Version 5: Add Tone / Quality Criteria
**Prompt:** Explain random forests to an SEO Content Director who has no math background. Context: We are using a random forest to predict which of our 30,000 pages are going to decline in traffic so we can prioritize our content refresh queue. Format: Give me exactly three bullet points. Constraint: You must explicitly contrast this model with our old method, which was a rigid rule ('update pages older than 6 months'). Tone: Direct, plainspoken, evidence-backed, no buzzwords.

**Output (Excerpt):**
> * **Better than rigid rules:** The old "update if older than 6 months" rule wasted time on healthy pages and missed newer ones that were losing traffic.
> * **Weighs multiple signals:** The random forest acts like a committee of auditors. It looks at age, CTR, and traffic drops simultaneously to make a more accurate decision than any single rule could.
> * **Clear prioritization:** It gives us a ranked list of the 50 pages most likely to decline, so the editorial team only spends time where it actually matters.

**Notes:**
*   **What changed in the prompt:** Added the tone constraint ("Direct, plainspoken, evidence-backed, no buzzwords").
*   **What actually improved:** The marketing fluff is gone. It sounds exactly like a competent, professional data analyst explaining a new system to their boss. 

---

### Final Reusable Prompt
*(Cleaned up for a stranger to use for any stakeholder explanation)*

**Role & Goal:** Explain [TECHNICAL CONCEPT] to a [SPECIFIC AUDIENCE ROLE] who has no background in [TECHNICAL FIELD]. 
**Context:** We are using this to [SPECIFIC BUSINESS GOAL OR USE CASE]. 
**Format:** Provide exactly three bullet points. 
**Constraint:** You must explicitly contrast this new approach with [THE OLD WAY THEY USED TO DO IT]. 
**Tone:** Direct, plainspoken, evidence-backed, no buzzwords. Do not sound like a salesperson.
