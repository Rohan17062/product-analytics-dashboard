🚀 Product Analytics Dashboard – Music Streaming App

🌐 Live Dashboard
Click here to view Streamlit dashboard

📌 Project Overview

This project presents an end-to-end Product Analytics case study on a music streaming application.

The goal is to analyze user behavior across the product lifecycle and identify opportunities to improve engagement, retention, and premium conversion using data-driven insights.

🎯 Business Problem

The music streaming platform aims to improve user engagement and premium subscription growth but lacks clear visibility into:

Where users drop off in the product journey
How user retention changes over time
Whether product improvements are actually increasing engagement

Without this understanding, it becomes difficult to optimize user experience and drive revenue growth.

🎯 Objective

To analyze user behavior across the product lifecycle using funnel, retention, and cohort analysis in order to:

Identify key drop-off points in the user journey
Measure user retention and engagement over time
Evaluate whether user behavior is improving across cohorts
Recommend data-driven strategies to improve engagement and conversion
🛠️ Tools & Technologies Used
SQL – Data analysis (joins, aggregations, window functions)
Python (Pandas, NumPy) – Data processing
Matplotlib / Seaborn – Visualization
Streamlit – Interactive dashboard
Google Colab – Development
📊 Data Overview

The dataset simulates user interactions in a music streaming platform, capturing behavior across multiple sessions and stages of the product lifecycle.

It includes:

Users data – user_id, device (Android/iOS)
Events data – user actions (app_open, search_song, play_song, like_song, add_to_playlist, etc.)
Subscription data – premium conversion outcomes

The data is structured to represent a typical product funnel and user engagement lifecycle.

📈 Analysis Performed
🔻 1. Funnel Analysis

Tracked user journey across key stages:
app_open → search_song → play_song → like_song → add_to_playlist → subscribe_premium

Calculated stage-wise user counts
Computed conversion rates using SQL window functions
Identified drop-off percentages
📉 2. Drop-off Analysis
Identified stages with highest user loss
Quantified inefficiencies in conversion flow
📱 3. Segmentation Analysis (Device-wise)
Compared Android vs iOS behavior
Verified whether issues are platform-specific or product-wide
📈 4. Retention Analysis
Calculated days since first user activity
Built retention curve
Measured Day-1 and long-term engagement
📊 5. Cohort Analysis
Grouped users by first activity date
Built cohort retention matrix
Analyzed behavior across cohorts over time
🔍 Key Insights
🔻 Funnel Insights
Largest drop-off (~21%) occurs at playlist → premium stage, directly impacting monetization
Significant drop (~17%) between like → playlist stage indicates friction in engagement
Early funnel stages show high engagement (>95%), suggesting strong initial interest
📱 Segmentation Insights
Similar behavior across Android and iOS users indicates product-level issues rather than platform-specific problems
📉 Retention Insights
Low Day-1 retention (~10–20%) indicates users are not experiencing sufficient value during first interaction
Retention drops sharply after initial use (~85%), highlighting early churn
Retention stabilizes at ~14–16%, indicating a small core group of engaged users
Gradual decline over time reflects long-term user churn
📊 Cohort Insights
Retention patterns are consistent across cohorts, indicating no improvement in user engagement over time
Lack of improvement suggests product changes are not effectively increasing retention
Long-term engagement remains weak across all user groups
📊 Final Business Conclusions
The product shows strong initial engagement but struggles with early retention
The most critical issue lies in the monetization stage (playlist → subscription)
A small core user base exists, but overall engagement is weak
Product performance is not improving over time across cohorts
🚀 Product Recommendations
🎯 Improve Early Retention
Introduce personalized onboarding
Provide instant value through curated playlists
Use Day-1 engagement strategies (notifications)
🎯 Increase Engagement
Recommend playlists after “like” actions
Introduce auto-generated playlists
Add gamification elements
🎯 Improve Premium Conversion
Offer free trials or previews
Highlight premium benefits during high engagement
Introduce limited-time offers
🎯 Strengthen Long-Term Retention
Implement re-engagement campaigns
Continuously update content
Provide loyalty incentives
📌 Priority Actions
Improve onboarding experience (High Priority)
Optimize playlist → subscription stage (Revenue Impact)
Enhance engagement through personalization
🧪 Suggested Experiments
A/B test free trial at playlist stage
Test personalized onboarding vs generic onboarding
Experiment with Day-1 push notifications
Test auto-playlist recommendations
📈 Impact Analysis
🔹 SQL Query

(Add your SQL query here)

🔹 Key Result
Current conversion rate from playlist to premium is ~79.15%
If improved to 85%, premium subscribers increase from 2938 to ~3155
This results in an increase of ~200+ users, showing how small improvements can significantly impact revenue
⚠ Limitations
Dataset is simulated and follows a structured funnel
Real-world user behavior may be more complex and noisy
Does not include external factors like pricing, competition, or content quality
📊 Streamlit Dashboard

The dashboard visualizes:

Funnel conversion rates
Drop-off analysis
Retention trends
Cohort heatmap
Business insights
📂 Project Structure
product-analytics-dashboard/
│
├── app.py
├── data/
│   ├── users.csv
│   ├── events.csv
│   └── subscriptions.csv
├── music_app_funnel_retention_cohort_project.ipynb
└── README.md
🎯 Key Takeaways
Demonstrates end-to-end product analytics workflow
Combines SQL, Python, and business thinking
Focuses on actionable insights and decision-making
Shows ability to translate data into product improvements
📌 Conclusion

This project demonstrates how data can be used to:

Identify product bottlenecks
Improve user engagement
Optimize conversion and revenue

It reflects strong capabilities in Product Analytics, Data Analysis, and Business Decision-Making.






