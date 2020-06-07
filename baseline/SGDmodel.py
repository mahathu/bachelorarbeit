import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from utilities import iprint, sprint, wprint, eprint, save_performance_report, clean_text
from nltk.corpus import stopwords


def search_params_SGD(X_col, y_col, scoring_method): #https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html
    X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=.2, random_state=1)

    # cv = CountVectorizer(analyzer='char', ngram_range=(1,9), stop_words = stopwords.words('german'))
    # X_train = cv.fit_transform(X_train)
    # X_test = cv.transform(X_test)
    # X_{train|test} are now term count matrices with the num. of columns
    
    input_param_grids = [
        {
            #'vect__analyzer': ['char', 'char_wb'],
            #'vect__preprocessor': [None, clean_text], #clean_text contains removing special chars and stemming
            'vect__ngram_range': [(3,9)]#[(1,3)], (1,6), (1,9), (3,3), (3,6), (3,9), (5,9), (5,12)],
            #'vect__stop_words': [[], stopwords.words('german')],
            #'tfidf__use_idf': [True, False],
        }
    ]
    sgd_param_grids = [
        {
            'sgd__loss': ['squared_loss'],
            'sgd__penalty': ['l2'],
            'sgd__alpha': [0.0001],
            'sgd__learning_rate': ['optimal'],
        }
    ]
    gs_params = [
        {**in_transform, **svr} for svr in sgd_param_grids for in_transform in input_param_grids
    ]

    rgr_pipeline = Pipeline([
        ('vect', CountVectorizer()), # count terms or chars
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('sgd', SGDRegressor(max_iter=7500)),
    ])

    # Automatic parameter tuning using grid search:
    iprint(f"GridSearchCV running for SGDRegressor perf_metric: {scoring_method}...")
    regressor = GridSearchCV(
        rgr_pipeline, gs_params, scoring=scoring_method, n_jobs=-1, verbose=1
    )

    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)

    sprint(f"Best parameters set found on development set: \n{regressor.best_params_}\n")

    scores = {
        "mae": mean_absolute_error(y_test, y_pred),
        "rmse": np.sqrt(mean_squared_error(y_test, y_pred)),
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
    #save_performance_report('SGDRegression', regressor, param_names, scoring_method)

def get_SGD(use_tuned_hyperparameters=True):
    cv = CountVectorizer(
        analyzer='char',
        ngram_range=(1,9),
        stop_words=stopwords.words('german'),
    )

    if use_tuned_hyperparameters: # Create a processing pipeline with the best hyperparameters:
        return Pipeline([
            ('vect', cv),
            ('tfidf', TfidfTransformer(use_idf=False)), # transform to term freq. inverse document freq.
            ('sgd', SGDRegressor(
                loss='squared_loss',
                penalty='l2',
                alpha=0.0001,
                learning_rate='constant'
            )),
        ])

    # use a standard SGD Regressor
    return Pipeline([
        ('vect', cv),
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('sgd', SGDRegressor()),
    ])