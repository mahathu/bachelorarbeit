import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from string import ascii_letters, digits
from nltk import bigrams

allowed_chars = 'öäüßÖÄÜẞ =->%'
def clean_text(s):
    if type(s) is float:
        return ""
    """remove special characters and return lowercase text""" 
    return "".join([ch for ch in s.lower() if ch in (ascii_letters + digits + allowed_chars)])

def get_tokens(s):
    """return a list of tokens separated by spaces from string"""
    tokens = s.split()
    return filter(lambda token: len(token)>1, tokens)

def get_ngrams(s, ngram_range=2):
    """return a list of word ngrams from string"""
    # tokens = s.split()
    # return filter(lambda token: len(token)>1, tokens)
    # return bigrams(s.split()) # NLTK bigrams method
    words = s.split()
    return [' '.join(words[i:i+ngram_range]) for i in range(len(words)-1)]

if __name__ == '__main__':
    text_varids = [
        ('Visite_ZNS', 22085815),
        # ('Visite_Pflege', 22085836),
        # ('Visite_Oberarzt', 22085820),
    ]

    in_file_url = '../data/clean/all_scores.csv'
    df = pd.read_csv(in_file_url)

    for name, varid in text_varids:
        print(f"### {name} ###")
        texts = df[df['VarID'] == varid]['wert']

        all_tokens = []
        texts.apply(lambda t: all_tokens.extend(get_ngrams(clean_text(t))))
        
        word_counts = pd.DataFrame(data=Counter(all_tokens).items(), columns=['token', 'count'])
        print(f"{len(all_tokens)} total tokens ({len(word_counts)} unique) across {len(texts)} texts")
        word_counts.sort_values('count', ascending=False, inplace=True)

        rare_words = word_counts[word_counts['count'] <= 1]
        print(f"{len(rare_words)} tokens with only 1 occurence")
        print(word_counts.head(30))
        print()
        