import streamlit as st
import subprocess

st.set_page_config(page_title="Sentiment Analysis Data App", page_icon="📊", layout="centered")

# Sidebar navigation
st.sidebar.title("Navigation")
pages = ["Home", "Analysis"]
page = st.sidebar.radio("Go to", pages)

# CMD SpaCy download
command = "python -m spacy download en_core_web_sm"
    # Run CMD through subprocess
try:
    subprocess.run(command, check=True, shell=True)
    print("Model 'en_core_web_sm' download succesfull.")
except subprocess.CalledProcessError as e:
    print(f"Error while downloading: {e}")

if page == "Home":
    import pages.home as home
    home.app()
elif page == "Analysis":
    import pages.analysis as analysis
    analysis.app()
