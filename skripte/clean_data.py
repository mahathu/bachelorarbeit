import os
import pandas as pd

def remove_linebreaks(str):
    return str.replace('\n', ' ').replace('\r', '')

input_path = "../data/"
output_path = os.path.join(input_path, 'clean/all_scores.csv')

print("Reading input files...")
scores1 = pd.read_csv(os.path.join(input_path, "scores1.csv"), sep=';') #GCS, DDS, BPS
scores2 = pd.read_excel(os.path.join(input_path, "scores2.xlsx")) #alle anderen Scores/Inputs

# var_ids_dict = pd.read_excel(os.path.join(input_path, "VarIDs.xlsx")).to_dict()
# var_ids = {}
# for i in var_ids_dict['VarID']:
#     var_ids[var_ids_dict['VarID'][i]] = var_ids_dict['Inhalt'][i]

scores1.rename({'Gesamtscore': 'wert'}, axis=1, inplace=True)

print("Removing linebreaks from long strings...")
scores2['vString'] = scores2['vString'].astype(str).apply(remove_linebreaks)
scores2.rename({'vString': 'wert'}, axis=1, inplace=True)

print("Concatenating files...")
scores = pd.concat([scores1, scores2]) #Zusammenfügen der beiden Tabellen

scores.rename({"n_ID": "patient"}, axis=1, inplace=True)
print("Sorting values...")
scores.sort_values(by=['patient', 'Zeitpkt'], inplace=True)
#scores['name'] = scores['VarID'].apply(lambda v: var_ids[v])

print(scores.head())
scores.to_csv(output_path, index=False)
print("Saved output to {}".format(output_path))