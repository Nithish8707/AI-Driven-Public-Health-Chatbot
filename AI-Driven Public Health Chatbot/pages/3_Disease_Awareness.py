import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Disease Awareness",
    page_icon="🩺",
    layout="wide"
)

# DARK THEME
st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #0E1117;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #161B22 !important;
}

/* Sidebar Text */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Main Text */
html, body, [class*="css"] {
    color: white !important;
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: white !important;
}

/* Paragraphs */
p, label, span {
    color: white !important;
}

/* Input Box */
.stTextInput input {
    background-color: #262730 !important;
    color: white !important;
    border: 1px solid #444 !important;
}

/* Select Box */
.stSelectbox div[data-baseweb="select"] {
    background-color: #262730 !important;
    color: white !important;
}

/* Buttons */
.stButton > button {
    background-color: #262730 !important;
    color: white !important;
    border: 1px solid #444 !important;
}

/* Metrics */
[data-testid="stMetricValue"] {
    color: white !important;
}

[data-testid="stMetricLabel"] {
    color: white !important;
}

/* Divider */
hr {
    border-color: #444 !important;
}

</style>
""", unsafe_allow_html=True)

# Load Dataset
try:
    df = pd.read_csv("data/diseases.csv")
except:
    st.error("diseases.csv not found in data folder.")
    st.stop()

# Title
st.title("🩺 Disease Awareness Center")

st.markdown("""
Learn about diseases, symptoms, prevention methods,
and risk levels through our public health awareness platform.
""")

st.divider()

# Search Box
search = st.text_input(
    "🔍 Search Disease",
    placeholder="Enter disease name..."
)

# Category Filter
categories = ["All"] + sorted(df["Category"].unique().tolist())

selected_category = st.selectbox(
    "Select Category",
    categories
)

# Apply Filters
filtered_df = df.copy()

if search:
    filtered_df = filtered_df[
        filtered_df["Disease"]
        .str.contains(search, case=False, na=False)
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

# Statistics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Diseases", len(df))

with col2:
    st.metric("Categories", len(df["Category"].unique()))

with col3:
    st.metric("Displayed", len(filtered_df))

st.divider()

# Risk Color Function
def get_risk_color(risk):
    risk = str(risk).lower()

    if risk == "high":
        return "#EF4444"
    elif risk == "medium":
        return "#F59E0B"
    return "#22C55E"

# Disease Cards
for _, row in filtered_df.iterrows():

    color = get_risk_color(row["Risk_Level"])

    st.markdown(
        f"""
        <div style="
            background-color:#1E1E1E;
            color:white;
            padding:20px;
            border-radius:15px;
            margin-bottom:20px;
            border-left:8px solid {color};
            box-shadow:0px 2px 10px rgba(0,0,0,0.5);
        ">

        <h2 style="color:white;">{row['Disease']}</h2>

        <p><b>Category:</b> {row['Category']}</p>

        <p>
            <b>Risk Level:</b>
            <span style="color:{color};font-weight:bold;">
                {row['Risk_Level']}
            </span>
        </p>

        <h4 style="color:white;">Symptoms</h4>
        <p>{row['Symptoms']}</p>

        <h4 style="color:white;">Prevention</h4>
        <p>{row['Prevention']}</p>

        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.warning(
    "⚠️ The information provided is for educational and awareness purposes only. "
    "Consult healthcare professionals for medical advice."
)