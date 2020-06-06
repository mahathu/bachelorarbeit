import pandas as pd
import numpy as np
import SVRmodel, SGDmodel
from utilities import iprint, sprint, wprint, eprint, test_estimator, get_x_y, var_ids
import methods

input_varids = [22085815, 22085836][:1]
output_varids = [22086158, 20512769][:1]

scoring_methods = ['r2', 'neg_mean_squared_error', 'neg_mean_absolute_error'] # scores to test the models with (https://scikit-learn.org/stable/modules/model_evaluation.html)

max_time_between_events=60*60/3
max_samples=0

df_all = pd.read_csv("../data/clean/labels_nearest.csv")

#this is mostly used for some more data cleaning before passing it to the models.
for input_varid in input_varids:
    for output_varid in output_varids:
        X,y = get_x_y(df_all, input_varid, output_varid, max_time_between=max_time_between_events, max_samples=max_samples)
       
        unique_labels = np.sort(y.unique())
        sprint(f"INPUT: {var_ids[input_varid]} OUTPUT: {var_ids[output_varid]} "
                f"({len(unique_labels)} unique labels, "
                f"max_minutes={int(max_time_between_events/60)}, {len(X)} total rows)")
        print(f"Labels: {unique_labels}")

        model = SGDmodel.get_SGD(use_tuned_hyperparameters=True)
        methods.make_predictions(X,y, var_ids[input_varid], var_ids[output_varid], model, n_preds=200)

        # estimators = [
        #     [SVRmodel.get_SVR(use_tuned_hyperparameters=False), False],
        #     [SVRmodel.get_SVR(use_tuned_hyperparameters=True), True],
        #     [SGDmodel.get_SGD(use_tuned_hyperparameters=False), False],
        #     [SGDmodel.get_SGD(use_tuned_hyperparameters=True), True],
        # ]
        # methods.test_estimators(X, y, estimators, scoring_methods)