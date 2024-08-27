import streamlit as st
import matplotlib.pyplot as plt

def senti_plot(df):
    fig, ax = plt.subplots()
    ax.hist(df['Sentimen_Sum'], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel('Sentimen_Label')
    ax.set_ylabel('Frequency')
    ax.set_title('Sentiment Distribution')
    # Tampilkan plot di Streamlit
    st.write("### Sentiment Distribution Histogram")
    st.pyplot(fig)
