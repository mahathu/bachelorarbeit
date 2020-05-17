import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import SGDClassifier
from sklearn import svm

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

import re

stop_words = stopwords.words('german')

def clean_text(text):
    stemmer = SnowballStemmer('german')
    pattern = re.compile('[^a-zA-Z0-9äöüÄÖÜß \.]', re.UNICODE) #remove all but words

    text = pattern.sub(' ', text) # remove special characters
    text = ' '.join( [stemmer.stem(word) for word in text.split()] ) # stem words
    return text

def train_model(df, test_size=.15, ngram_max_len=3):
    df['text_clean'] = df['text'].apply(clean_text)

    X_col = df['text_clean'] #df['text']
    y_col = df['label']
    
    # Create a processing pipeline containing preprocessing and the model:
    text_clf = Pipeline([
        ('vect', CountVectorizer()), # count terms
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('clf', svm.SVR(cache_size=2048)), #SVM
    ])

    X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=test_size)
    
    # Automatic parameter tuning using grid search:
    gs_params = {
        'vect__ngram_range': tuple((1,i+1) for i in range(ngram_max_len)), # ((1,1), (1,2), (1,3)
        'vect__stop_words': (None, stop_words), # use stop words or not
        'tfidf__use_idf': (True, False), # divide term frequency by document frequency?
    }
    
    gs_clf = GridSearchCV(text_clf, gs_params, cv=5, n_jobs=-1)
    gs_clf.fit(X_train, y_train)

    acc = gs_clf.score(X_test, y_test)

    return acc