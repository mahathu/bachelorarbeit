import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVR
from sklearn.dummy import DummyRegressor
from sklearn.metrics import classification_report, SCORERS

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

from termcolor import cprint

import re

def print_performance_report(regressor):
    # based on: https://scikit-learn.org/stable/auto_examples/model_selection/plot_grid_search_digits.html
    cprint(f"Best parameters set found on development set: \n{regressor.best_params_}\n", attrs=['bold'])
    cprint("Grid scores on development set:", attrs=['bold'])
    means = regressor.cv_results_['mean_test_score']
    stds = regressor.cv_results_['std_test_score']

    for mean, std, params in zip(means, stds, regressor.cv_results_['params']):
        if params['vect__stop_words']: # use a different string instead of printing the entire list
            params['vect__stop_words'] = f"Yes (n={len(params['vect__stop_words'])})"
        print("%0.3f (+/-%0.03f) for %r"
            % (mean, std * 2, params))
    print("\n")

def clean_text(text):
    stemmer = SnowballStemmer('german')
    pattern = re.compile('[^a-zA-Z0-9äöüÄÖÜß \.]', re.UNICODE) #remove all but words

    text = pattern.sub(' ', text) # remove special characters
    text = ' '.join( [stemmer.stem(word) for word in text.split()] ) # stem words
    return text

def train_SVR(df, X_col, y_col, test_size=.2):
    X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=test_size, random_state=1)

    scores = ['r2', 'neg_mean_squared_error'][:1] # https://scikit-learn.org/stable/modules/model_evaluation.html
    
    input_param_grids = [
        {
            'vect__analyzer': 'word',
            'vect__ngram_range': list((1,i+1) for i in range(3)), # try out these ngram ranges: (1,1), (1,2), (1,3)
            'vect__stop_words': [None, stopwords.words('german')], # use stop words or not
            'tfidf__use_idf': [True, False], # divide term frequency by document frequency?
        },
        {
            'vect__analyzer': 'char',
            'vect__ngram_range': (1,9),
            'vect__stop_words': [stopwords.words('german')], # use stop words when analyzing char ngrams
            'tfidf__use_idf': [True, False], # divide term frequency by document frequency?
        }
    ]

    # https://stats.stackexchange.com/questions/31066/what-is-the-influence-of-c-in-svms-with-linear-kernel
    svr_param_grids = [ # rgr_gamma is used only for kernel=rbf
        {'rgr__kernel': ['rbf'], 'rgr__gamma': ['scale', 'auto'], 'rgr__C': [1, 10, 100]},
        {'rgr__kernel': ['linear'], 'rgr__C': [1, 10, 100]}
    ]

    gs_params = [ # concatenate the dicts to finally save a list of dicts in gs_params
        {**in_transform, **svr} for svr in svr_param_grids for in_transform in input_param_grids
    ]


    for score in scores:
        cprint(f"### Tuning hyper-parameters for {score} ###", attrs=['bold', 'underline'])
 
        # Create a processing pipeline containing preprocessing and the model:
        clf_pipeline = Pipeline([
            #('vect', CountVectorizer(analyzer='char', ngram_range=(2,3))), # count characters
            ('vect', CountVectorizer()), # count terms
            ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
            ('rgr', SVR(cache_size=512)), #SVR
        ])

        # Automatic parameter tuning using grid search:
        cprint("GridSearchCV running...", "yellow")
        regressor = GridSearchCV(
            clf_pipeline, gs_params, scoring=score, n_jobs=-1, verbose=1
        )
        regressor.fit(X_train, y_train)

        performance = regressor.score(X_test, y_test)
        cprint(f"R^2 performance for model after hyperparameter tuning using {score}: {performance:.3f}\n", "green")
        
        print_performance_report(regressor)

    return 1