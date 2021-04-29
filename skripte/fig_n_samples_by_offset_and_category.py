import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

var_id_names = {
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


output_varid = 20512769 #GCS
input_varids = [22085815, 22085836, 22085820]
pairs = []

max_seconds = 60*60*6 #6 hours

df = pd.read_csv('../data/clean/labels_nearest_all.csv')

for input_varid in input_varids:
    # remove unwanted rows:
    df_filter = ((df['text_varid'] == input_varid) & (df['label_varid'] == output_varid))
    df_filtered = df[df_filter]
    df_filtered['offset'] = (df_filtered['text_time'] - df_filtered['label_time']).abs()
    
    # offsets = (df_filtered['text_time'] - df_filtered['label_time']).abs().sort_values(ascending=False)
    # print(offsets)

    #print(f"{var_id_names[input_varid]} --> {var_id_names[output_varid]} (n={len(df_filtered)}, max offset={df_filtered['offset'].max()})")

    buckets = np.empty(max_seconds)
    buckets.fill(0)

    # for offset in offsets: # this is slow
    #     # für jedes Wertepaar nimm den offset. 
    #     # für alle buckets darüber, erhöhe den Zähler um 1
    #     buckets[-offset:] = [x+1 for x in buckets[-offset:]]

    # für jeden bucket, gucke wie viele der offsets darüber sind:
    for i in range(max_seconds):
        n_of_pairs_below_offset_thresh = len(df_filtered[df_filtered['offset'] <= i])
        buckets[i] = n_of_pairs_below_offset_thresh

    pairs.append({
        'in': input_varid,
        'out': output_varid,
        'buckets': buckets,
    })

print(pairs)

#== plotting: ==#
# maybe redo this in ggplot to make it look nicer if bored
x = np.arange(max_seconds)

colors = ["#3969b1", "#da7c30", "#3e9651"] # 1 for each out category (nur die ersten 3 sind relevant)

print(max_seconds)

xtick_pos = np.arange(60*60, max_seconds, 60*60)
xtick_labels = [f"{s+1}h" for s in range(xtick_pos.size)]

fig, ax = plt.subplots()

for i, pair in enumerate(pairs):
    b = pair['buckets']
    line, = plt.plot(x, b, linewidth=1.33, c=colors[i], label=var_id_names[pair['in']])

plt.legend(loc="upper left")
plt.title('Wertepaare für '+var_id_names[output_varid])
plt.ylabel('Anzahl Wertepaare')
# plt.xlabel('Maximal zulässige Differenz zwischen Zeitpunkten')
plt.xticks(xtick_pos, xtick_labels)
ax.set_xlim(0, max_seconds)
ax.set_ylim(0, max(b[:max_seconds])*1.1)

# plt.show()
# exit()

filename = f'pairs_by_max_min_{var_id_names[output_varid]}_FIXED.png'
plt.savefig(filename, bbox_inches='tight', dpi=280)
plt.clf() #clear figure
plt.close()