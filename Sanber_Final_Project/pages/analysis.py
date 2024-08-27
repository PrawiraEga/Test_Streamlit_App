import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import nltk
from data import data_scraping
from process import text_cleaning, vader_senti
from nltk_download import download_nltk_pkg

def app():
    st.title("Analysis Page")
    st.write("Here Is Analysis Page of The Scraped News")

    on = st.toggle("Show Data")

    df = pd.DataFrame()
    sum_df = pd.DataFrame()

    if on:
        # st.write("Show News!")
       list_txt =  data_scraping.get_all_items()
       df = pd.DataFrame(list_txt, columns=['Berita'])
       
       # Tampilkan DataFrame
       st.write("### Latest News DataFrame")
       editable_df = st.data_editor(df, width=1000, num_rows="dynamic")
       st.session_state.df_st = editable_df
       st.write(
       """
       Users can add additional news by clicking the add icon at the top right of the table.
       """
       )
      
       
       # Add Sentiment
    if st.button("Show Sentiment"): 
       data_df = dataframe_process.process_df(editable_df)
       sum_df = data_df["df"]

       st.session_state.df_sum = data_df["df"]
     
       st.write("### News With Sentiment")
       st.write(
       """
       The first sentiment analysis uses the Vader Sentiment model. For the second sentiment analysis, SentiWordNet is utilized. 
       The final outcome is achieved by combining the sentiment labels provided by each model.
       """
       )
       st.dataframe(sum_df)

    if st.button("Show Sentiment Distribution"):
        sum_df = st.session_state.df_sum
        st.write("### News With Sentiment")
        st.dataframe(sum_df)

        st.write("### Sentiment Distribution")
        visualization.senti_plot(sum_df)
      
app()


