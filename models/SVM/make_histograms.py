import pandas as pd
import numpy as np
import SVRmodel
from utilities import iprint, sprint, wprint, eprint, test_estimator, get_x_y, var_ids, clean_and_stem_text
import methods
import os, pickle

input_varids = 22085815
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

model_path = 'baked_models/'

xvals = []
yvals = []
ypreds = []

n = 1000

with open(os.path.join(model_path, 'svr-22085815-20512769.est'), 'rb') as f: #GCS
    model_ZNS_GCS = pickle.load(f)
    X, y = get_x_y(df_all, 22085815, 20512769, 
        max_min_between=MAX_MIN_BETWEEN_EVENTS, 
        max_samples=n
    )

    xvals.extend(X)
    yvals.extend(y)
    ypreds.extend([
        min(
            max(round(yval), min(y)),
            max(y)
        ) for yval in model_ZNS_GCS.predict(X)
    ])

with open(os.path.join(model_path, 'svr-22085815-22086158.est'), 'rb') as f: #RASS
    model_ZNS_RASS = pickle.load(f)
    X, y = get_x_y(df_all, 22085815, 22086158, 
        max_min_between=MAX_MIN_BETWEEN_EVENTS, 
        max_samples=n
    )

    xvals.extend(X)
    yvals.extend(y)
    ypreds.extend([
        min(
            max(round(yval), min(y)),
            max(y)
        ) for yval in model_ZNS_RASS.predict(X)
    ])

df = pd.DataFrame({
    'out_varid': ['GCS'] * n + ['RASS'] * n,
    'x': xvals,
    'y': yvals,
    'ypred': ypreds,
})
df.to_csv('hist_performance.csv', index=False)