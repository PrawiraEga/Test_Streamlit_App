# Menggunakan Opinion Lexicon
import nltk
from process import convert_senti as cs
from nltk.corpus import opinion_lexicon

def opini_lex_senti(text):
    
    # Tokenisasi
    tokens = nltk.word_tokenize(text.lower())

    # Hitung kata-kata positif dan negatif
    positive_words = set(opinion_lexicon.positive())
    negative_words = set(opinion_lexicon.negative())

    positive_count = sum(1 for word in tokens if word in positive_words)
    negative_count = sum(1 for word in tokens if word in negative_words)

    sentimen_count = positive_count - negative_count

    sentimen_label = cs.senti_to_label(sentimen_count)

    senti_res = {
        "count" : sentimen_count,
        "label" : sentimen_label
    }

    return senti_res
