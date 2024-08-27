# Sentiment Analysis of Cryptocurrency News

This project focuses on analyzing the sentiment of news articles related to cryptocurrency. The goal is to classify the sentiment of news articles as positive, negative, or neutral, providing insights into market sentiment and trends in the cryptocurrency space.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Data](#data)
- [Installation](#installation)
- 
## Introduction

Cryptocurrency markets are highly volatile and sensitive to news and events. Analyzing the sentiment of news articles can provide valuable insights into market behavior and help in making informed decisions. This project uses natural language processing (NLP) techniques to classify the sentiment of cryptocurrency-related news articles.

## Features

- **Data Collection**: Scraping and gathering news articles related to cryptocurrency from various cryptocurrency news portal sources.
- **Text Preprocessing**: Cleaning and preprocessing of news articles to prepare them for sentiment analysis using SpaCy Library.
- **Sentiment Analysis**: Implementing various sentiment analysis models to classify the sentiment of the articles.
- **Visualization**: Visualizing the sentiment trends over time.

## Data

The data consists of news articles related to various cryptocurrencies. Each article includes the following fields:

- **Berita**: The title of the news article.
- **Sentiment_One**: The sentiment analysis using Vader model.
- **Sentiment_Two**: The sentiment analysis using Sentiword model NLTK library.
- **Sentiment_Two**: The summary of sentiment analysis by combining two model.

### Example Data Format

| Berita                                         | Sentiment_One  | Sentiment_Two    | Sentiment_Sum
|------------------------------------------------|----------------|------------------|---------------|
| Bitcoin Price Surges as Investors Flock to BTC |    POSITIVE    |     NEUTRAL      |  POSITIVE     |
| Ethereum Network Faces Congestion Issues       |    NEGATIVE    |     NEGATIVE     |  NEGATIVE     |

## Installation

To run this project locally, you will need Python 3.x and the following dependencies:
- request
- pandas
- numpy
- nltk
- spacy
- beautifulsoup4
- matplotlib
- seaborn
- vaderSentiment
- streamlit

You can install the dependencies using pip:

pip install -r requirements.txt
