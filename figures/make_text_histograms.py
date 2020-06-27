import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

text_varids = [
    ('Visite_ZNS', 22085815, 10, 2),
    ('Visite_Pflege', 22085836, 20, 5),
    ('Visite_Oberarzt', 22085820, 100, 5),
]

in_file_url = '../data/clean/all_scores.csv'
df = pd.read_csv(in_file_url)

for name, varid, step, nlabel in text_varids:
    texts = df[df['VarID'] == varid]['wert']
    
    textlens = []
    nan_vals = 0
    for text in texts:
        if type(text) is float:
            nan_vals += 1
            continue

        textlens.append(len(text.strip()))

    max_len = max(textlens)
    
    plot_title = f"Text length for {name} ({len(texts)} total entries)"
    if nan_vals:
        plot_title = f"Text length for {name} ({len(texts)} total entries, {nan_vals} nan)"
    plt.title(plot_title)
    plt.xlabel('Characters')
    plt.ylabel('Number of entries')
    plt.hist(textlens, bins=np.arange(0, max_len, step)-step/2, rwidth=.85, color='#3969b1')
    
    plt.xticks(np.arange(0, max_len-step, step))
    for i, xtick in enumerate(plt.gca().xaxis.get_ticklabels()):
        if i%nlabel != 0:
            xtick.set_visible(False)

    #plt.show()
    plt.gcf().set_size_inches(10, 6)
    plt.savefig(f"visitentext_histograms/hist_{name}.png", bbox_inches='tight', dpi=300)
    plt.clf()
    print(f"{name} done")