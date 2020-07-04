import pandas as pd
import numpy as np

df = pd.read_csv('../ELM/performance.csv')

parameter_names = ['dimensions', 'word_min_count', 'window_size', 'svr_C']

for parameter in parameter_names:
    unique_vals = df[parameter].unique()
    print(f"=== {parameter} ===")
    for val in unique_vals:
        print(f"> {parameter}={val}")
        vals = df[df[parameter] == val]['MAE']

        #print(f"mean: {np.mean(vals):.3f}")
        print(f"best: {np.min(vals):.3f}")
    print()