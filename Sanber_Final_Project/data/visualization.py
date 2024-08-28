import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import random

def senti_plot(df):
    fig, ax = plt.subplots()
    ax.hist(df['Sentimen_Sum'], bins=5, color='skyblue', edgecolor='black')
    ax.set_xlabel('Sentimen_Label')
    ax.set_ylabel('Frequency')
    ax.set_title('Sentiment Distribution')
    # Tampilkan plot di Streamlit
    st.write("### Sentiment Distribution Histogram")
    st.pyplot(fig)

def plotly_chart(df, col):
    random_int = random.randint(100000, 270000)
    fig = px.bar(df, y = 'count', template = 'seaborn')
    fig.update_traces(marker_color='#'+str(random_int))
    fig.update_layout(title_text="Number of " + col,title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title="Total", xaxis_title="Sentimen")
    
    return fig
