import streamlit as st
import subprocess
from nltk_download import download_nltk_pkg

def app():
    st.set_page_config(page_title='Sentiment App' ,layout="wide",page_icon='👨‍🔬')
    st.title("Home Page")
    # st.write("## This Sentiment Analysis Data App related to cryptocurrency news can help understand how public and media opinions influence the price.")
    
    download_nltk_pkg()

    st.write(
    """
    # Sentiment Analysis Data App

    Welcome to my project! 👋 This app shows sentiment analysis related to cryptocurrency news. 
    By using sentiment analysis, users can make more informed and strategic investment decisions, 
    as well as predict market movements based on detected sentiment trends. ✨
    """
    )

    st.write(
    """
    The news sources are taken from the portals cryptopotato and cryptorank.
    """
    )

    if st.button("Start!"):
        st.switch_page("pages/2_Analysis.py")

app()
