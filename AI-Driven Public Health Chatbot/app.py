import streamlit as st
from streamlit_option_menu import option_menu

selected = option_menu(
    menu_title=None,
    options=["Home", "Chatbot", "Disease Awareness", "About"],
    icons=["house", "robot", "heart-pulse", "info-circle"],
    orientation="horizontal"
)

if selected == "Home":
    exec(open("pages/1_Home.py", encoding="utf-8").read())

elif selected == "Chatbot":
    exec(open("pages/2_Chatbot.py", encoding="utf-8").read())

elif selected == "Disease Awareness":
    exec(open("pages/3_Disease_Awareness.py", encoding="utf-8").read())

elif selected == "About":
    exec(open("pages/4_About.py", encoding="utf-8").read())