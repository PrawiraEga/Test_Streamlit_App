import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from data import data_scraping, visualization
from process import text_cleaning, vader_senti, sentiword, convert_senti, dataframe_process
import nltk




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
       data_df = dataframe_process.process_df(st.session_state.df_st)
       sum_df = data_df["df"]

       st.session_state.df_sum = data_df["df"]
     
       st.write("### News With Sentiment")
       st.write(
       """
       The first sentiment analysis uses the Vader Sentiment model. For the second sentiment analysis, SentiWordNet is utilized. 
       The final outcome is achieved by combining the sentiment labels provided by each model.
       """
       )
       st.dataframe(sum_df, width=1000)

    if st.button("Show Sentiment Distribution"):
        st.write("### Sentiment Distribution")
        sum_df = st.session_state.df_sum
        g1, g2, g3 = st.columns((1,1,1))
        # st.write("### Sentiment Only")
        df_sen_one = dataframe_process.sum_senti_df(sum_df,'Sentimen_One')
        df_sen_two = dataframe_process.sum_senti_df(sum_df,'Sentimen_Two')
        df_sen_sum = dataframe_process.sum_senti_df(sum_df,'Sentimen_Sum')

        fig1 = visualization.plotly_chart(df_sen_one, 'Sentimen_One')
        g1.plotly_chart(fig1)

        fig2 = visualization.plotly_chart(df_sen_two, 'Sentimen_Two')
        g2.plotly_chart(fig2)

        fig3 = visualization.plotly_chart(df_sen_sum, 'Sentimen_Sum')
        g3.plotly_chart(fig3)
      
app()

    


