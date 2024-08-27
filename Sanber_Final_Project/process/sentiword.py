import nltk
from nltk.corpus import wordnet
from nltk.corpus import sentiwordnet as swn
from nltk.tokenize import word_tokenize 

# Fungsi untuk mendapatkan tag POS dari NLTK ke WordNet POS
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def set_senti(txt):
    # Tokenisasi dan POS tagging
    tokens = word_tokenize(txt)
    pos_tags = nltk.pos_tag(tokens)

    # Hitung skor sentimen
    sentiment_score = 0
    for word, tag in pos_tags:
        wn_tag = get_wordnet_pos(tag)
        if wn_tag is not None:
            synsets = list(swn.senti_synsets(word, wn_tag))
            if synsets:
                sentiment = synsets[0]
                sentiment_score += sentiment.pos_score() - sentiment.neg_score()

    if sentiment_score > 0:
        sentiment_label = 'POSITIVE'
    elif sentiment_score < 0:
        sentiment_label = 'NEGATIVE'
    else:
        sentiment_label = 'NEUTRAL'

    return sentiment_label    
