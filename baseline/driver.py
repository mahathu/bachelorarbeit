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

df_all = pd.read_csv("../data/clean/labels_nearest_all.csv")
MAX_MIN_BETWEEN_EVENTS = 45
#this is mostly used for some more data cleaning before passing it to the models.
out_rows = []
for input_varid in input_varids:
    for output_varid in output_varids:
            for i in range(10):
                X, y = get_x_y(df_all, input_varid, output_varid, max_min_between=MAX_MIN_BETWEEN_EVENTS, max_samples=7500)

                unique_labels = np.sort(y.unique())
                wprint('*'*80)
                sprint(f"INPUT: {var_ids[input_varid]} OUTPUT: {var_ids[output_varid]} "
                        f"({len(unique_labels)} unique labels, "
                        f"max_minutes={MAX_MIN_BETWEEN_EVENTS}, {len(X)} total rows)")
                # print(f"Labels: {unique_labels}")
            


                print(f"Gucke nur auf erste 5 Zeichen")
                svr = SVRmodel.get_SVR(True, True)

                scores = test_estimator(svr, X, y, 'neg_mean_absolute_error')
                for s in scores:
                    print(f"{s} : {scores[s][0]:.5f}")
                
                wprint("******************************")