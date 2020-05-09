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

input_varids = [22085815]
output_varids = [20512801,20512802,20512769,22086169,22086158]
max_time_difference = 60*60*.5 #30 minutes

acc = np.zeros((len(input_varids), len(output_varids)))

df_all = pd.read_csv("../data/clean/labels.csv")
for i, input_varid in enumerate(input_varids):
    for j, output_varid in enumerate(output_varids):
        print(f"Predicting {var_ids[output_varid]} based on {var_ids[input_varid]}")

        filter = ((df_all['text_varid'] == input_varid) 
                & (df_all['label_varid'] == output_varid) 
                & (df_all['label_time'] - df_all['text_time'] <= max_time_difference))

        # remove unwanted rows:
        df = df_all[filter]

        # remove all but the relevant columns:
        df = df[['text', 'label']]
        if output_varid == 22086169: # CAM-ICU
            df = df.replace({'label': {
                'neg.': 0,
                'pos.': 1,
                'unmögl.': 2,
            }})

        df['label'] = df['label'].astype(int) #this will throw an error for CAM-ICU
        
        print(f"Unique labels: {df['label'].unique()}")
        print(f"Total training pairs after filtering: {len(df)}")
        
        score = train_model(df)

        print(f"Accuracy: {score}\n")
        acc[i,j] = score


#plot the matrix:
plt.bar(np.arange(len(output_varids)), [acc[0,j] for j in range(len(output_varids))])
plt.xticks(np.arange(len(output_varids)), [var_ids[vi] for vi in output_varids])

plt.show()
plt.savefig("accuracies.png", bbox_inches='tight', dpi=280)