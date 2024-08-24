# SpaCy
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def clean_text_spacy(text):
    # Parse the text with spaCy
    doc = nlp(text)
    txt = str(text)
    # Lowercasing, remove stop words, lemmatization, dan remove angka
    txt = ' '.join([token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha])

    return txt
