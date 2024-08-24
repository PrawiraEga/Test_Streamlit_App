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
    download_nltk_pkg()
    # txt_list = data_scraping.get_data_scrap()
    # next_txt_list = data_scraping.get_data_scrap_two()
    # all_txt_list = txt_list + next_txt_list

    on = st.toggle("Show Data")

    if on:
        # st.write("Show News!")
       list_item = data_scraping.get_data_scrap_two()
       df = pd.DataFrame(list_item, columns=['Berita'])
       df_clean = df.copy()  
    #    st.write("### DataFrame")
    #    st.dataframe(df) 
    #    if st.button("Show Data"):
          
        # Do Text Cleaning
       df_clean['Berita_Clean'] = df['Berita'].apply(text_cleaning.clean_text_spacy)
       
        # Set Sentiment
       df_clean['Sentimen'] = df_clean['Berita_Clean'].apply(vader_senti.set_vader)

         # Tampilkan DataFrame
       st.write("### DataFrame")
       st.dataframe(df)
       
       if st.button("Show Distribution"):
              # Drop Kolom Berita Clean
            df_clean.drop(columns=['Berita_Clean'], inplace=True)
          # Plot Sentiment

        # Membuat histogram dari kolom 'Sentimen'
            fig, ax = plt.subplots()
            ax.hist(df_clean['Sentimen'], bins=5, color='skyblue', edgecolor='black')
            ax.set_xlabel('Sentimen_Label')
            ax.set_ylabel('Frequency')
            ax.set_title('Sentiment Distribution')

            # Tampilkan plot di Streamlit
            st.write("### Sentiment Distribution Histogram")
            st.pyplot(fig)
            df = pd.DataFrame()
    #     list_item = get_data_scrap_two()
    #     df = pd.DataFrame(list_item, columns=['Berita'])
    # Load dataset
    # df = pd.read_csv('data/sample_data.csv')
    # df = data_scraping.get_data_scrap()
    
    # Tampilkan DataFrame
    # st.write("### DataFrame")
    # st.dataframe(df_scrap)

    


