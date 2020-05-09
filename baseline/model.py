import pandas as pd
from stop_words import get_stop_words
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import SGDClassifier
from sklearn import svm


def train_model(df, test_size=.15):
    X_col = df.iloc[:, 0] # <class 'pandas.core.series.Series'>
    y_col = df.iloc[:, 1] # <class 'pandas.core.series.Series'>

    stop_words = get_stop_words('de')

    # Create a processing pipeline containing preprocessing and the model:
    text_clf = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', SGDClassifier(loss='hinge', penalty='l2')), #SVM
    ])

    X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=test_size)

    # Automatic parameter tuning using grid search:
    parameters = {
        'vect__ngram_range': ((1, 1), (1, 2)),  # unigrams or bigrams
        'vect__stop_words': (None, stop_words),
        'tfidf__use_idf': (True, False),
        'clf__alpha': (1e-2, 1e-3),
    }

    gs_clf = GridSearchCV(text_clf, parameters, cv=5, n_jobs=-1)
    gs_clf.fit(X_train, y_train)

    return gs_clf.score(X_test, y_test)