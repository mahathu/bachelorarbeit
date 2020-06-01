import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import search_params_SVR
from datetime import datetime

var_ids = {
    22086067: "Vigilanz",
    22085897: "Ramsay",
    22086170: "BPS-Bewertung",
    20512801: "BPS",
    22086172: "NRS/VAS Bedingungen",
    22085911: "NRS/VAS",
    20512802: "DDS",
    20512769: "GCS",
    22086169: "CAM-ICU",
    22086158: "RASS",
    22085815: "Visite_ZNS",
    22085836: "Visite_Pflege",
    22085820: "Visite_Oberarzt",
}

input_varids = [22085815, 22085836][:1]
output_varids = [22086158, 20512769][:1]

scores_regression = ['r2', 'neg_mean_squared_error'] # scores to test the models with (https://scikit-learn.org/stable/modules/model_evaluation.html)
scores_classification = []

max_time_between = 60*60/3 #20 minutes

note = ""

df_all = pd.read_csv("../data/clean/labels_nearest.csv", nrows=100)
perf_rows = []

for i, input_varid in enumerate(input_varids):
    for j, output_varid in enumerate(output_varids):
        filter = ((df_all['text_varid'] == input_varid) 
                & (df_all['label_varid'] == output_varid) 
                & (df_all['label_time'] - df_all['text_time'] <= max_time_between))

        # remove unwanted rows:
        df = df_all[filter]

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
        
        print(f"INPUT: {var_ids[input_varid]} OUTPUT: {var_ids[output_varid]} "
                f"({len(df['label'].unique())} unique labels, "
                f"max_min={int(max_time_between/60)}, {len(df)} total rows)")
        
        search_params_SVR(df=df, X_col=df['text'], y_col=df['label'], score=scores_regression[0])

        # acc = 1
        # row = [var_ids[input_varid], var_ids[output_varid], max_time_between, len(df), acc, note]
        # perf_rows.append(row)

# perf_df = pd.DataFrame(perf_rows, columns=['label_varid', 'predict_varid', 'max_time_between', 'n_samples', 'r2', 'note'])
# perf_df.to_csv(f"baseline_model_performance_{datetime.now().strftime('%Y-%m-%d %H_%M')}.csv", index=False)