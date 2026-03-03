import streamlit as st
import pandas as pd

st.set_page_config(page_title="Interactive Resume", page_icon="📄", layout="wide")

# ====== EDIT THESE WITH YOUR REAL INFO ======
NAME = "Cindy Xu"
TITLE = "Finance + Analytics | Risk | Treasury"
EMAIL = "cindy.lx.xu@gmail.com"
LINKEDIN = "www.linkedin.com/in/cindy-lx-xu"
SUMMARY = """
I build practical analytics for finance (risk, treasury, and data-driven projects).
I enjoy turning messy data into clear decisions with dashboards, models, and automation.
"""

education_df = pd.DataFrame([
    {"School": "University of Toronto (Rotman)", "Program": "Master of Management Analytics", "Years": "2025–2026"},
    {"School": "University of Waterloo / WLU", "Program": "Math & Business Double Degree", "Years": "2020–2025"},
])

experience_df = pd.DataFrame([
    {"Type": "Risk", "Company": "CIBC", "Role": "Market Risk Analyst", "Year": 2023,
     "Impact": "Built stress/VaR reporting and improved monitoring workflows."},
    {"Type": "Treasury", "Company": "Brookfield", "Role": "Treasury Analyst", "Year": 2024,
     "Impact": "Supported liquidity operations and cash forecasting processes."},
    {"Type": "Analytics", "Company": "Nasdaq", "Role": "Analytics Intern", "Year": 2025,
     "Impact": "Built transcript/sentiment dashboards and automated pipelines."},
])

skills_df = pd.DataFrame([
    {"Category": "Technical", "Skill": "Python", "Proficiency": 85},
    {"Category": "Technical", "Skill": "Excel / Modeling", "Proficiency": 90},
    {"Category": "Finance", "Skill": "Risk Analytics", "Proficiency": 82},
    {"Category": "Finance", "Skill": "Treasury & Liquidity", "Proficiency": 78},
    {"Category": "Soft", "Skill": "Communication", "Proficiency": 84},
    {"Category": "Soft", "Skill": "Presentation", "Proficiency": 88},
])
# ===========================================

st.title(f"{NAME} — Interactive Resume")
st.caption(TITLE)
st.write(f"📧 {EMAIL} | 🔗 [LinkedIn]({LINKEDIN})")
st.markdown(SUMMARY)
st.divider()

# ---- Sidebar widgets (3+ required) ----
with st.sidebar:
    st.header("Customize View")
    focus = st.selectbox("Focus area", ["All", "Risk", "Treasury", "Analytics"])          # widget 1
    min_year = st.slider("Show experience from year ≥", 2020, 2026, 2023)                # widget 2
    categories = st.multiselect(                                                         # widget 3
        "Skill categories", 
        options=sorted(skills_df["Category"].unique()),
        default=sorted(skills_df["Category"].unique())
    )
    show_impacts = st.checkbox("Show impact bullets", value=True)                        # widget 4 (extra)

# ---- Layout ----
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Education (Table)")
    st.dataframe(education_df, use_container_width=True)

    st.subheader("Experience (Table)")
    exp = experience_df.copy()
    if focus != "All":
        exp = exp[exp["Type"] == focus]
    exp = exp[exp["Year"] >= min_year]
    st.dataframe(exp[["Company", "Role", "Year", "Type"]], use_container_width=True)

    if show_impacts:
        st.markdown("**Highlights**")
        for _, r in exp.iterrows():
            st.write(f"- **{r['Company']} — {r['Role']} ({r['Year']})**: {r['Impact']}")

with col2:
    st.subheader("Skills (Table)")
    s = skills_df[skills_df["Category"].isin(categories)].sort_values("Proficiency", ascending=False)
    st.dataframe(s, use_container_width=True)

    st.subheader("Skills Proficiency (Chart)")
    chart_data = s.set_index("Skill")[["Proficiency"]]
    st.bar_chart(chart_data, horizontal=True)

st.divider()
st.info("Use the sidebar filters to update the resume content and chart.")
