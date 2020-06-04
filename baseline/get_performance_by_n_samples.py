import pandas as pd
import numpy as np
#from math import ceil
import SGDmodel, SVRmodel
from utilities import test_estimator

input_varid = 22085815
output_varid = 22086158
scoring_methods = ['r2', 'neg_mean_squared_error', 'neg_mean_absolute_error']

max_time_between = 60*60/6 #max 10 min between the text and the score entries

df_all = pd.read_csv("../data/clean/labels_nearest.csv")
df_filter = ((df_all['text_varid'] == input_varid) 
        & (df_all['label_varid'] == output_varid )
        & (df_all['label_time'] - df_all['text_time'] <= max_time_between))
df = df_all[df_filter]
df = df[['text', 'label']]

df['text'] = df['text'].astype('U') #unicode
df['label'] = df['label'].astype(int)

n_total_rows = len(df)
runs_per_x=5
x_vals = np.arange(3500, 5500, 500) #up to 8500

print(n_total_rows)
print(x_vals)
out_df_rows = []
for x in x_vals:
    print(x)
    sample_df = df.sample(n=x)

    score_runs = [] #contains list of 5 dicts, each having tuple values
    for i in range(runs_per_x):
        print(f"{x}-{i+1}/{runs_per_x}...")
        estimator = SVRmodel.get_SVR(use_tuned_hyperparameters=True)
        score_runs.append(test_estimator(estimator, sample_df['text'], sample_df['label'], scoring_methods, n_cv_splits=5))
    
    row = {'x': x}
    for col_name in score_runs[0]:
        row[col_name] = np.mean([r[col_name][0] for r in score_runs])
        row[col_name+'_std'] = np.mean([r[col_name][1] for r in score_runs])
    out_df_rows.append(row) 

out_df = pd.DataFrame(out_df_rows)
out_df.to_csv("svr_perf_by_n_samples_2.csv", index=False)
print(out_df.head())