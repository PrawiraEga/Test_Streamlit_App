import streamlit as st
# import pandas as pd
# from data import data_scraping
from pages import analysis

def app():
    st.title("Home Page")
    # st.write("## This Sentiment Analysis Data App related to cryptocurrency news can help understand how public and media opinions influence the price.")
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

    st.page_link("pages/analysis.py", label=" Start Analysis", icon="🌎")
    # st.button("Show News", type="primary", on_click=analysis.app())
    
    # txt_list = data_scraping.get_data_scrap()
    # next_txt_list = data_scraping.get_data_scrap_two()

    # all_txt= txt_list + next_txt_list

    # df_scrap = pd.DataFrame(all_txt, columns=['Berita'])
    # Load dataset
    # df = pd.read_csv('data/sample_data.csv')
    # df_scrap = data_scraping.get_data_scrap()
    
    # Display dataset
    # st.write("### News Data Scraped")
    # st.dataframe(df_scrap)
    
    # Display statistics
    # st.write("### Summary Statistics")
    # st.write(df_scrap.describe())

    # # Display department-wise grouping
    # st.write("### Average Salary by Department")
    # avg_salary = df.groupby('department')['salary'].mean()
    # st.bar_chart(avg_salary)
