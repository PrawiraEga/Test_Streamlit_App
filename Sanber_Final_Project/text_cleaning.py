# SpaCy
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

txt = "Liquidity Crisis Causes Major Price Slippages During Cryptocurrency Sell-Offs: Kaiko"

def clean_text_spacy(text):
    # Parse the text with spaCy
    doc = nlp(text)

    # Lowercasing, remove stop words, lemmatization, dan remove angka
    text = ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha])

    return text

cln_txt = clean_text_spacy(txt)

print(cln_txt)