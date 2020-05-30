import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

max_seconds = 60*60*8
buckets = np.empty(max_seconds)
buckets.fill(0)
x = np.arange(len(buckets))

df = pd.read_csv('../data/clean/labels_nearest.csv', nrows=100)
df['offset'] = (df['text_time'] - df['label_time']).abs()

for offset in df['offset']:
    buckets[-offset:] = [x+1 for x in buckets[-offset:]]

print(buckets)

mins = [60*60*(i+1) for i in range(8)]
for max_seconds in mins:
    print(max_seconds)

    if max_seconds <= 60*60:
        xtick_pos = np.arange(15*60, max_seconds, 15*60)
        xtick_labels = [f"{(s+1)*15} Min" for s in range(xtick_pos.size)]
    else:
        xtick_pos = np.arange(60*60, max_seconds, 60*60)
        xtick_labels = [f"{s+1}h" for s in range(xtick_pos.size)]

    fig, ax = plt.subplots()
    plt.plot(x, buckets)
    plt.ylabel('Anzahl der verbleibenden Wertepaare')
    plt.xlabel('Maximal zulässige Differenz zwischen Zeitpunkten')
    plt.xticks(xtick_pos, xtick_labels)
    ax.set_xlim(0, max_seconds)
    ax.set_ylim(0, max(buckets[:max_seconds])*1.1)
    plt.fill_between(np.arange(max_seconds), 0, buckets[:max_seconds], alpha=.15)

    plt.show()
    break

    filename = f'out/n_samples_max_{int(max_seconds/60)}min.png'
    plt.savefig(filename, bbox_inches='tight', dpi=280)
    plt.clf() #clear figure
    plt.close()