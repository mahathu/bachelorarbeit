import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from nltk.corpus import stopwords
from datetime import datetime
from os.path import isfile
from utilities import iprint, sprint, wprint, eprint, save_performance_report, clean_text, clean_and_stem_text, brief_dict, get_x_y
from nltk.stem import SnowballStemmer

def search_params_SVR(X_col, y_col, scoring_method):
    X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=.15)
    
    gs_params = { # concatenate the dicts to finally save a list of dicts in gs_params
        #{**in_transform, **svr} for svr in svr_param_grids for in_transform in input_param_grids
        'vect__analyzer': ['char', 'char_wb', 'word'],
        'vect__ngram_range': [(1,5), (2,6), (4,7), (4,9), (5,12)],
        'vect__preprocessor': [None, clean_and_stem_text],  
        'vect__stop_words': [[], stopwords.words('german')], # use stop words when analyzing char ngrams
        'svr__kernel': ['linear', 'rbf', 'poly', 'sigmoid'], 
        'svr__C': [10**-i for i in range(4)]  # [1, 0.1, 0.01, 0.001] 
    }

    # Create a processing pipeline containing preprocessing and the model:
    rgr_pipeline = Pipeline([
        ('vect', CountVectorizer()), # count terms or chars
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('svr', SVR(cache_size=1000)), #SVR
    ])

    # Automatic parameter tuning using grid search:
    iprint(f"GridSearchCV running for SVR perf_metric: {scoring_method}...")

    # will run 5-fold cross validation!
    regressor = GridSearchCV(
        rgr_pipeline, gs_params, scoring=scoring_method, n_jobs=-1, verbose=1, cv=5
    )
    
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    best_params = brief_dict(regressor.best_params_)

    wprint(f"{len(X_test)} test pairs used")
    sprint(f"Best parameters set found on development set: \n{best_params}\n")

    scores = {
        "mae": mean_absolute_error(y_test, y_pred),
        #"rmse": np.sqrt(mean_squared_error(y_test, y_pred)),
        "r2": regressor.score(X_test, y_test),
    }

    sprint(f"Performance for model after hyperparameter tuning using {scoring_method}:")
    for s in scores:
        print(f"{s:>4}: {scores[s]:.3f}")

    param_names = []
    for d in gs_params: #d is a dict
        for n in d:
            if n not in param_names:
                param_names.append(n)

    save_performance_report('SVR_0626', regressor, param_names, scoring_method, len(X_col))

def get_SVR(use_tuned_hyperparameters=True, filter_rass=False):
    cache_size = 1024
    cv = CountVectorizer(
        analyzer='char',
        ngram_range=(1,5),
        preprocessor=lambda s: s.lower()
    )
    
    if filter_rass:
        cv = CountVectorizer(
            analyzer='char',
            ngram_range=(1,5),
            preprocessor=filter_rass_occurences
        )

    if use_tuned_hyperparameters: # Create a processing pipeline with the best hyperparameters:
        return Pipeline([
            ('vect', cv),
            ('tfidf', TfidfTransformer()),
            ('svr', SVR(cache_size=cache_size, C=10)), #das sind wirklich die besten Hyperparameter!
        ])
    
    # else use a standard SVR
    return Pipeline([ # no tuned hyperparameters!
        ('vect', cv),
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('svr', SVR(cache_size=cache_size, C=10)),
    ])

def filter_rass_occurences(s):
    l = s.lower()
    index = l.find('rass')
    if index < 0:
        return l

    return l[:index] + l[index+7:]

if __name__ == '__main__':
    print("Initializing gridsearch cv.")

    df_all = pd.read_csv("../../data/clean/labels_nearest_all.csv")
    
    X, y = get_x_y(df_all, 22085815, 22086158, 
        max_min_between=45, 
        max_samples=1000
    )

    search_params_SVR(X, y, 'neg_root_mean_squared_error')