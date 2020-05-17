import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import train_model

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

input_varids = [22085836, 22085815]
output_varids = [22086158, 22086169, 20512769]
max_time_difference = 60*60*.5 #30 minutes

acc = np.zeros((len(input_varids), len(output_varids)))

df_all = pd.read_csv("../data/clean/labels.csv")
for i, input_varid in enumerate(input_varids):
    for j, output_varid in enumerate(output_varids):
        filter = ((df_all['text_varid'] == input_varid) 
                & (df_all['label_varid'] == output_varid) 
                & (df_all['label_time'] - df_all['text_time'] <= max_time_difference))

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
        
        print(f"Predicting {var_ids[output_varid]} based on {var_ids[input_varid]}\n"
              f"Unique labels: {df['label'].unique()} ({len(df['label'].unique())} in total)\n"
              f"Total training pairs after filtering: {len(df)}")

        score = train_model(df)
        
        print(f"=== Accuracy: {score} ===\n")
        acc[i,j] = score
