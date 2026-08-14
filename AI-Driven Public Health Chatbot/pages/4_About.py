import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="About - AI Public Health Chatbot",
    page_icon="🩺",
    layout="wide"
)

# Header
st.markdown("""
<div style='text-align:center;padding:20px;'>
    <h1 style='color:#0EA5E9;'>🩺 About the Project</h1>
    <p style='font-size:20px;color:gray;'>
        AI-Driven Public Health Chatbot for Disease Awareness
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Project Overview
st.header("📌 Project Overview")

st.write("""
The **AI-Driven Public Health Chatbot for Disease Awareness** is designed to
provide users with reliable health information, disease awareness, symptom
guidance, and preventive healthcare recommendations.

The chatbot leverages Artificial Intelligence and Natural Language Processing (NLP)
to answer health-related queries in a user-friendly manner.
""")

# Objectives
st.header("🎯 Project Objectives")

col1, col2 = st.columns(2)

with col1:
    st.success("Increase disease awareness among the public")
    st.success("Provide symptom-based health guidance")
    st.success("Promote preventive healthcare practices")

with col2:
    st.success("Offer instant health information")
    st.success("Reduce misinformation about diseases")
    st.success("Support healthcare education")

# Features
st.header("✨ Key Features")

features = [
    "🤖 AI-Powered Health Chatbot",
    "🩺 Disease Awareness Information",
    "🔍 Symptom-Based Query Assistance",
    "📊 Health Statistics Dashboard",
    "📚 Preventive Healthcare Tips",
    "📱 Responsive and User-Friendly Interface"
]

for feature in features:
    st.markdown(f"- {feature}")

# Technologies Used
st.header("💻 Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.info("""
    **Frontend**
    
    • Streamlit
    
    • HTML/CSS Styling
    
    • Responsive Layout
    """)

with tech2:
    st.info("""
    **Backend**
    
    • Python
    
    • Machine Learning
    
    • NLP Processing
    """)

with tech3:
    st.info("""
    **Data Tools**
    
    • Pandas
    
    • NumPy
    
    • Scikit-Learn
    """)

# Benefits
st.header("🌍 Public Health Impact")

st.write("""
This project contributes to public health by:

- Educating users about common diseases.
- Encouraging preventive healthcare measures.
- Providing accessible health information.
- Supporting awareness campaigns.
- Promoting informed health decisions.
""")

# Team Section
st.header("👨‍💻 Project Team")

st.markdown("""
<div style="
background-color:#000000;
padding:20px;
border-radius:10px;
border-left:5px solid #0EA5E9;">
<h4>Developer Details</h4>

<b>Project:</b> AI-Driven Public Health Chatbot for Disease Awareness<br>

<b>Department:</b> Information Technology<br>

<b>Institution:</b> karpagam institute of technology<br>

<b>Academic Year:</b> 2024-2028
</div>
""", unsafe_allow_html=True)

# Future Enhancements
st.header("🚀 Future Enhancements")

future_features = [
    "Voice-based interaction",
    "Multi-language support",
    "Disease prediction using AI models",
    "Doctor recommendation system",
    "Real-time health alerts",
    "Mobile application integration"
]

for item in future_features:
    st.write(f"✔ {item}")

st.divider()

# Footer
st.markdown("""
<div style='text-align:center;padding:15px;'>
    <p style='color:gray;'>
        © 2026 AI-Driven Public Health Chatbot | Developed for Educational Purpose
    </p>
</div>
""", unsafe_allow_html=True)