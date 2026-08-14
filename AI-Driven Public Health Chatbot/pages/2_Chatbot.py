import streamlit as st
import pandas as pd

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Public Health Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ==========================
# CUSTOM CSS
# ==========================

st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #312e81
    );
}

/* Text */
h1,h2,h3,h4,h5,h6,p,label,span{
    color:white !important;
}

/* Hero Card */
.hero{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    padding:25px;
    border-radius:20px;
    text-align:center;
    margin-bottom:20px;
    border:1px solid rgba(255,255,255,0.1);
}

/* Metric Cards */
[data-testid="metric-container"]{
    background: rgba(255,255,255,0.08);
    border-radius:15px;
    padding:15px;
    border:1px solid rgba(255,255,255,0.1);
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#111827;
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* Chat Messages */
[data-testid="stChatMessage"]{
    background:rgba(255,255,255,0.05);
    border-radius:15px;
    padding:10px;
}

/* Input */
.stChatInputContainer{
    background:rgba(255,255,255,0.05);
}

</style>
""", unsafe_allow_html=True)

# ==========================
# LOAD DATASET
# ==========================

try:
    df = pd.read_csv("data/diseases.csv")
except:
    st.error("❌ diseases.csv not found inside data folder")
    st.stop()

# ==========================
# HERO SECTION
# ==========================

st.markdown("""
<div class="hero">

<h1>🤖 AI Public Health Assistant</h1>

<p>
Disease Awareness • Symptom Analysis • Prevention Guidance
</p>

</div>
""", unsafe_allow_html=True)

# ==========================
# DASHBOARD STATS
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Diseases", len(df))

with col2:
    st.metric(
        "Categories",
        len(df["Category"].unique())
    )

with col3:
    st.metric("AI Status", "Online")

# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.title("🩺 Quick Symptoms")

    st.markdown("""
Try entering:

- Fever, Cough
- Headache
- Vomiting
- Fatigue
- Chest Pain
- Sore Throat
- Runny Nose
- Dizziness
""")

    st.success("AI Health Assistant Ready")

    st.warning(
        "This chatbot is for awareness purposes only."
    )

# ==========================
# CHAT HISTORY
# ==========================

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==========================
# CHAT INPUT
# ==========================

user_input = st.chat_input(
    "Enter symptoms (Example: fever, cough, headache)"
)

# ==========================
# PROCESS USER INPUT
# ==========================

if user_input:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    user_symptoms = user_input.lower()

    matches = []

    # Disease Matching
    for _, row in df.iterrows():

        symptoms = str(row["Symptoms"]).lower()

        score = 0

        for symptom in user_symptoms.split(","):

            symptom = symptom.strip()

            if symptom and symptom in symptoms:
                score += 1

        if score > 0:
            matches.append((score, row))

    matches.sort(
        key=lambda x: x[0],
        reverse=True
    )

    # ==========================
    # RESPONSE
    # ==========================

    if matches:

        response = "# 🩺 Possible Related Diseases\n\n"

        for score, disease in matches[:3]:

            confidence = min(score * 30, 95)

            response += f"""
## {disease['Disease']}

📂 **Category:** {disease['Category']}

🧾 **Symptoms**

{disease['Symptoms']}

🛡 **Prevention**

{disease['Prevention']}

⚠ **Risk Level:** {disease['Risk_Level']}

📊 **Confidence:** {confidence}%

---
"""

        response += """

### ⚠ Medical Disclaimer

This result is generated based on symptom matching.

It is NOT a medical diagnosis.

Please consult a qualified healthcare professional or doctor for proper examination and treatment.
"""

    else:

        response = """
# No Disease Match Found

Try symptoms such as:

- Fever
- Cough
- Headache
- Fatigue
- Vomiting
- Chest Pain

⚠ Please consult a healthcare professional for medical advice.
"""

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)