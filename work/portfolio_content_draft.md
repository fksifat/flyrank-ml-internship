# Portfolio Content Draft & Case Study
---

## 1. The Voice Card
**"Direct, plainspoken, evidence-backed, no buzzwords."**

---

## 2. Case Study 1: The Refresh Opportunity Scorer

**The Problem:**
A content team has thousands of pages and limited hours. When overall traffic starts slipping, they can't manually review 30,000 URLs to figure out which ones actually need an update. They need a way to filter out seasonal noise and surface the pages that are genuinely decaying and worth fixing.

**What I Did (and Decided):**
Instead of just guessing or using a rigid "update if older than 6 months" rule, I framed this as an ML ranking problem. 
*   First, I built a transparent baseline rule to have something honest to beat. 
*   Then, using 90 days of historical search and engagement signals (impressions, CTR, scroll rate), I trained a Random Forest model to predict actual content decline.
*   I actively avoided "target leakage" by strictly separating the feature window from the outcome, ensuring the model actually learned the pattern instead of memorizing the answer.

**What Came of It:**
The learned model beat the hand-written rule significantly. On the test set, it achieved a Precision@50 of 74% (compared to the baseline's 24%). I translated these probabilities into a ranked priority queue with clear "reason codes," meaning the editorial team now gets a daily list of exactly which 50 pages to fix first and why.

---

## 3. About Me (Bio)
I'm an aspiring Machine Learning Engineer focused on Applied Search Intelligence. I prefer solving messy, real-world data problems over chasing benchmark scores. I use Python, Pandas, and scikit-learn to build transparent pipelines that help humans make better, faster decisions. When I'm not auditing data for leakage, I'm [Insert Personal Hobby Here].

## 4. Contact / CTA Copy
**Ready to stop guessing with your data?**
Let’s talk about how we can build transparent, actionable ML pipelines for your team.
[ Email Me / Book a Quick Chat ]

---

## 5. The Before & After

**Before (Generic AI filler):**
"I leveraged cutting-edge machine learning algorithms and synergistic data-driven methodologies to optimize content strategies and maximize actionable ROI."

**After (My edited, plainspoken version):**
"I built a ranking model that finds declining pages so editors know exactly what to update first."
