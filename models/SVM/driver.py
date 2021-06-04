import pandas as pd
import numpy as np
import SVRmodel
from utilities import iprint, sprint, wprint, eprint, test_estimator, get_x_y, var_ids, clean_and_stem_text
import methods

input_varids = [22085815, 22085836]
output_varids = [22086158, 20512769]


# https://scikit-learn.org/stable/modules/model_evaluation.html
SCORING_METHODS = [
    'r2', 
    'neg_root_mean_squared_error', 
    'neg_mean_absolute_error', 
    # 'neg_median_absolute_error'
]

df_all = pd.read_csv("../../data/clean/labels_nearest_all.csv")
MAX_MIN_BETWEEN_EVENTS = 45


TEST_SET_SIZE = 1000 # same for all!
out_rows = []
sample_sizes = [25,50,100,250,500,750]
sample_sizes.extend([i for i in range(1000, 10000, 1000)])

total_runs = len(input_varids) * len(output_varids) * len(sample_sizes) * N_RUNS_PER_SAMPLE
current_run = 0

for input_varid in input_varids[1:]:
    for output_varid in output_varids:
        for max_samples in sample_sizes:
                # current_run += 1
                # print(f"RUN #{current_run:03}/{total_runs} --- in: {var_ids[input_varid]} out: {var_ids[output_varid]} "
                #         f"max_minutes={MAX_MIN_BETWEEN_EVENTS}, {max_samples} training rows)")        

                X, y = get_x_y(df_all, input_varid, output_varid, 
                    max_min_between=MAX_MIN_BETWEEN_EVENTS, 
                    max_samples=max_samples + TEST_SET_SIZE
                )

                svr = SVRmodel.get_SVR()
                # svr_norass = SVRmodel.get_SVR(True, True)

                scores = test_estimator(svr, X, y, TEST_SET_SIZE, SCORING_METHODS)
                print(f"{scores}\n")
                
                # out_rows.append({
                #     'text': var_ids[input_varid],
                #     'predict': var_ids[output_varid],
                #     #'max_min_between': MAX_MIN_BETWEEN_EVENTS,
                #     'max_samples': max_samples,
                #     #'filter_rass': filter_rass,
                #     'fit_time': scores['fit_time'][0],
                #     'mae': -scores['neg_mean_absolute_error'][0],
                #     'rmse': -scores['neg_root_mean_squared_error'][0],
                #     'r2': scores['r2'][0],
                # })

df = pd.DataFrame(out_rows)
df.to_csv('SVM_performance_test_1000.csv', index=False)