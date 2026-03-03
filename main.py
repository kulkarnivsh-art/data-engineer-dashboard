import streamlit as st

import streamlit as st

# ✅ MUST be first Streamlit command
st.set_page_config(
    page_title="Data Engineer Pro Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ✅ Styling right after config
st.markdown("""
    <style>
        .main {
            background-color: #0E1117;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)


# 👇 Rest of your code starts here
st.title("🚀 Data Engineer Dashboard")

st.set_page_config(page_title="Data Engineer Dashboard", layout="wide")

# Sidebar
st.sidebar.title("🚀 Data Engineer Tracker")
page = st.sidebar.radio("Go to", [
    "Dashboard",
    "Learning Path",
    "Practice Tracker",
    "Projects",
    "Interview Prep",
    "Resume Tracker",
    "Leaderboard"
])

# Dummy data
progress = 65
streak = 7
score = 72

# Dashboard
if page == "Dashboard":


    col1, col2, col3 = st.columns(3)
    col1.metric("Completion %", f"{progress}%")
    col2.metric("Daily Streak", f"{streak} days")
    col3.metric("Job Readiness Score", score)

    st.progress(progress / 100)

    st.subheader("📅 Weekly Goal")
    st.write("Complete SQL Window Functions")

    st.subheader("⚠️ Pending Tasks")
    st.write("- Finish Airflow DAG")
    st.write("- Upload Project 2")

# Learning Path
elif page == "Learning Path":
    st.title("📘 Learning Modules")

    modules = ["SQL", "Python", "ETL", "Airflow", "Snowflake"]

    for module in modules:
        st.write(f"### {module}")
        st.progress(0.6)

# Practice Tracker
elif page == "Practice Tracker":
    st.title("🧪 Practice Tracker")

    sql_count = st.number_input("SQL Questions Solved", 0, 500)
    python_count = st.number_input("Python Problems Solved", 0, 500)

    st.write(f"Total Practice Score: {sql_count + python_count}")

# Projects
elif page == "Projects":
    st.title("🚀 Projects")

    project = st.text_input("Project Name")
    github = st.text_input("GitHub Link")

    if st.button("Add Project"):
        st.success("Project Added!")

# Interview Prep
elif page == "Interview Prep":
    st.title("💼 Interview Preparation")

    score = st.slider("Mock Interview Score", 0, 100)
    feedback = st.text_area("Feedback")

# Resume Tracker
elif page == "Resume Tracker":
    st.title("📄 Resume Tracker")

    uploaded = st.file_uploader("Upload Resume")
    ats_score = st.slider("ATS Score", 0, 100)

# Leaderboard
elif page == "Leaderboard":
    st.title("🏆 Leaderboard")

    st.table({
        "Name": ["Amit", "Rahul", "Priya"],
        "Score": [85, 78, 72]
    })