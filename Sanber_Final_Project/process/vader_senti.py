# VADER
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def set_vader(txt):
    # Inisialisasi analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Mendapatkan hasil sentimen
    sentiment = analyzer.polarity_scores(txt)
    sentiment_comp = sentiment.get('compound')

    if sentiment_comp >= 0.05:
        sentiment_label = 'POSITIVE'
    elif sentiment_comp <= -0.05:
        sentiment_label = 'NEGATIVE'
    else:
        sentiment_label = 'NEUTRAL'

    sentiment.update({'label': sentiment_label})

    return sentiment_label
