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
input_varids = [22085815, 22085836, 22085820][:1]
output_varids = [22086158, 20512769, 22086169][:1]
pairs = []

max_seconds = 60*60*8

#labels_nearest.csv enthält "nur" Daten mit max_offset = 3600 (1h)
df = pd.read_csv('../data/clean/labels_nearest_all.csv', nrows=1000000)

for input_varid in input_varids:
    for output_varid in output_varids:
        # remove unwanted rows:
        filter = ((df['text_varid'] == input_varid) & (df['label_varid'] == output_varid))
        df_filtered = df[filter]
        offsets = (df_filtered['text_time'] - df_filtered['label_time']).abs().sort_values(ascending=False)
        
        print(offsets)

        print(f"{var_id_names[input_varid]} --> {var_id_names[output_varid]} (n={len(df_filtered)}, max offset={offsets.max()})")

        buckets = np.empty(max_seconds)
        buckets.fill(0)

        for offset in offsets: # this is slow
            buckets[-offset:] = [x+1 for x in buckets[-offset:]]

        pairs.append({
            'in': input_varid,
            'out': output_varid,
            'buckets': buckets,
        })

print(pairs)

#== plotting: ==#
# maybe redo this in ggplot to make it look nicer if bored
x = np.arange(max_seconds)
mins = [60*60*(i+1) for i in range(8)]

linestyles = ['-', '--', ':'] # 1 for each input category
colors = ["#E57373", "#4DD0E1", "#AED581", "#FF8A65", "#FFF176"] # 1 for each out category (nur die ersten 3 sind relevant)

for max_seconds in mins:
    print(max_seconds)

    if max_seconds <= 60*60:
        xtick_pos = np.arange(15*60, max_seconds, 15*60)
        xtick_labels = [f"{(s+1)*15} Min" for s in range(xtick_pos.size)]
    else:
        xtick_pos = np.arange(60*60, max_seconds, 60*60)
        xtick_labels = [f"{s+1}h" for s in range(xtick_pos.size)]

    fig, ax = plt.subplots()

    for pair in pairs:
        b = pair['buckets']
        ls_index = input_varids.index(pair['in'])
        c_index = output_varids.index(pair['out'])
        line, = plt.plot(x, b, linestyle=linestyles[ls_index], color=colors[c_index], linewidth=1.33)
        line.set_label(var_id_names[pair['out']])

    lines = ax.get_lines()
    
    dummy_lines = []
    for i,v_id in enumerate(input_varids):
        line = ax.plot([],[], c="black", ls = linestyles[i])[0]
        line.set_label(var_id_names[v_id])
        dummy_lines.append(line)

    legend1 = plt.legend([l for l in lines], [lines[i].get_label() for i in range(len(output_varids))], loc=4)
    legend2 = plt.legend([l for l in dummy_lines], [l.get_label() for l in dummy_lines], loc=2)
    ax.add_artist(legend1)

    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    plt.ylabel('Anzahl der verbleibenden Wertepaare')
    plt.xlabel('Maximal zulässige Differenz zwischen Zeitpunkten')
    plt.xticks(xtick_pos, xtick_labels)
    ax.set_xlim(0, max_seconds)
    ax.set_ylim(0, max(b[:max_seconds])*1.1)

    plt.show()
    break

    filename = f'out/n_samples_max_{int(max_seconds/60)}min.png'
    plt.savefig(filename, bbox_inches='tight', dpi=280)
    plt.clf() #clear figure
    plt.close()