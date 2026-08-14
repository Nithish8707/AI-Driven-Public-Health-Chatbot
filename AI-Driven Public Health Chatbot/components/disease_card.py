import streamlit as st


def disease_card(
    disease_name,
    emoji,
    symptoms,
    prevention,
    description
):

    with st.expander(f"{emoji} {disease_name}"):

        st.write(description)

        st.subheader("Symptoms")

        for symptom in symptoms:
            st.write(f"• {symptom}")

        st.subheader("Prevention")

        for item in prevention:
            st.write(f"• {item}")