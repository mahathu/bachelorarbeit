import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import timedelta

input_file = "../data/clean/all_scores.csv"
out_file_name = "labels.csv"

MARKER_COLOR_DEFAULT = 'lightgrey'
MARKER_COLOR_LABEL = 'orange'
MARKER_COLOR_TEXT = 'blue'

PREDICTION_MAX_DISTANCE = 60*60*2 #2 hours

total_data_pairs = 0
training_pairs = [] #2d array, containing one text and label per row (+metadata)

var_ids = {
    22086067: {"label": "Vigilanz"},
    22085897: {"label": "Ramsay"},
    22086170: {"label": "BPS-Bewertung"},
    20512801: {"label": "BPS"},
    22086172: {"label": "NRS/VAS Bedingungen"},
    22085911: {"label": "NRS/VAS"},
    20512802: {"label": "DDS"},
    20512769: {"label": "GCS"},
    22086169: {"label": "CAM-ICU"},
    22086158: {"label": "RASS"},
    22085815: {"label": "Visite_ZNS"},
    22085836: {"label": "Visite_Pflege"},
    22085820: {"label": "Visite_Oberarzt"},
}

text_varids = [22085815,22085836,22085820]
label_varids = [20512801,20512802,20512769,22086169,22086158]

arrow_props = dict(arrowstyle="->,head_width=0.15,head_length=0.3", shrinkB=3, linewidth=.5, alpha=.5, zorder=2)

#give the var_id markers their appropriate colors:
for v_id in var_ids:
    if v_id in text_varids:
        var_ids[v_id]['color'] = MARKER_COLOR_TEXT
        continue
    if v_id in label_varids:
        var_ids[v_id]['color'] = MARKER_COLOR_LABEL
        continue
    var_ids[v_id]['color'] = MARKER_COLOR_DEFAULT

df = pd.read_csv(input_file)
df = df[df['VarID'].isin(var_ids)] # only consider relevant var ids

for patient_n in df['patient'].unique():
    prev_columns_n = len(training_pairs)
    fig, ax = plt.subplots()

    patient_df = df[df['patient'] == patient_n].copy() #explicitly copy dataframe to suppress SettingWithCopyWarning

    #time between first and last event:
    first_event = patient_df['Zeitpkt'].min()
    seconds_in_icu = patient_df['Zeitpkt'].max() - first_event

    #create some helper columns for the individual events:
    patient_df['VarIDIndex'] = patient_df['VarID'].map(lambda vi: list(var_ids.keys()).index(vi) ) # use the index of each var id in the above list to map it on the scatter plot
    patient_df['VarIDColor'] = patient_df['VarID'].apply(lambda vi: var_ids[vi]['color'])
    patient_df['Zeitpkt_offset'] = patient_df['Zeitpkt'] - first_event

    #draw arrows between texts and their corresponding labels and save data pairs in new dataframe:
    text_rows = patient_df[ patient_df['VarID'].isin(text_varids) ] 
    for i, tr in text_rows.iterrows():
        tr_x = tr['Zeitpkt_offset']
        tr_y = tr['VarIDIndex']

        for v_id in label_varids:
            # only consider scores recorded within 2h of the text:
            corresponding_labels = patient_df[(patient_df['VarID'] == v_id) & 
                    (patient_df['Zeitpkt_offset'] > tr_x) & 
                    (patient_df['Zeitpkt_offset']-tr_x <= PREDICTION_MAX_DISTANCE)]

            if corresponding_labels.empty: #if no matching label was found vor this var_id, continue
                continue

            label_marker = corresponding_labels.iloc[0]
            l_x = label_marker['Zeitpkt_offset']
            l_y = label_marker['VarIDIndex']

            #Add the training pair to the list:
            pair = [patient_n, tr['VarID'], tr['Zeitpkt_offset'], tr['wert'], label_marker['VarID'], l_x, label_marker['wert']]
            training_pairs.append(pair)

            #Draw the arrow:
            plt.annotate("", xy=(l_x,l_y), xytext=(tr_x, tr_y), arrowprops=arrow_props)

    xtick_pos = np.arange(0, seconds_in_icu, 86400) #86400 seconds in a day --> 1 label per 24h
    xtick_labels = [f"Tag {s+1}" for s in range(xtick_pos.size)]

    # Draw a thin vertical line for each new day
    for xpos in xtick_pos:
        plt.axvline(x=xpos, color='#ededed', linewidth='1', zorder=1)

    #Draw markers on the plot
    plt.scatter(patient_df['Zeitpkt_offset'], patient_df['VarIDIndex'], c=patient_df['VarIDColor'], s=25, marker='+', zorder=3)
    
    #Set display properties for the plot
    plt.title(f"patient #{patient_n:04} (time in ICU: {timedelta(seconds=seconds_in_icu)} / data pairs: {len(training_pairs)-prev_columns_n})")
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=-45, ha="left", rotation_mode="anchor")
    plt.xticks(xtick_pos, xtick_labels)
    plt.yticks(range(len(var_ids)), [var_ids[id]['label'] for id in var_ids])
    fig.set_size_inches(15, 6)

    #Save figure and clean up
    filename = f'out/patient_{patient_n:04}.png'
    plt.savefig(filename, bbox_inches='tight', dpi=280)
    plt.clf() #clear figure
    plt.close() #close plot and release memory (in theory?)

    print(f"Saved result to {filename}. n={len(training_pairs)} (+{len(training_pairs)-prev_columns_n})")

out_df = pd.DataFrame(data=training_pairs, columns=['patient_id','text_varid','text_time','text','label_varid','label_time','label'])
out_df['text_time'] = out_df['text_time'].astype('int')
out_df['label_time'] = out_df['label_time'].astype('int')

print(f"Saving dataframe with {len(out_df)} rows to {out_file_name}...")
out_df.to_csv(out_file_name, index=False)