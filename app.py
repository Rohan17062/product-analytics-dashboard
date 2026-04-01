import streamlit as st
import pandas as pd

st.title("🎧 Music App Dashboard")

# load data
users = pd.read_csv("users (1).csv")
subs = pd.read_csv("subscriptions.csv")

# calculations
total_users = users['user_id'].nunique()
premium_users = subs['user_id'].nunique()
conversion = (premium_users / total_users) * 100

# display metrics
st.subheader("📊 Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Users", total_users)
col2.metric("Premium Users", premium_users)
col3.metric("Conversion %", round(conversion, 2))


# load events
events = pd.read_csv("events.csv")

st.subheader("🔻Funnel Stage Counts")

 # define order
funnel_order = [
    "app_open",
    "search_song",
    "play_song",
    "like_song",
    "add_to_playlist",
    "subscribe_premium"
]

# calculate counts
funnel_df = (
    events.groupby("event_type")["user_id"]
    .nunique()
    .reindex(funnel_order)
    .reset_index()
)

funnel_df.columns = ["Stage", "Users"]

# display
st.dataframe(funnel_df)

import matplotlib.pyplot as plt

st.subheader("📊 Funnel Visualization")

fig, ax = plt.subplots()

ax.bar(funnel_df["Stage"], funnel_df["Users"])

ax.set_xlabel("Funnel Stage")
ax.set_ylabel("Users")
ax.set_title("User Funnel")

plt.xticks(rotation=45)

st.pyplot(fig)

# calculate conversion %
funnel_df["Conversion %"] = (
    funnel_df["Users"] / funnel_df["Users"].shift(1) * 100
 )

# round it
funnel_df["Conversion %"] = funnel_df["Conversion %"].round(2)


# drop-off %
funnel_df["Drop-off %"] = 100 - funnel_df["Conversion %"]

# clean first row
funnel_df["Drop-off %"] = funnel_df["Drop-off %"].fillna(0)

# remove first row
temp_df = funnel_df.iloc[1:]

max_drop = temp_df.loc[temp_df["Drop-off %"].idxmax()]
st.dataframe(funnel_df)

st.subheader("🚨 Key Insight")

st.write(
    f"Biggest drop-off occurs at **{max_drop['Stage']}** stage "
    f"with a drop of **{round(max_drop['Drop-off %'], 2)}%**"
)

st.subheader("📈 Retention Curve")

# prepare retention data
retention_df = (
    events.groupby("user_id")["event_time"]
    .apply(lambda x: pd.to_datetime(x).dt.date)
    .reset_index()
)

events["event_time"] = pd.to_datetime(events["event_time"])

# first activity
first_activity = events.groupby("user_id")["event_time"].min().reset_index()
first_activity.columns = ["user_id", "first_date"]

# merge back
retention = events.merge(first_activity, on="user_id")

# days since
retention["days_since"] = (
    (retention["event_time"] - retention["first_date"]).dt.days
)

retention_counts = (
    retention.groupby("days_since")["user_id"]
    .nunique()
    .reset_index()
)

total_users = retention_counts.loc[
    retention_counts["days_since"] == 0, "user_id"
].values[0]

retention_counts["retention_%"] = (
    retention_counts["user_id"] / total_users * 100
)


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot(
    retention_counts["days_since"],
    retention_counts["retention_%"]
)

ax.set_xlabel("Days Since Signup")
ax.set_ylabel("Retention %")
ax.set_title("Retention Curve")

st.pyplot(fig)

st.subheader("🧠 Retention Insights")

st.markdown("""
- **Sharp drop after Day 0 (~85%)**  
  → Indicates poor early user engagement or onboarding issues  

- **Stable retention (~14–16%) from Day 1 to Day 40**  
  → Suggests presence of a consistent core user base  

- **Gradual decline after Day 45**  
  → Indicates long-term churn among retained users  
""")


st.subheader("📊 Cohort Retention Heatmap")

# prepare data
events["event_time"] = pd.to_datetime(events["event_time"])

# first date
first_date = events.groupby("user_id")["event_time"].min().reset_index()
first_date.columns = ["user_id", "first_date"]

# merge
cohort = events.merge(first_date, on="user_id")

# days since
cohort["days_since"] = (cohort["event_time"] - cohort["first_date"]).dt.days

# cohort_date
cohort["cohort_date"] = cohort["first_date"].dt.date


cohort_counts = (
    cohort.groupby(["cohort_date", "days_since"])["user_id"]
    .nunique()
    .reset_index()
)


cohort_size = cohort_counts[cohort_counts["days_since"] == 0][
    ["cohort_date", "user_id"]
].rename(columns={"user_id": "cohort_size"})


cohort_final = cohort_counts.merge(cohort_size, on="cohort_date")

cohort_final["retention_%"] = (
    cohort_final["user_id"] / cohort_final["cohort_size"] * 100
)

cohort_pivot = cohort_final.pivot(
    index="cohort_date",
    columns="days_since",
    values="retention_%"
)

cohort_pivot = cohort_pivot.iloc[:10, :15]  # keep it readable


import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))

sns.heatmap(
    cohort_pivot,
    cmap="coolwarm",
    vmin=0,
    vmax=100,
    linewidths=0.5,
    ax=ax
)

ax.set_title("Cohort Retention Heatmap")

st.pyplot(fig)

st.subheader("🧠 Cohort Insights")

st.markdown("""
- **Low Day-1 retention (~10–20%)**  
  → Indicates weak onboarding or poor initial user experience  

- **Highly fluctuating retention across days**  
  → Suggests users are not forming consistent usage habits  

- **Occasional spikes in retention**  
  → Likely driven by external triggers such as notifications or new content  

- **Retention stabilizes at a low level (~10–20%)**  
  → Indicates a small but consistent core user base with limited long-term growth  
""")

st.warning("⚠️ Low Day-1 retention is the biggest concern — users are not returning after first experience.")

st.subheader("🚀 Product Recommendations")

st.markdown("""
### 🎯 Improving Early Retention
- Introduce **personalized onboarding** to guide new users during first session  
- Send **Day-1 push notifications** with song recommendations  
- Provide **instant value (e.g., curated playlists)** immediately after signup  

### 🎯 Increasing Engagement (Like → Playlist Drop)
- Encourage playlist creation using **“Add to playlist” prompts after liking songs**  
- Provide **auto-generated playlists** based on liked songs  
- Introduce **gamification (e.g., badges for playlist creation)**  

### 🎯 Improving Premium Conversion
- Offer **free trial or limited premium preview**  
- Highlight premium benefits during high-engagement moments  
- Provide **discounts or time-limited offers**  

### 🎯 Strengthening Long-term Retention
- Send **re-engagement notifications (Day 3, Day 7)**  
- Continuously update content and recommendations  
- Introduce **loyalty rewards for frequent users**
""")





