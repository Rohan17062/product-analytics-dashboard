🚀 Product Analytics Dashboard – Music Streaming App

⚡ Quick Summary

1. End-to-end product analytics project analyzing user journey in a music streaming app
2. Identified key drop-offs in funnel, low Day-1 retention, and weak long-term engagement
3. Performed funnel, retention, and cohort analysis using SQL and Python
4. Found major monetization issue at playlist → premium stage (~21% drop-off)
5. Estimated business impact: improving conversion from ~79% to 85% can increase subscribers by ~200+ users
6. Provided data-driven recommendations to improve onboarding, engagement, and revenue

🌐 Live Dashboard
[https://appuct-analytics-dashboard-tsv95gnxxmjenh4ydjeo4f.streamlit.app/](url)

📌 Project Overview

1. This project presents an end-to-end Product Analytics case study on a music streaming application
2. Focuses on analyzing user behavior across the product lifecycle
3. Demonstrates how data can be used to improve engagement, retention, and monetization
4. Simulates real-world product decision-making using analytics

🎯 Business Problem

-> The platform aims to increase user engagement and premium subscriptions
-> Lack of clarity on where users drop in the product journey
-> Unclear retention patterns across time
-> No visibility into whether product improvements are actually working
-> These gaps limit the ability to improve user experience and revenue

🎯 Objective

1. Identify key drop-off points in the user journey
2. Measure user retention and engagement over time
3. Evaluate behavior across different user cohorts
4. Provide actionable recommendations to improve product performance

🛠️ Tools & Technologies Used

1. SQL – Data analysis (joins, aggregations, window functions)
2. Python (Pandas, NumPy) – Data processing
3. Matplotlib / Seaborn – Visualization
4. Streamlit – Interactive dashboard
5. Google Colab – Development environment

📊 Data Overview

Simulated dataset representing a music streaming platform
Captures user behavior across multiple sessions

Includes:

Users data → user_id, device (Android/iOS)
Events data → user actions (app_open, search_song, play_song, like_song, add_to_playlist, etc.)
Subscription data → premium conversion

Key Characteristics:
1. Structured funnel flow
2. Tracks complete user lifecycle
3. Designed for product analytics use cases

📈 Analysis Performed

1. Funnel Analysis
Tracked user journey across stages:
app_open → search_song → play_song → like_song → add_to_playlist → subscribe_premium
Calculated stage-wise user counts
Computed conversion rates using SQL window functions
Identified drop-off percentages

2. Drop-off Analysis
Identified stages with maximum user loss
Quantified inefficiencies in conversion flow

3. Segmentation Analysis (Device-wise)
Compared Android vs iOS user behavior
Evaluated whether drop-offs are product-related or platform-specific

4. Retention Analysis
Calculated days since first user activity
Built retention curve
Measured Day-1 and long-term retention trends

5. Cohort Analysis
Grouped users by first activity date
Built cohort retention matrix
Compared retention patterns across cohorts
Evaluated product performance over time

🔍 Key Insights

1. Funnel Insights
Largest drop-off (~21%) occurs at playlist → premium stage
Significant drop (~17%) between like → playlist stage
Early funnel stages show high engagement (>95%)

2. Segmentation Insights
Similar behavior across Android and iOS users
Indicates product-level issues rather than platform-specific problems

3. Retention Insights
Low Day-1 retention (~10–20%) indicates onboarding issues
Sharp drop after first use (~85%) shows early churn
Retention stabilizes at ~14–16%, indicating a small core user base
Gradual decline reflects long-term churn

4. Cohort Insights
Retention patterns are consistent across cohorts
No improvement in newer cohorts
Indicates product changes are not improving engagement

📊 Final Business Conclusions

1. Strong initial engagement but weak early retention
2. Major issue at monetization stage (playlist → subscription)
3. Small group of loyal users exists, but overall engagement is low
4. Product performance is not improving over time

🚀 Product Recommendations

1. Improve Early Retention
Introduce personalized onboarding
Provide instant value through curated playlists
Use Day-1 engagement strategies

2. Increase Engagement
Recommend playlists after “like” actions
Introduce auto-generated playlists
Add gamification features

3. Improve Premium Conversion
Offer free trials or previews
Highlight premium benefits during high engagement
Introduce limited-time offers

4. Strengthen Long-Term Retention
Implement re-engagement campaigns
Continuously update content
Provide loyalty incentives

📌 Priority Actions
-> Improve onboarding experience (High Priority)
-> Optimize playlist → subscription stage (Revenue Impact)
-> Enhance engagement through personalization

🧪 Suggested Experiments
1. A/B test free trial at playlist stage
2. Test personalized onboarding vs generic onboarding
3. Experiment with Day-1 push notifications
4. Test auto-playlist recommendations

📈 Impact Analysis

Current conversion rate from playlist to premium is ~79.15%
Improving conversion to 85% increases subscribers from 2938 to ~3155
Results in ~200+ additional users
Demonstrates strong revenue impact from small improvements

⚠ Limitations

-> Dataset is simulated and follows a structured funnel
-> Real-world behavior may be more complex and noisy
=> External factors (pricing, competition, content quality) not considered

📊 Streamlit Dashboard

1. Visualizes funnel conversion
2. Shows drop-offs
3. Displays retention trends
4. Includes cohort heatmap
5. Highlights business insights

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

1. Demonstrates end-to-end product analytics workflow
2. Combines SQL, Python, and business thinking
3. Focuses on actionable insights
4. Shows ability to drive product decisions using data

📌 Conclusion

Identified key product bottlenecks
Highlighted engagement and retention issues
Provided data-driven strategies for improvement
Demonstrates strong product analytics and decision-making skills





