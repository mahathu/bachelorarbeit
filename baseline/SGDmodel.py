import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from utilities import iprint, sprint, wprint, eprint, save_performance_report, clean_and_stem_text, brief_dict
from nltk.corpus import stopwords

def search_params_SGD(X_col, y_col, scoring_method, save_perf_report=True ,gs_params=None): #https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html
    X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=.2)
    
    if gs_params:
        wprint(f"Using the following gs_params: {gs_params}")
    else:
        wprint(f"gs_params set by function")
        input_param_grids = [
            {
                'vect__analyzer': ['char', 'char_wb'],
                'vect__ngram_range': [(1,3), (1,5), (1,9), (2,6), (3,7), (4,9)],
                'vect__preprocessor': [None, clean_and_stem_text],
            },
        ]
        sgd_param_grids = [
            {
                'sgd__loss': ['huber', 'squared_loss'],
                'sgd__penalty': ['l1', 'l2'],
                'sgd__alpha': [1e-06, 1e-05, 0.0001, 0.001, 0.01] # 0.0001 = 1e-4 is default
            }
        ]
        gs_params = [
            {**in_transform, **svr} for svr in sgd_param_grids for in_transform in input_param_grids
        ]

    rgr_pipeline = Pipeline([
        ('vect', CountVectorizer()), # count terms or chars
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('sgd', SGDRegressor()),
    ])

    # Automatic parameter tuning using grid search:
    iprint(f"GridSearchCV running for SGDRegressor perf_metric: {scoring_method}...")
    regressor = GridSearchCV(
        rgr_pipeline, gs_params, scoring=scoring_method, n_jobs=-1, verbose=0
    )

    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    best_params = brief_dict(regressor.best_params_)

    sprint(f"Best parameters set found on development set: \n{best_params}\n")

    scores = {
        "mae": mean_absolute_error(y_test, y_pred),
        "rmse": np.sqrt(mean_squared_error(y_test, y_pred)),
        "r2": regressor.score(X_test, y_test),
    }

    sprint(f"Performance for model after hyperparameter tuning using {scoring_method}:")
    for s in scores:
        print(f"{s:>4}: {scores[s]:.3f}")

    if not save_perf_report:
        return scores["mae"]

    param_names = []
    for d in gs_params: #d is a dict
        for n in d:
            if n not in param_names:
                param_names.append(n)
    save_performance_report('SGDRegression', regressor, param_names, scoring_method, len(X_col))

def get_SGD(use_tuned_hyperparameters=True):
    cv = CountVectorizer(
        analyzer='char',
        ngram_range=(2,6),
    )

    if use_tuned_hyperparameters: # Create a processing pipeline with the best hyperparameters:
        return Pipeline([
            ('vect', cv),
            ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
            ('sgd', SGDRegressor(
                loss='squared_loss',
                penalty='l2',
                alpha=1e-07,
                max_iter=15000
            )),
        ])

    # use a standard SGD Regressor
    return Pipeline([
        ('vect', cv),
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('sgd', SGDRegressor()),
    ])