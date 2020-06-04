import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from utilities import iprint, sprint, wprint, eprint, save_performance_report, clean_text
from nltk.corpus import stopwords

def search_params_Lasso(X_col, y_col, score):
    iprint(f"Tuning hyperparameters for Lasso model using {score}")

    X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=.2, random_state=1)

    fixed_params = { #these will be included in the performance report
        'analyzer': 'char', 
        'ngram_range': '(1,9)', 
        'stop_words': 'yes'
    }
    
    input_param_grids = [
        {'tfidf__use_idf': [True]} # doesn't seem to affect performance much at all
    ]
    lasso_param_grids = [
        {
            'lasso__alpha': [.01, .1, 1, 10, 100],
            'lasso__tol': [.00001, .0001, .001, .01]
        }
    ]
    gs_params = [
        {**in_transform, **lparams} for lparams in lasso_param_grids for in_transform in input_param_grids
    ]

    #vectorizing stage is not part of the pipeline anymore!
    rgr_pipeline = Pipeline([
        ('vect', CountVectorizer(analyzer='char', ngram_range=(1,9), stop_words = stopwords.words('german'))), # count chars
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('lasso', Lasso()),
    ])

    # Automatic parameter tuning using grid search:
    iprint("GridSearchCV running...")
    regressor = GridSearchCV(
        rgr_pipeline, gs_params, scoring=score, n_jobs=-1, verbose=2
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
    
    save_performance_report('Lasso', regressor, param_names, score, fixed_params)

def get_Lasso(use_tuned_hyperparameters=True):
    if use_tuned_hyperparameters: # Create a processing pipeline with the best hyperparameters:
        rgr_pipeline = Pipeline([
            ('vect', CountVectorizer(analyzer='char', ngram_range=(1,9), stop_words = stopwords.words('german'))),
            ('tfidf', TfidfTransformer(use_idf=True)), # transform to term freq. inverse document freq.
            ('lasso', Lasso(
                alpha=0.01,
                tol=1e-05
            )),
        ])

    else: # use a standard Lasso
        rgr_pipeline = Pipeline([
            ('vect', CountVectorizer(analyzer='char', ngram_range=(1,9), stop_words = stopwords.words('german'))),
            ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
            ('lasso', Lasso()),
        ])
    
    return rgr_pipeline
