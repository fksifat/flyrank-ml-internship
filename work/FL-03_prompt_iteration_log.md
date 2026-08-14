# Prompt Iteration Log: ML Feature Engineering

**Target Task (from FL-01):** Brainstorming and Defining ML Features
**Goal:** Generate a robust, leakage-free list of features to predict content decay for the Refresh Scoring pipeline.

---

## The Iteration Log

### Baseline (The Naive Prompt)
**Prompt:** Give me some machine learning features for predicting page traffic drops.
**Output (Excerpt):** 
> *Here are some features you can use: 1. Traffic drops in the last 30 days. 2. Bounce rate. 3. Number of backlinks. 4. Keyword density...*
**Notes:**
*   **What changed:** N/A (Baseline).
*   **What improved:** N/A.
*   **What still failed:** The features are generic SEO metrics. Some (like "traffic drops in the last 30 days") are blatant target leakage because they overlap with the outcome we are trying to predict.
*   **Next step:** Apply **Role Assignment**.

### Version 1: Role Assignment
**Prompt:** Act as an expert Machine Learning Engineer specializing in Applied Search Intelligence. Give me some machine learning features for predicting page traffic drops.
**Output (Excerpt):** 
> *As an MLE in search intelligence, I recommend looking at time-series decay, click-through rate differentials, and query cannibalization...*
**Notes:**
*   **What changed:** Added Role Assignment ("expert Machine Learning Engineer specializing in Applied Search Intelligence").
*   **What actually improved:** The vocabulary and complexity immediately upgraded. It stopped suggesting basic SEO metrics like "keyword density" and started suggesting data science concepts like "time-series decay."
*   **What still failed:** It's too abstract. It doesn't know what data I actually have available in my dataset, so its suggestions aren't actionable.
*   **Next step:** Apply **Context and Motivation**.

### Version 2: Context and Motivation
**Prompt:** Act as an expert Machine Learning Engineer specializing in Applied Search Intelligence. Context: We are predicting which of our 30k web pages will decline in traffic next month to prioritize our content refresh queue. Our data comes from Google Search Console and GA4 (impressions, clicks, sessions, position, age). Give me some machine learning features for this.
**Output (Excerpt):** 
> *Given your GSC and GA4 data, here are features you can engineer: 
> 1. Delta Impressions (Last 30d vs Prev 30d) 
> 2. Position Volatility 
> 3. CTR Gap to Position Expected CTR...*
**Notes:**
*   **What changed:** Added Context and Motivation (the specific data sources available and the business goal).
*   **What actually improved:** The suggestions are now physically possible to build with my actual dataset. "CTR Gap to Position" is a highly actionable feature.
*   **What still failed:** The output is just a raw list. It's hard to read and doesn't explicitly warn me about data leakage risks.
*   **Next step:** Apply **Output Structure**.

### Version 3: Output Structure
**Prompt:** Act as an expert Machine Learning Engineer specializing in Applied Search Intelligence. Context: We are predicting which of our 30k web pages will decline in traffic next month to prioritize our content refresh queue. Our data comes from Google Search Console and GA4 (impressions, clicks, sessions, position, age). 
Output format: A Markdown table with columns: [Feature Name] | [Formula/Definition] | [Why it matters] | [Leakage Risk Level].
**Output (Excerpt):** 
> *| Feature Name | Formula/Definition | Why it matters | Leakage Risk Level |*
> *| :--- | :--- | :--- | :--- |*
> *| CTR_Gap | `actual_ctr - avg_ctr_for_position` | Identifies pages underperforming their rank | Low |*
**Notes:**
*   **What changed:** Dictated a specific Output Structure (Markdown table with defined columns).
*   **What actually improved:** The readability skyrocketed. Forcing the "Leakage Risk Level" column made the AI explicitly evaluate its own suggestions for target leakage.
*   **What still failed:** While the features are good, they are all basic metrics. It hasn't generated any complex interaction features (like combining age and position).
*   **Next step:** Apply **Few-Shot Examples**.

### Version 4: Few-Shot Examples
**Prompt:** Act as an expert Machine Learning Engineer specializing in Applied Search Intelligence. Context: We are predicting which of our 30k web pages will decline in traffic next month to prioritize our content refresh queue. Our data comes from Google Search Console and GA4.
Example 1: "Stale_Winner_Flag" = (age_days > 365) AND (avg_position < 10).
Example 2: "Engagement_Deficit" = (impressions_90d > 1000) AND (scroll_rate < 0.20).
Output format: A Markdown table with columns: [Feature Name] | [Formula/Definition] | [Why it matters] | [Leakage Risk Level].
Provide 5 new advanced interaction features.
**Output (Excerpt):** 
> *| Slipping_Giant_Flag | (impressions_90d > 5000) AND (position_trend = negative) | Flags high-volume pages slowly losing ground | Low |*
**Notes:**
*   **What changed:** Provided Few-Shot Examples showing how to combine simple metrics into boolean flags or interaction features.
*   **What actually improved:** The model mirrored my logic. Instead of just giving me `age` or `position`, it generated highly specific, business-logic-driven interaction features.
*   **What still failed (Honest negative):** It just jumped straight into the table without explaining its underlying strategy.
*   **Next step:** Apply **Step Decomposition**.

### Version 5: Step Decomposition (The Final Prompt)
**Prompt:** Act as an expert Machine Learning Engineer specializing in Applied Search Intelligence. Context: We are predicting which of our 30k web pages will decline in traffic next month to prioritize our content refresh queue. Our data comes from GSC and GA4.
Example 1: "Stale_Winner_Flag" = (age_days > 365) AND (avg_position < 10).
Example 2: "Engagement_Deficit" = (impressions_90d > 1000) AND (scroll_rate < 0.20).
Perform this task in exactly two steps:
Step 1: Write a one-paragraph strategy on the types of decay signals we should look for.
Step 2: Provide a Markdown table with 5 advanced interaction features. Columns: [Feature Name] | [Formula] | [Why it matters] | [Leakage Risk Level].
**Output (Excerpt):** 
> *Step 1: Strategy... To predict decay before it happens, we must look for divergence between exposure and engagement. A page that maintains rank but drops in CTR is likely suffering from intent drift or SERP feature changes...*
> *Step 2: Table...*
**Notes:**
*   **What changed:** Forced Step Decomposition (Step 1: Strategy, Step 2: Table).
*   **What actually improved:** Separating the "thinking" from the "formatting" resulted in a much smarter table. The AI grounded its feature suggestions in the strategy it established in Step 1.

---

## Cross-Model Comparison

I ran the final Version 5 prompt through both **Claude 3.5 Sonnet** and **ChatGPT (GPT-4o)**.

*   **Tone & Structure:** Claude followed the step decomposition perfectly and maintained a very analytical, professional tone. ChatGPT included a lot of enthusiastic filler ("Great project! Let's dive in!") which cluttered the output.
*   **Accuracy / Leakage:** Claude correctly identified that using *any* data from the "next month" target window in the feature formulas would be fatal leakage, marking all its features as "Low Risk." ChatGPT accidentally included a feature using a 30-day moving average that edged dangerously close to the prediction window, marking it "Medium Risk" but still suggesting it.
*   **Conclusion:** For strict formatting and safe, analytical data science tasks, Claude's adherence to the steps and constraints was superior. ChatGPT was slightly more creative with the feature naming, but the risk of leakage makes it less reliable for this specific task.

---

## The Final Reusable Template

*(Anyone can use this for brainstorming ML features on any dataset)*

**Role:** Act as a Senior [DOMAIN] Machine Learning Engineer.
**Context:** We are trying to predict [TARGET VARIABLE] in order to [BUSINESS GOAL / ACTION]. Our available data sources include [DATA SOURCES / COLUMNS].
**Examples of what good looks like:**
- Example 1: [FEATURE NAME] = [FORMULA / LOGIC]
- Example 2: [FEATURE NAME] = [FORMULA / LOGIC]
**Instructions:**
Perform this task in exactly two steps:
**Step 1:** Write a short strategy paragraph identifying the key hidden signals or interactions that would predict this target without causing target leakage.
**Step 2:** Provide a Markdown table of 5 advanced interaction features based on your strategy. Columns must be: [Feature Name] | [Formula] | [Business Rationale] | [Leakage Risk Level].
