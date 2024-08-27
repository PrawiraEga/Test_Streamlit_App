import pandas as pd
from data import data_scraping
from process import text_cleaning, vader_senti, sentiword, convert_senti

df = pd.DataFrame()
df_stg = pd.DataFrame()

def process_df(pd_df):
    df = pd_df
    df_stg = df.copy()
       
    # Do Text Cleaning
    df_stg['Berita_Clean'] = df['Berita'].apply(text_cleaning.clean_text_spacy)
    
    # Set Sentiment
    df_stg['Sentimen_One'] = df_stg['Berita_Clean'].apply(vader_senti.set_vader)
    df_stg['Sentimen_Two'] = df_stg['Berita_Clean'].apply(sentiword.set_senti)
    
    # Copy Sentiment To Main DF
    df['Sentimen_One'] = df_stg['Sentimen_One'] 
    df['Sentimen_Two'] = df_stg['Sentimen_Two']
    
    # Label To Number
    df_stg['Sentimen_One_Val'] = df_stg['Sentimen_One'].apply(convert_senti.senti_to_val)
    df_stg['Sentimen_Two_Val'] = df_stg['Sentimen_Two'].apply(convert_senti.senti_to_val)
    df_stg['Sentimen_One_Val'] = df_stg['Sentimen_One_Val'].astype(int)
    df_stg['Sentimen_Two_Val'] = df_stg['Sentimen_Two_Val'].astype(int)
    
    # Total Sentiment Value
    df_stg['Sentimen_Total_Val'] = df_stg['Sentimen_One_Val'] + df_stg['Sentimen_Two_Val']
    
    # Number To Label
    df_stg['Sentimen_Sum'] = df_stg['Sentimen_Total_Val'].apply(convert_senti.senti_to_label) 
    
    # Add Column Sentiment To First DF
    df['Sentimen_Sum'] = df_stg['Sentimen_Sum']

    df_dict = {
        "df" : df,
        "df_stg" : df_stg
    }

    return df_dict

def sum_senti_df(df):
    df_sum = df.groupby(['Sentimen_Sum']).count()
    
    if 'Sentimen_One' in df_sum.columns:
        df.drop(columns=['Sentimen_One'], inplace=True)
       
    if 'Sentimen_Two' in df_sum.columns:
        df.drop(columns=['Sentimen_Two'], inplace=True)
    
    return df_sum
