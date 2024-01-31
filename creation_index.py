import json
import re
import nltk
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text, options):
    # Tokenization
    tokens = word_tokenize(text)

    # Lowercasing
    if 'lowercase' in options:
        tokens = [token.lower() for token in tokens]

    # Removing stopwords
    if 'remove_stopwords' in options:
        stop_words = set(stopwords.words('english'))
        tokens = [token for token in tokens if token not in stop_words]

    # Stemming
    if 'stemming' in options:
        stemmer = PorterStemmer()
        tokens = [stemmer.stem(token) for token in tokens]

    return tokens

def build_non_pos_index(documents, options):
    index = defaultdict(list)

    # Statistics
    num_documents = len(documents)
    num_tokens_global = 0
    num_tokens_per_field = {'title': 0, 'content': 0, 'h1': 0}

    for doc in documents:
        # Extracting information
        url = doc['url']
        title = doc['title']
        content = doc['content']
        h1 = doc['h1']

        # Tokenizing and processing
        title_tokens = preprocess_text(title, options)
        content_tokens = preprocess_text(content, options)
        h1_tokens = preprocess_text(h1, options)

        # Updating statistics
        num_tokens_global += len(title_tokens) + len(content_tokens) + len(h1_tokens)
        num_tokens_per_field['title'] += len(title_tokens)
        num_tokens_per_field['content'] += len(content_tokens)
        num_tokens_per_field['h1'] += len(h1_tokens)

        # Building non-positional index
        for token in set(title_tokens + content_tokens + h1_tokens):
            index[token].append(url)

    return index, {
        'num_documents': num_documents,
        'num_tokens_global': num_tokens_global,
        'num_tokens_per_field': num_tokens_per_field,
        'avg_tokens_per_document': num_tokens_global / num_documents
    }