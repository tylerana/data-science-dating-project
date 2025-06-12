'''
The purpose of this file is to clean four short user-written essay responses by
- lowercasing
- removing punctuation
- removing stopwords
- removing long words
- lemmatizing

and it returns a cleaned and space-joined token string.
'''
import re
import warnings
from datetime import datetime, timedelta

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import swifter
from sentence_transformers import SentenceTransformer
from spellchecker import SpellChecker

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

warnings.filterwarnings('ignore')

def process_user_essay(combined_user_essay):    
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    def preprocess_text(text):
        text = text.lower()
        text = re.sub(r"[^\w\s]", "", text)
        return text.split()

    def remove_stopwords(tokens):
        return [word for word in tokens if word not in stop_words]

    def remove_long_words(tokens, max_length=20):
        return [word for word in tokens if len(word) <= max_length]

    def lemmatization(tokens):
        return [lemmatizer.lemmatize(word) for word in tokens]
    
    tokens = preprocess_text(combined_user_essay)
    tokens = remove_stopwords(tokens)
    tokens = remove_long_words(tokens)
    tokens = lemmatization(tokens)
    
    return " ".join(tokens)