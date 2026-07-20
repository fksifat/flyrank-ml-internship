# FL-01 Workflow Audit

## Part 1: Recurring Tasks Classification

| Task | Classification | Rationale |
| :--- | :--- | :--- |
| **1. Reading and understanding complex ML research papers** | Just me | AI summaries can miss nuance; I need to build my own deep mental models. |
| **2. Defining the business problem and success metrics for a project** | Just me | Requires human context, stakeholder alignment, and strategic judgment. |
| **3. Writing initial boilerplate code for data pipelines** | Delegate to AI with review | AI is excellent at generating standard pandas/SQL boilerplate, but I must review for correctness. |
| **4. Debugging obscure Python/Pandas error messages** | Collaborate with AI | AI acts as a great sounding board to quickly brainstorm potential causes of the bug. |
| **5. Drafting regular weekly progress update emails** | Delegate to AI with review | I can provide bullet points and AI can format it into a professional email; requires final polish. |
| **6. Brainstorming edge cases for feature engineering** | Collaborate with AI | AI can suggest creative data combinations I might miss, which we refine together. |
| **7. Formatting and linting Python code (PEP8)** | Fully automate | Tools like Black/Ruff (often AI-assisted in IDEs) handle this perfectly without my intervention. |
| **8. Summarizing long meeting transcripts or call notes** | Delegate to AI with review | Saves hours of re-reading, though I need to verify action items are captured correctly. |
| **9. Designing the architecture of a new ML pipeline** | Collaborate with AI | I dictate the core requirements and constraints; AI helps propose structures and critique my design. |
| **10. Writing documentation and docstrings for functions** | Delegate to AI with review | AI writes accurate descriptions based on code logic, saving time, but I must ensure the "why" is clear. |
| **11. Exploring a new dataset (Initial EDA code)** | Collaborate with AI | AI writes the plotting/summary code, but I interpret the charts and decide what to query next. |
| **12. Managing my calendar and prioritizing my weekly to-do list** | Just me | Only I know my true energy levels and personal life constraints for the week. |

## Part 2: Three Target Tasks & Success Definitions

These three tasks will be reused in FL-02 through FL-04.

### Target Task 1: Writing Data Processing Scripts (ETL/Pandas)
**What "done well" means:** The script handles missing values and edge cases robustly, executes efficiently on large datasets without memory errors, follows PEP8 standards, and includes clear docstrings explaining the transformations.

### Target Task 2: Brainstorming and Defining ML Features
**What "done well" means:** The resulting feature list includes both standard aggregations and creative, domain-specific signals. The features must be strictly observable at prediction time (zero leakage) and clearly mapped to the business problem.

### Target Task 3: Drafting Technical Documentation / Reports
**What "done well" means:** The document is structured logically, communicates complex technical findings in plain language accessible to non-technical stakeholders, correctly highlights caveats/limitations, and requires zero grammatical editing.

---
*Note: Ensure to attach your Claude Project screenshot and Anthropic Academy enrollment evidence when submitting this document.*
