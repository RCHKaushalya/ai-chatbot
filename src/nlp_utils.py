import nltk
from nltk.tokenize import word_tokenize
import string

nltk.download('punkt')

def preprocess_text(text):
    text = text.lower()

    for char in string.punctuation:
        text = text.replace(char, '')

    tokens = word_tokenize(text)

    return tokens