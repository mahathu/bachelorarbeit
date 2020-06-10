import numpy as np
import pandas as pd
import SVRmodel, SGDmodel
from utilities import iprint, sprint, wprint, eprint, test_estimator, var_ids, safe_filename

def test_estimators(X, y, estimators, scoring_methods):# Test baseline models and print results
    max_score_len = max([len(s) for s in scoring_methods])

    for a in estimators:
        estimator = a[0]
        estimator_name = type(estimator[-1]).__name__
        
        iprint("\n{1} performance ({0} hyperparameter tuning):".format("with" if a[1] else "no", estimator_name))

        mean_scores = test_estimator(estimator, X, y, scoring_methods)

        for scoring_method, v in mean_scores.items():
            # if scoring_method in ['score_time', 'fit_time']: #skip these, but maybe useful later
            #     continue

            mean = v[0]
            std = v[1]
            if scoring_method.startswith("neg_"):
                scoring_method = scoring_method[4:]
                mean = mean*-1

            print("{0:>{1}}: {2:6.3f} (+/- {3:5.3f})".format(scoring_method, max_score_len, mean, std*2))

def make_predictions(X, y, X_name, y_name, estimator, n_preds, n_total_samples=-1, verbose=True): # get some sample output from the model
    if n_total_samples > -1:
        X = X.sample(n_total_samples)
        y = y[X.index]

    X_test, y_test = X.iloc[:n_preds], y.iloc[:n_preds]
    X_train, y_train = X.iloc[n_preds:], y.iloc[n_preds:]

    estimator.fit(X_train, y_train)
    preds = estimator.predict(X_test)

    mae = np.mean(np.abs(y_test-preds))

    out_df = pd.DataFrame({
        X_name: X_test, 
        "actual_"+y_name: y_test, 
        "predicted_"+y_name: preds.round().astype(int),
    })
    
    #fn = safe_filename(f"preds/preds-SVR-{X_name}-{y_name}", "csv")
    #out_df.to_csv(fn, index=False)

    if verbose:
        iprint(f"Number of pairs used for prediction: {X.shape[0]}")
        sprint(f"mae={mae}")
        print(out_df.head())
    return mae

def get_performance_by_n_samples(X, y, estimator, n_samples):
    scoring_methods = [
        #'neg_root_mean_squared_error', 
        'neg_mean_absolute_error', 
        #'neg_median_absolute_error'
    ]
    n_runs = 10

    X = X.sample(n_samples)
    y = y[X.index]

    score_runs = [] #contains list of 5 dicts, each having tuple values
    for i in range(n_runs):
        score_runs.append(test_estimator(estimator, X, y, scoring_methods, n_cv_splits=5))
        #test_estimator returns mean and std for the given scoring methods and fit times
    
    row = {}
    for col_name in score_runs[0]:
        row[col_name] = np.mean([r[col_name][0] for r in score_runs])
        row[col_name+'_std'] = np.mean([r[col_name][1] for r in score_runs])

    return row