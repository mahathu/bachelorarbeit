import pandas as pd
import numpy as np
import SVRmodel, SGDmodel
from utilities import iprint, sprint, wprint, eprint, test_estimator, get_x_y, var_ids
import methods

input_varids = [22085815, 22085836][:1]
output_varids = [22086158, 20512769][:1]

# https://scikit-learn.org/stable/modules/model_evaluation.html
SCORING_METHODS = ['r2', 'neg_root_mean_squared_error', 'neg_mean_absolute_error', 'neg_median_absolute_error']
MAX_SEC_BETWEEN_EVENTS = 60*60/90
MAX_SAMPLES = 4000
MAX_SAMPLES = 0
df_all = pd.read_csv("../data/clean/labels_nearest_all.csv")
eprint(f"total lines read: {len(df_all)}")

#this is mostly used for some more data cleaning before passing it to the models.
for input_varid in input_varids:
    for output_varid in output_varids:
        X,y = get_x_y(df_all, input_varid, output_varid, max_time_between=MAX_SEC_BETWEEN_EVENTS, max_samples=MAX_SAMPLES)
       
        unique_labels = np.sort(y.unique())
        sprint(f"INPUT: {var_ids[input_varid]} OUTPUT: {var_ids[output_varid]} "
                f"({len(unique_labels)} unique labels, "
                f"max_minutes={int(MAX_SEC_BETWEEN_EVENTS/60)}, {len(X)} total rows)")
        print(f"Labels: {unique_labels}")

        continue

        #TODO: compare GSCV results when tuning for different hyperparameters!
        SGDmodel.search_params_SGD(X, y, 'r2')
        
        # Predicting some sample data:
        #model = SGDmodel.get_SGD(use_tuned_hyperparameters=True)
        #methods.make_predictions(X,y, var_ids[input_varid], var_ids[output_varid], model, n_preds=200)

        # Comparing estimator performance using cross validation:
        estimators = [
            [SGDmodel.get_SGD(use_tuned_hyperparameters=True), True],
            [SVRmodel.get_SVR(use_tuned_hyperparameters=True), True],
        ]
        #methods.test_estimators(X, y, estimators, SCORING_METHODS)