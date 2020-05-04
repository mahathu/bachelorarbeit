import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def sec_to_label(s):
    td = datetime.timedelta(seconds=s)
    d = td.days
    return f"Tag {d}"
    # h, rem = divmod(td.seconds, 3600)
    # m, s = divmod(rem, 60)
    # return f"{d}d {h:02}h{m:02}m"

input_file = "../data/clean/all_scores.csv"

var_ids = {
    22086067: {"label": "Vigilanz", "color": "lightgrey"},
    22085897: {"label": "Ramsay", "color": "lightgrey"},
    22086170: {"label": "BPS-Bewertung", "color": "lightgrey"},
    20512801: {"label": "BPS", "color": "orange"},
    22086172: {"label": "NRS/VAS Bedingungen", "color": "lightgrey"},
    22085911: {"label": "NRS/VAS", "color": "lightgrey"},
    20512802: {"label": "DDS", "color": "orange"},
    20512769: {"label": "GCS", "color": "orange"},
    22086169: {"label": "CAM-ICU", "color": "orange"},
    22086158: {"label": "RASS", "color": "orange"},
    22085815: {"label": "Visite_ZNS", "color": "blue"},
    22085836: {"label": "Visite_Pflege", "color": "blue"},
    22085820: {"label": "Visite_Oberarzt", "color": "blue"},
}

df = pd.read_csv(input_file)
df = df[ df['VarID'].isin(var_ids) ] # only consider relevant var ids

unique_patient_ids = df['patient'].unique()
print(unique_patient_ids)

for patient_n in unique_patient_ids:
    #patient_n = 12
    print(f"Working on {patient_n}")

    patient_df = df[df['patient'] == patient_n].copy() #explicitly copy dataframe to suppress SettingWithCopyWarning

    #time between first and last event:
    first_event = patient_df['Zeitpkt'].min()
    seconds_in_icu = patient_df['Zeitpkt'].max() - first_event

    patient_df['VarIDIndex'] = patient_df['VarID'].map(lambda vi: list(var_ids.keys()).index(vi) ) # use the index of each var id in the above list to map it on the scatter plot
    patient_df['VarIDColor'] = patient_df['VarID'].apply(lambda vi: var_ids[vi]['color'])
    patient_df['Zeitpkt_offset'] = patient_df['Zeitpkt'] - first_event

    fig, ax = plt.subplots()
    #ax.tick_params(axis='x', which='major', labelsize=9) # set x label size to 9 (slightly smaller)
    plt.scatter(patient_df['Zeitpkt_offset'], patient_df['VarIDIndex'], c=patient_df['VarIDColor'], s=25, marker='+', zorder=2)
    
    n_labels = seconds_in_icu/86400 #86400 seconds in a day --> 1 label per 24h
    xtick_pos = np.arange(0, seconds_in_icu, seconds_in_icu/n_labels)
    xtick_labels = [sec_to_label(s) for s in xtick_pos]
    for xpos in xtick_pos:
        plt.axvline(x=xpos, color='#ededed', linewidth='1', zorder=1)

    plt.xticks(xtick_pos, xtick_labels)
    plt.yticks(range(len(var_ids)), [var_ids[id]['label'] for id in var_ids])
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=-45, ha="left", rotation_mode="anchor")

    plt.title(f"Patient #{patient_n:04} ({datetime.timedelta(seconds=seconds_in_icu)})")
    plt.gcf().set_size_inches(15, 6)

    filename = f'out/patient_{patient_n:04}.png'
    plt.savefig(filename, bbox_inches='tight', dpi=280)
    plt.clf() #clear figure
    print(f"Saved result to {filename}")