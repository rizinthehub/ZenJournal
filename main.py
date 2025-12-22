import streamlit as st
import pandas as pd
from backend import MoodAI # Importing our own module

# 1. UI Configuration (Must be the first command)
st.set_page_config(page_title="ZenJournal", page_icon="🧠", layout="centered")

# 2. CSS Styling (To show off UI Skills)
st.markdown("""
    <style>
    .stTextArea textarea {
        background-color: #f0f2f6;
        color: #31333F;
    }
    .main-title {
        font-size: 3em;
        font-weight: bold;
        color: #4B4B4B;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize our Backend Class
app_logic = MoodAI()

# 3. The App Layout
st.markdown('<div class="main-title">🧠 ZenJournal</div>', unsafe_allow_html=True)
st.write("Write your daily thoughts below. Our AI will analyze your mood.")

# Input Area
with st.form("journal_form"):
    user_text = st.text_area("How are you feeling right now?", height=150)
    submit_btn = st.form_submit_button("Analyze & Save Entry")

# Logic Implementation
if submit_btn and user_text:
    score, label = app_logic.analyze_entry(user_text)
    app_logic.save_entry(user_text, score, label)
    
    st.success("Entry Saved Successfully!")
    
    # Display the Result
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Mood Score", value=f"{score:.2f}")
    with col2:
        st.info(f"Detected Mood: {label}")

# 4. Data Visualization Section
st.divider()
st.subheader("📊 Your Mood Trends")

try:
    data = app_logic.load_data()
    
    # Only show graph if we have data
    if not data.empty:
        # Convert Date column to datetime objects for better graphing
        data['Date'] = pd.to_datetime(data['Date'])
        
        # Line Chart
        st.line_chart(data, x='Date', y='Mood_Score')
        
        # Recent Entries Table
        with st.expander("View Past Entries"):
            st.dataframe(data.sort_values(by='Date', ascending=False))
            
except Exception as e:
    st.write("No data available yet. Write your first entry!")