'''
Desired output: a dataframe with columns:

patientID, patientAge, patientSex, patientICUDuration, patientDied, eventTime
VarID (eigene Spalte für jede varID?)
'''

import os
import pandas as pd

input_path = "data/"
output_path = os.path.join(input_path, 'clean')


scores1 = pd.read_csv(os.path.join(input_path, "scores1.csv"), sep=';')
scores2 = pd.read_csv(os.path.join(input_path, "scores2.csv"), sep=';', encoding="latin1")

var_ids_dict = pd.read_excel(os.path.join(input_path, "VarIDs.xlsx")).to_dict()
var_ids = {}
for i in var_ids_dict['VarID']:
    var_ids[var_ids_dict['VarID'][i]] = var_ids_dict['Inhalt'][i]

scores1.rename({'Gesamtscore': 'wert'}, axis=1, inplace=True)
scores2.rename({'vString': 'wert'}, axis=1, inplace=True)

scores = pd.concat([scores1, scores2])
scores.rename({"n_ID": "patient"}, axis=1, inplace=True)
scores.sort_values(by=['patient', 'Zeitpkt'], inplace=True)
scores['name'] = scores['VarID'].apply(lambda v: var_ids[v])

print(scores.head())
scores.to_csv(os.path.join(output_path, "all_scores.csv"))