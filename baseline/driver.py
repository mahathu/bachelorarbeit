import pandas as pd
import numpy as np
import SVRmodel, SGDmodel, Lassomodel
from utilities import iprint, sprint, wprint, eprint, test_estimator, var_ids

MAX_SAMPLES = 0 # maximum n of training pairs. Should only be used to speed up testing

input_varids = [22085815, 22085836]
output_varids = [22086158, 20512769]

scores_regression = ['r2', 'neg_mean_squared_error', 'neg_mean_absolute_error'] # scores to test the models with (https://scikit-learn.org/stable/modules/model_evaluation.html)
scores_classification = []
scores_max_len = max([len(s) for s in scores_regression+scores_classification])

max_time_between = 60*60/2 #30 minutes

df_all = pd.read_csv("../data/clean/labels_nearest.csv")

for i, input_varid in enumerate(input_varids):
    for j, output_varid in enumerate(output_varids):
        df_filter = ((df_all['text_varid'] == input_varid) 
                & (df_all['label_varid'] == output_varid) 
                & (df_all['label_time'] - df_all['text_time'] <= max_time_between))

        # remove unwanted rows:
        df = df_all[df_filter]

        if MAX_SAMPLES>0:
            df = df[:MAX_SAMPLES]
            eprint(f"Only considering the first {MAX_SAMPLES} samples!")

        # remove irrelevant columns:
        df = df[['text', 'label']]
        if output_varid == 22086169: # CAM-ICU
            df = df.replace({'label': {
                'neg.': 0,
                'pos.': 1,
                'unmögl.': 2,
            }})

        df['text'] = df['text'].astype('U') #unicode
        df['label'] = df['label'].astype(int)
        
        unique_labels = np.sort(df['label'].unique())
        sprint(f"INPUT: {var_ids[input_varid]} OUTPUT: {var_ids[output_varid]} "
                f"({len(unique_labels)} unique labels, "
                f"max_minutes={int(max_time_between/60)}, {len(df)} total rows)")
        print(f"Labels: {unique_labels}")

        #SVRmodel.search_params_SVR(X_col=df['text'], y_col=df['label'], score=scores_regression[0])
        #SVRmodel.test_SVR(df['text'], df['label'])

        # Test all baseline models:
        estimators = [
            [SVRmodel.get_SVR(use_tuned_hyperparameters=False), False],
            [SVRmodel.get_SVR(use_tuned_hyperparameters=True), True],
            [SGDmodel.get_SGD(use_tuned_hyperparameters=False), False],
            [SGDmodel.get_SGD(use_tuned_hyperparameters=True), True],
            # [Lassomodel.get_Lasso(use_tuned_hyperparameters=False), False],
            # [Lassomodel.get_Lasso(use_tuned_hyperparameters=True), True],
        ]

        for a in estimators:
            estimator = a[0]
            estimator_name = type(estimator[-1]).__name__
            
            iprint("\n{1} performance ({0} hyperparameter tuning):".format("with" if a[1] else "no", estimator_name))

            mean_scores = test_estimator(estimator, df['text'], df['label'], scores_regression)
            

            for scoring_method, v in mean_scores.items():
                if scoring_method in ['score_time', 'fit_time']: #skip these, but maybe useful later
                    continue

                mean = v[0]
                std = v[1]
                if scoring_method.startswith("neg_"):
                    scoring_method = scoring_method[4:]
                    mean = mean*-1

                print("{0:>{1}}: {2:6.3f} (+/- {3:5.3f})".format(scoring_method, scores_max_len, mean, std*2))