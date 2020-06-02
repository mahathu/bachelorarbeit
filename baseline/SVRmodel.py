import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error
from nltk.corpus import stopwords
from datetime import datetime
from os.path import isfile
from utilities import iprint, sprint, wprint, eprint, save_performance_report, clean_text

def search_params_SVR(df, X_col, y_col, score):
    X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=.2, random_state=1)
    
    input_param_grids = [
        {
            'vect__analyzer': ['word'],
            'vect__ngram_range': [(1,i+1) for i in [0,2,5]],
            'vect__stop_words': [None, stopwords.words('german')],
            'tfidf__use_idf': [True, False],
        },
        {
            'vect__analyzer': ['char'],
            'vect__ngram_range': [(1,9)],
            'vect__stop_words': [stopwords.words('german')], # use stop words when analyzing char ngrams
            'tfidf__use_idf': [True, False],
        }
    ]

    # https://stats.stackexchange.com/questions/31066/what-is-the-influence-of-c-in-svms-with-linear-kernel
    svr_param_grids = [ # svr_gamma is used only for kernel=rbf
        {'svr__kernel': ['rbf'], 'svr__gamma': ['scale', 'auto'], 'svr__C': [1, 10, 100]},
        {'svr__kernel': ['linear'], 'svr__C': [1, 10, 100]}
    ]

    gs_params = [ # concatenate the dicts to finally save a list of dicts in gs_params
        #{**in_transform, **svr} for svr in svr_param_grids for in_transform in input_param_grids
        {'svr__kernel': ['linear'], 'svr__C': [1, 10, 100]}
    ]

    print(f"Tuning hyper-parameters for {score}.")

    # Create a processing pipeline containing preprocessing and the model:
    clf_pipeline = Pipeline([
        ('vect', CountVectorizer()), # count terms or chars
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('svr', SVR(cache_size=512)), #SVR
    ])

    # Automatic parameter tuning using grid search:
    iprint("GridSearchCV running...")
    regressor = GridSearchCV(
        clf_pipeline, gs_params, scoring=score, n_jobs=-1, verbose=1 #remove cv=2
    )
    regressor.fit(X_train, y_train)

    performance = regressor.score(X_test, y_test)
    sprint(f"R^2 performance for model after hyperparameter tuning using {score}: {performance:.3f}")
    sprint(f"Best parameters set found on development set: \n{regressor.best_params_}\n")

    param_names = []
    for d in gs_params: #d is a dict
        for n in d:
            if n not in param_names:
                param_names.append(n)
    save_performance_report('SVR', regressor, param_names, score)

def test_SVR(df, X_col, y_col):
    X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=.2)

    # Create a processing pipeline with the best hyperparameters:
    clf_pipeline = Pipeline([
        ('vect', CountVectorizer(analyzer="char", ngram_range=(1,9), stop_words=stopwords.words('german'))), # count terms
        ('tfidf', TfidfTransformer(use_idf=False)), # transform to term freq. inverse document freq.
        ('svr', SVR(cache_size=512, C=10)),
    ])
    clf_pipeline_default = Pipeline([ # no tuned hyperparameters!
        ('vect', CountVectorizer()), # count terms
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('svr', SVR(cache_size=512)), 
    ])
    
    clf_pipeline.fit(X_train, y_train)
    
    y_pred = clf_pipeline.predict(X_test)
    sprint(f"MSE: {mean_squared_error(y_test, y_pred):6.3f}")
    sprint(f"MAE: {mean_absolute_error(y_test, y_pred):6.3f}")
    sprint(f"R^2: {clf_pipeline.score(X_test, y_test):6.3f}")

    return clf_pipeline.score(X_test, y_test)