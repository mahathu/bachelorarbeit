import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from utilities import iprint, sprint, wprint, eprint, save_performance_report, clean_text
from nltk.corpus import stopwords

def search_params_SGD(df, X_col, y_col, score): #https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDRegressor.html
    iprint(f"Tuning hyperparameters for SGDRegressor model using {score}")

    X_train, X_test, y_train, y_test = train_test_split(X_col, y_col, test_size=.2, random_state=1)

    #Use a fixed CountVectorizer because it's expensive to count char ngrams each time:
    iprint("Building character ngram vectorizer...")
    cv = CountVectorizer(analyzer='char', ngram_range=(1,9), stop_words = stopwords.words('german'))
    fixed_params = { #these will be included in the performance report
        'analyzer': 'char', 
        'ngram_range': '(1,9)', 
        'stop_words': 'yes'
    }
    X_train = cv.fit_transform(X_train)
    X_test = cv.transform(X_test)
    #X_{train|test} are now term count matrices with the num. of columns
    sprint("Done!")
    
    input_param_grids = [
        {'tfidf__use_idf': [True, False]}
    ]
    sgd_param_grids = [
        {
            'sgd__loss': ['squared_loss', 'huber'],
            #'sgd__penalty': ['l1', 'l2', 'elasticnet'],
            # 'sgd__alpha': 10.0**(-np.arange(1,7)),
            # 'sgd__learning_rate': ['invscaling', 'constant', 'optimal'],
        }
    ]
    gs_params = [
        {**in_transform, **svr} for svr in sgd_param_grids for in_transform in input_param_grids
    ]

    #vectorizing stage is not part of the pipeline anymore!
    rgr_pipeline = Pipeline([
        #('vect', CountVectorizer()), # count terms or chars
        ('tfidf', TfidfTransformer()), # transform to term freq. inverse document freq.
        ('sgd', SGDRegressor()), #SVR
    ])

    # Automatic parameter tuning using grid search:
    iprint("GridSearchCV running...")
    regressor = GridSearchCV(
        rgr_pipeline, gs_params, scoring=score, n_jobs=-1, verbose=1
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
    save_performance_report('SGDRegression', regressor, param_names, score, fixed_params)

    #move this to the other function    
    y_pred = regressor.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 =  r2_score(y_test, y_pred)

    sprint(f"MSE: {mse:6.3f}")
    sprint(f"MAE: {mae:6.3f}")
    sprint(f"R^2: {r2:6.3f}")
    
    return mse, mae, r2