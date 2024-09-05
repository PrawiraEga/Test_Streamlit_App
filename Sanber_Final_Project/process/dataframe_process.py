import pandas as pd
from data import data_scraping
from process import text_cleaning, vader_senti, sentiword, lexicon_senti, convert_senti

df = pd.DataFrame()
df_stg = pd.DataFrame()

def process_df(pd_df):
    # list_item = data_scraping.get_all_items()
    # df = pd.DataFrame(list_item, columns=['Berita'])
    df = pd_df
    df_stg = df.copy()
       
    # Do Text Cleaning
    df_stg['Berita_Clean'] = df['Berita'].apply(text_cleaning.clean_text_spacy)
    
   # Set Sentiment
    df_stg['Sentimen_One'] = df_stg['Berita_Clean'].apply(vader_senti.set_vader)
    df_stg['Sentimen_Two'] = df_stg['Berita_Clean'].apply(sentiword.set_senti)
    df_stg['Sentimen_Tri_Dict'] = df_stg['Berita_Clean'].apply(lexicon_senti.opini_lex_senti)
    df_stg['Sentimen_Tri'] = df_stg['Sentimen_Tri_Dict'].str.get('label')
    
    # Copy Sentiment To Main DF
    df['Sentimen_One'] = df_stg['Sentimen_One'] 
    df['Sentimen_Two'] = df_stg['Sentimen_Two']
    df['Sentimen_Tri'] = df_stg['Sentimen_Tri']
    
    # Label To Number
    df_stg['Sentimen_One_Val'] = df_stg['Sentimen_One'].apply(convert_senti.senti_to_val)
    df_stg['Sentimen_Two_Val'] = df_stg['Sentimen_Two'].apply(convert_senti.senti_to_val)
    df_stg['Sentimen_Tri_Val'] = df_stg['Sentimen_Tri'].apply(convert_senti.senti_to_val)
    df_stg['Sentimen_One_Val'] = df_stg['Sentimen_One_Val'].astype(int)
    df_stg['Sentimen_Two_Val'] = df_stg['Sentimen_Two_Val'].astype(int)
    
    # Total Sentiment Value
    df_stg['Sentimen_Total_Val'] = df_stg['Sentimen_One_Val'] + df_stg['Sentimen_Two_Val'] + df_stg['Sentimen_Tri_Val']
    
    # Number To Label
    df_stg['Sentimen_Sum'] = df_stg['Sentimen_Total_Val'].apply(convert_senti.senti_to_label) 
    
    # Add Column Sentiment To First DF
    df['Sentimen_Sum'] = df_stg['Sentimen_Sum']

    df.index += 1
    df_stg.index += 1

    df_dict = {
        "df" : df,
        "df_stg" : df_stg
    }

    return df_dict

def sum_senti_df(df, col):
    df_sum = df[col].value_counts()
    return df_sum
