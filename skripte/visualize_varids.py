import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

input_file = "../data/clean/all_scores.csv"

relevant_varids = [
    # 20512802, # DDS
    # 20512769, # GCS
    # 20512801, # BPS
    22085815, # Visite_ZNS
    22085836, # Visite_Pflege
    22085820, # Visite_Oberarzt
    # 22085897, # Ramsay
    # 22086169, # CAM-ICU
    22086158, # RASS
    22086067, # Vigilanz
    22086170, # BPS-Bewertung
    # 22085911, # NRS/VAS
    # 22086172, # NRS/VAS Bedingungen
]

df = pd.read_csv(input_file)
df = df[ df['VarID'].isin(relevant_varids) ] # only consider relevant varids
df['VarIDIndex'] = df['VarID'].apply(lambda vi: relevant_varids.index(vi) ) # use the index of each var id in the above list to map it on the scatter plot

patient_n = 4
patient_df = df[df['patient'] == patient_n]

labels = list(patient_df['VarID'].unique())

fig, ax = plt.subplots()
plt.scatter(patient_df['Zeitpkt'], patient_df['VarIDIndex'], c=patient_df['VarIDIndex'])
#ax.legend()
plt.show()