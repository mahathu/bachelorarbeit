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
from utilities import save_performance_report, clean_text, clean_and_stem_text, rmstop_clean_stem, brief_dict, get_x_y
from nltk.stem import SnowballStemmer

def search_params_SVR(X_col, y_col, scoring_method):
    #X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=.15)
    
    # gs_params = [
    #     { # concatenate the dicts to finally save a list of dicts in gs_params
    #         'vect__analyzer': ['word'],
    #         'vect__ngram_range': [(1,1), (1,2), (1,5), (2,6)],
    #         'vect__preprocessor': [lambda s: s.lower(), clean_text, clean_and_stem_text, rmstop_clean_stem],
    #         'svr__kernel': ['linear', 'rbf', 'poly', 'sigmoid'], 
    #         'svr__C': [10**-i for i in range(3)], # [1, 0.1, 0.01, 0.001] 
    #         'svr__epsilon': [0.05, 0.1, 0.15],
    #     },
    #     {   
    #         'vect__analyzer': ['char', 'char_wb'],
    #         'vect__ngram_range': [(2,6), (3,7), (4,12)],
    #         'vect__preprocessor': [lambda s: s.lower(), clean_text, clean_and_stem_text, rmstop_clean_stem],
    #         'svr__kernel': ['linear', 'rbf', 'poly', 'sigmoid'], 
    #         'svr__C': [10**-i for i in range(3)], # [1, 0.1, 0.01, 0.001] 
    #         'svr__epsilon': [0.05, 0.1, 0.15],
    #     },
    # ]
    
    gs_params = {   
        'vect__analyzer': ['char'],
        'vect__ngram_range': [(1,5), (2,6), (4,12), (6,8)],
        'vect__preprocessor': [rmstop_clean_stem],
        'svr__kernel': ['linear', 'rbf', 'poly'], 
        'svr__C': [10, 1, 0.1, 0.01, 0.001, 0.0003],
        'svr__epsilon': [0.01, 0.025, 0.05, 0.1, 0.15, 0.25, 0.4, 1],
    },


    # Create a processing pipeline containing preprocessing and the model:
    rgr_pipeline = Pipeline([
        ('vect', CountVectorizer()), # count terms or chars
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('svr', SVR(cache_size=1000)), #SVR
    ])

    # Automatic parameter tuning using grid search:
    print(f"GridSearchCV running for SVR perf_metric: {scoring_method}...")

    # will run 5-fold cross validation!
    gs_rgr = GridSearchCV(
        rgr_pipeline, 
        gs_params, 
        scoring=scoring_method, 
        n_jobs=10, 
        verbose=2,
        cv=4
    )

    gs_rgr.fit(X_col, y_col)
    
    params = gs_rgr.cv_results_['params'] # eine Liste (n=n param-kombis "candidates") von dicts mit den parametern und deren entsprechenden Werten.
    print(len(params))

    out_rows = []
    for i, param_dict in enumerate(params):
        for key in ['mean_test_score', 'std_test_score', 'rank_test_score', 'mean_fit_time']:
            param_dict[key] = gs_rgr.cv_results_[key][i]
        
        for key, value in param_dict.items():
            if callable(value): # val is a function
                param_dict[key] = value.__name__
            elif value.__class__.__name__ in ('list', 'tuple') and len(value) > 5: # val is a (long!) list
                param_dict[key] = f"List (n={len(value)})"
        
        out_rows.append(param_dict)
    
    df = pd.DataFrame(out_rows)
    df.to_csv('GridsearchCV_results_char_e_C.csv', index=False)

    best_params = brief_dict(gs_rgr.best_params_)
    print(best_params)

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
        max_samples=1250
    )

    search_params_SVR(X, y, 'neg_root_mean_squared_error')