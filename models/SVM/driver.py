import pandas as pd
import numpy as np
import SVRmodel
from utilities import iprint, sprint, wprint, eprint, test_estimator, get_x_y, var_ids, clean_and_stem_text
import methods

input_varids = [22085815, 22085836]
output_varids = [22086158, 20512769]


# https://scikit-learn.org/stable/modules/model_evaluation.html
SCORING_METHODS = [
    # 'r2', 
    # 'neg_root_mean_squared_error', 
    'neg_mean_absolute_error', 
    # 'neg_median_absolute_error'
]

df_all = pd.read_csv("../../data/clean/labels_nearest_all.csv")
MAX_MIN_BETWEEN_EVENTS = 45
N_SAMPLES_PER_RUN = 10
N_SAMPLES_PER_RUN_ALT = 3

out_rows = []
sample_sizes = [50,100,250,500,750,1000,2500, 5000, 7500]

for input_varid in input_varids:
    for output_varid in output_varids:
        for max_samples in sample_sizes:
            for filter_rass in [False]:
                
                out_row = {
                    'text': var_ids[input_varid],
                    'predict': var_ids[output_varid],
                    'max_min_between': MAX_MIN_BETWEEN_EVENTS,
                    'max_samples': max_samples,
                    'filter_rass': filter_rass,
                    'mean_fit_time': 0,
                    'mean_MAE': 0,
                }
            
                # print(f"Labels: {unique_labels}")
                
                for i in range(N_SAMPLES_PER_RUN):
                    X, y = get_x_y(df_all, input_varid, output_varid, max_min_between=MAX_MIN_BETWEEN_EVENTS, max_samples=max_samples)

                    unique_labels = np.sort(y.unique())
                    wprint('*'*80)
                    sprint(f"INPUT: {var_ids[input_varid]} OUTPUT: {var_ids[output_varid]} "
                            f"({len(unique_labels)} unique labels, "
                            f"max_minutes={MAX_MIN_BETWEEN_EVENTS}, {len(X)} total rows)")

                    svr = SVRmodel.get_SVR(True, False)
                    # svr_norass = SVRmodel.get_SVR(True, True)

                    scores = test_estimator(svr, X, y, SCORING_METHODS)
                    print(scores)
                    
                    out_row['mean_fit_time'] += scores['fit_time'][0]
                    out_row['mean_MAE'] -= scores['neg_mean_absolute_error'][0]
                
                out_row['mean_fit_time'] = out_row['mean_fit_time']/n
                out_row['mean_MAE'] = out_row['mean_MAE']/n
                out_rows.append(out_row)

df = pd.DataFrame(out_rows)
df.to_csv('scores.csv', index=False)

#out csv: in_varid, out_varid, max_samples, rass_filtered, fit_time, neg_mean_absolute_error