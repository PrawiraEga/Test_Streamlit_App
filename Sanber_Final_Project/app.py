import streamlit as st
from nltk_download import download_nltk_pkg
st.set_page_config(page_title="Sentiment Analysis Data App", page_icon="📊", layout="centered")

# Sidebar navigation
st.sidebar.title("Navigation")
pages = ["Home", "Analysis"]
page = st.sidebar.radio("Go to", pages)

download_nltk_pkg()

if page == "Home":
    import pages.home as home
    home.app()
elif page == "Analysis":
    import pages.analysis as analysis
    analysis.app()
