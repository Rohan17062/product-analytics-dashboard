# 🎧 Product Analytics Dashboard – Music Streaming App

## 🌐 Live Dashboard
[Click here to view streamlit dashboard](https://appuct-analytics-dashboard-tsv95gnxxmjenh4ydjeo4f.streamlit.app/)


## 📌 Project Overview
This project presents an end-to-end **Product Analytics case study** on a music streaming application.  

The objective was to analyze user behavior across the product lifecycle and answer key business questions:
- Where are users dropping in the funnel?
- How well are users retained over time?
- Are there behavioral differences across user segments?
- How can we improve engagement and premium conversion?

The project covers the complete analytics workflow — from raw event data to actionable product insights and an 
interactive dashboard.

---

## 🛠️ Tools & Technologies used
- **SQL** – Data analysis (joins, aggregations, window functions)
- **Python (Pandas, NumPy)** – Data processing and analysis
- **Matplotlib / Seaborn** – Visualization
- **Streamlit** – Interactive dashboard
- **Google Colab** – Development environment
  
---

## 📊 Dataset Description
The dataset simulates user activity in a music streaming platform and includes:
- **Users data** – user_id, device (Android/iOS)
- **Events data** – user actions (app_open, search_song, play_song, etc.)
- **Subscription data** – premium conversion details

---

## 📈 Analysis Performed

###🔻1. Funnel Analysis
Tracked user journey across key stages:
app_open → search_song → play_song → like_song → add_to_playlist → subscribe_premium

- Calculated stage-wise user counts.
- Computed **conversion rates** using window functions.
- Identified **drop-off percentages**.

---

### 📉 2. Drop-off Analysis
- Determined the stage with maximum user loss.
- Quantified conversion inefficiencies across funnel steps.

---

### 📱 3. Segmentation Analysis (Device-wise)
- Compared funnel behavior for **Android vs iOS users**.
- Evaluated whether drop-offs were device-specific or product-wide.

---

### 📈 4. Retention Analysis
- Calculated **days since first activity**.
- Built **retention curve**.
- Measured Day-1 and long-term retention trends.

---

### 📊 5. Cohort Analysis
- Grouped users by **signup date (cohort)**.
- Built **cohort retention table**.
- Visualized retention using a **heatmap**.
- Analyzed behavioral patterns across cohorts.

---

## 🔍 Key Insights

### 🔻 Funnel Insights
- The **largest drop-off (~21%)** occurs at the transition from *playlist creation to premium subscription*.
- Significant drop (~17%) observed between *like → playlist stage*.
- Early funnel stages show high engagement (>95%).

---

### 📱 Segmentation Insights
- Funnel behavior is **consistent across Android and iOS**.
- Drop-offs are **product-related**, not platform-specific.

---

### 📉 Retention Insights
- **Day-1 retention is low (~10–20%)**, indicating weak onboarding.
- Retention drops sharply after first use (~85% drop).
- Retention stabilizes at ~14–16%, indicating a **small core user base**.
- User behavior is **inconsistent**, suggesting lack of habit formation.
- Occasional spikes indicate **external triggers (notifications/content)**.

---

### 📊 Cohort Insights
- No significant improvement in retention across cohorts.
- Retention patterns remain relatively stable over time.
- Long-term engagement remains weak across all cohorts.

---

## 🚀 Product Recommendations

### 🎯 Improve Early Retention
- Introduce **personalized onboarding experience**.
- Provide **instant value (curated playlists)** during first session.
- Send **Day-1 push notifications**.

---

### 🎯 Increase Engagement
- Add **playlist suggestions after liking songs**.
- Provide **auto-generated playlists**.
- Introduce **gamification (badges, rewards)**.

---

### 🎯 Improve Premium Conversion
- Offer **free trials / premium previews**.
- Highlight premium benefits during high-engagement moments.
- Provide **time-limited discounts**.

---

### 🎯 Strengthen Long-Term Retention
- Implement **re-engagement notifications (Day 3, Day 7)**.
- Continuously update content and recommendations.
- Introduce **loyalty rewards for active users**.

---

## 📊 Streamlit Dashboard

An interactive dashboard was built using Streamlit to visualize:
- Funnel analysis & conversion rates
- Drop-off identification
- Retention curve
- Cohort heatmap
- Business insights & recommendations

---

## 📂 Project Structure

product-analytics-dashboard/
│
├──> app.py # Streamlit dashboard
├──> data/
│ ├──> users.csv
│ ├──> events.csv
│ └──> subscriptions.csv
├──> music_app_funnel_retention_cohort_project.ipynb # Analysis notebook
└──> README.md

---

## 🎯 Key Takeaways
- Demonstrates **end-to-end product analytics workflow**.
- Combines **SQL + Python + Business thinking**.
- Focuses on **actionable insights**, not just data analysis.
- Simulates real-world **product decision-making**.

---

## 🔗 Future Improvements
- Add real-time data integration.
- Enhance dashboard UI/UX.
- Include additional segmentation (location, user behavior).
- Deploy dashboard publicly for live access.

---

## 📌 Conclusion
This project highlights how data-driven analysis can be used to:
- Identify product bottlenecks.
- Improve user engagement.
- Optimize conversion strategies/

It reflects a strong foundation in **Product Analytics, Data Analysis, and Business Insight generation**.
