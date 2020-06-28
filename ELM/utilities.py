import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from string import ascii_letters, digits
from nltk import bigrams

allowed_chars = set(ascii_letters + digits + 'öäüßÖÄÜẞ =-%')
stop_words = set(['pat', '-pat', 'patient', 'patientin', '-', 'sich', 'zu', 'hat', 'und'])

def clean_text(s, remove_stop_words=True):
    """remove special characters and return lowercase text"""
    if type(s) is float: # some elements in Visite_ZNS are "nan"
        return "NA"
    
    s.replace('4/4', '44')
    s.replace('/', '/ ') # extra leerzeichen, sodass Worte die
                         # vorher durch '/' getrennt waren nicht
                         # zu einem gemeinsamen Token werden

    tokens = ''.join(filter(lambda ch: ch in allowed_chars, s.lower())).split()
    
    if not remove_stop_words:
        return " ".join(tokens) # remove multiple whitespaces in a row

    tokens = [word for word in tokens if not word in stop_words]
    return " ".join(tokens)

def get_tokens(s):
    """return a list of tokens separated by spaces from string"""
    tokens = s.split()
    return filter(lambda token: len(token)>1, tokens)

def get_ngrams(s, ngram_range=1):
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
        print(word_counts.head(50))
        print()
        