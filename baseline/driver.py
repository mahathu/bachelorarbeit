import pandas as pd
import numpy as np
import SVRmodel, SGDmodel
from utilities import iprint, sprint, wprint, eprint, test_estimator, get_x_y, var_ids, clean_and_stem_text
import methods

input_varids = [22085815, 22085836][:1]
output_varids = [22086158, 20512769][:1]

# https://scikit-learn.org/stable/modules/model_evaluation.html
SCORING_METHODS = [
    'r2', 
    'neg_root_mean_squared_error', 
    'neg_mean_absolute_error', 
    'neg_median_absolute_error'
]

MAX_MIN_BETWEEN_EVENTS = 30 #still have > 5k rows per varid pair
df_all = pd.read_csv("../data/clean/labels_nearest_all.csv")

out_rows = []
n_samples_arr = np.concatenate([np.arange(100,1000,100), np.arange(1000,8000,500)]) #100-7500
#this is mostly used for some more data cleaning before passing it to the models.
for input_varid in input_varids:
    for output_varid in output_varids:
        for n_samples in n_samples_arr:
            X, y = get_x_y(df_all, input_varid, output_varid, max_min_between=MAX_MIN_BETWEEN_EVENTS, max_samples=0)
            # unique_labels = np.sort(y.unique())
            # wprint('*'*80)
            # sprint(f"INPUT: {var_ids[input_varid]} OUTPUT: {var_ids[output_varid]} "
            #         f"({len(unique_labels)} unique labels, "
            #         f"max_minutes={MAX_MIN_BETWEEN_EVENTS}, {len(X)} total rows)")
            # print(f"Labels: {unique_labels}")
            
            # Calculate performance on tuned models by number of samples:
            wprint(f"{var_ids[input_varid]} --> {var_ids[output_varid]} n={n_samples}")
            for estimator, estimator_name in zip([SGDmodel.get_SGD(), SVRmodel.get_SVR()], ['SGDRegressor', 'SVR']):
                print(f"{estimator_name}...")

                row = methods.get_performance_by_n_samples(X, y, estimator, n_samples)
                row['max_minutes_between_events'] = MAX_MIN_BETWEEN_EVENTS
                row['estimator'] = estimator_name
                row['n_samples'] = n_samples
                row['input_varid'] = var_ids[input_varid]
                row['output_varid'] = var_ids[output_varid]
                out_rows.append(row)
                sprint("Done!")

            # Predicting some sample data:
            # model = SVRmodel.get_SVR(use_tuned_hyperparameters=True)
            # methods.make_predictions(X,y, var_ids[input_varid], var_ids[output_varid], model, n_preds=50, n_total_samples=500)
            #selbst mit nur 1000 samples erreichen wir MAE von <1 ????

df = pd.DataFrame(out_rows)
df.to_csv(f'performances_max_{MAX_MIN_BETWEEN_EVENTS}min_rassonly.csv', index=False)
print(df.head())
