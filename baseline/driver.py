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

minute_window = 20 #10 minute window
min_min_arr = np.arange(0,110,minute_window/2)
df_all = pd.read_csv("../data/clean/labels_nearest_all.csv")

#this is mostly used for some more data cleaning before passing it to the models.
out_rows = []
for input_varid in input_varids:
    for output_varid in output_varids:
        for min_min in min_min_arr:
            max_min = min_min+minute_window
            X, y = get_x_y(df_all, input_varid, output_varid, max_min_between=max_min, min_min_between=min_min, max_samples=0)

            # unique_labels = np.sort(y.unique())
            # wprint('*'*80)
            # sprint(f"INPUT: {var_ids[input_varid]} OUTPUT: {var_ids[output_varid]} "
            #         f"({len(unique_labels)} unique labels, "
            #         f"max_minutes={MAX_MIN_BETWEEN_EVENTS}, {len(X)} total rows)")
            # print(f"Labels: {unique_labels}")
            
            # Calculate performance of tuned models by max offset:
            sprint(f"min: {min_min} max: {max_min} n samples: {len(X)}")
            
            #get a random sample:
            mae = 0
            mae_std = 0
            for i in range(3):
                X = X.sample(1167)
                y = y[X.index]
                perf = methods.get_performance_from_sample(X, y, SVRmodel.get_SVR(use_tuned_hyperparameters=True))
                mae -= 1/3 * perf['neg_mean_absolute_error']
                mae_std += 1/3 * perf['neg_mean_absolute_error_std']
                print('.', end='', flush=True)
            
            print(f"\n{mae}")
            out_rows.append({
                "min": min_min,
                "max": max_min,
                "mae": mae,
                "std": mae_std,
            })

df = pd.DataFrame(out_rows)
df.head()
df.to_csv("performance_by_min_offset.csv", index=False)