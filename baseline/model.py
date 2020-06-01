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
from datetime import datetime
from os.path import isfile

import re

def save_performance_report(estimator_name, regressor_obj, all_params, scoring_method):
    means = regressor_obj.cv_results_['mean_test_score']
    stds = regressor_obj.cv_results_['std_test_score']
    df_rows = []
    df_colnames = ["estimator", "scoring_method", "performance_mean", "performance_std"] + all_params

    for mean, std, params in zip(means, stds, regressor_obj.cv_results_['params']):
        if params['vect__stop_words']: # use a different string instead of printing the entire list
            params['vect__stop_words'] = f"Yes (n={len(params['vect__stop_words'])})"
        
        row = [estimator_name, scoring_method, mean, std] + ['N/A' for p in all_params]

        for p in params:
            idx = all_params.index(p) + 4
            row[idx] = params[p]

        df_rows.append(row)

    df = pd.DataFrame(df_rows, columns=df_colnames)

    out_file_name_base = f"perf_reports/performance_{estimator_name}_{scoring_method}"
    file_n = 0
    #change to walrus operator!
    fn = f"{out_file_name_base}_{file_n}.csv"
    while isfile(fn):
        cprint("Skipping file name: "+fn, "yellow")
        file_n += 1
        fn = f"{out_file_name_base}_{file_n}.csv"

    df.to_csv(fn, index=False)
    cprint("Saved performance report to "+fn, "green", attrs=['bold'])

def clean_text(text):
    stemmer = SnowballStemmer('german')
    pattern = re.compile('[^a-zA-Z0-9äöüÄÖÜß \.]', re.UNICODE)

    text = pattern.sub(' ', text) # remove special characters
    text = ' '.join( [stemmer.stem(word) for word in text.split()] ) # stem words
    return text

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
        {
            'vect__analyzer': ['word'],
            'vect__ngram_range': [(1,i+1) for i in [0,5]],
            'vect__stop_words': [None, stopwords.words('german')],
        }
    ]

    print(f"Tuning hyper-parameters for {score}.")

    # Create a processing pipeline containing preprocessing and the model:
    clf_pipeline = Pipeline([
        #('vect', CountVectorizer(analyzer='char', ngram_range=(2,3))), # count characters
        ('vect', CountVectorizer()), # count terms
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('svr', SVR(cache_size=512)), #SVR
    ])

    # Automatic parameter tuning using grid search:
    cprint("GridSearchCV running...", "yellow")
    regressor = GridSearchCV(
        clf_pipeline, gs_params, scoring=score, n_jobs=-1, verbose=1 #remove cv=2
    )
    regressor.fit(X_train, y_train)

    performance = regressor.score(X_test, y_test)
    cprint(f"R^2 performance for model after hyperparameter tuning using {score}: {performance:.3f}", "green", attrs=['bold'])
    cprint(f"Best parameters set found on development set: \n{regressor.best_params_}\n", "green")

    param_names = []
    for d in gs_params: #d is a dict
        for n in d:
            if n not in param_names:
                param_names.append(n)
    save_performance_report('SVR', regressor, param_names, score)