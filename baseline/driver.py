import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import train_model
from datetime import datetime

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

draw_accuracy_plot = False
input_varids = [22085815, 22085836]
output_varids = [22086158, 20512769]
max_time_between = 60*60/4 #15 minutes

accuracies = np.zeros((len(input_varids), len(output_varids)))
note = "NO STEMMING/CLEANING --> CountVectorizer (w/ n=[1,2,3] word ngrams) --> TfidfTransformer --> svm.SVR(kernel='linear')"

df_all = pd.read_csv("../data/clean/labels_nearest.csv")
perf_rows = []

for i, input_varid in enumerate(input_varids):
    for j, output_varid in enumerate(output_varids):
        filter = ((df_all['text_varid'] == input_varid) 
                & (df_all['label_varid'] == output_varid) 
                & (df_all['label_time'] - df_all['text_time'] <= max_time_between))

        # remove unwanted rows:
        df = df_all[filter]

        # remove irrelevant columns:
        df = df[['text', 'label']]
        if output_varid == 22086169: # CAM-ICU
            df = df.replace({'label': {
                'neg.': 0,
                'pos.': 1,
                'unmögl.': 2,
            }})

        df['text'] = df['text'].astype('U') #unicode
        df['label'] = df['label'].astype(int)
        
        print(f"Predicting {var_ids[output_varid]} based on {var_ids[input_varid]}\n"
              f"Unique labels: {df['label'].unique()} ({len(df['label'].unique())} in total)\n"
              f"Total samples after filtering: {len(df)}")
        
        acc, dummy_acc = train_model(df)

        row = [var_ids[input_varid], var_ids[output_varid], max_time_between, len(df), acc, dummy_acc, note]
        perf_rows.append(row)

        accuracies[i,j] = acc
        exit()

perf_df = pd.DataFrame(perf_rows, columns=['label_varid', 'predict_varid', 'max_time_between', 'n_samples', 'r2', 'dummy_r2', 'note'])
perf_df.to_csv(f"baseline_model_performance_{datetime.now().strftime('%Y-%m-%d %H:%M')}.csv", index=False)

if not draw_accuracy_plot:
    exit()

#plot results:
x = np.arange(accuracies.shape[1])  # label locations
bar_width = .25  # width of the bars

fig, ax = plt.subplots()
for index,accuracies in enumerate(accuracies):
    l = var_ids[input_varids[index]]
    rects = ax.bar(x + index*bar_width, [max(0,a) for a in accuracies], bar_width, edgecolor='white', label=l)
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f"{height:5.3f}",
            xy=(rect.get_x() + bar_width / 2, height),
            xytext=(0, 3),  # 3pt vertical offset
            textcoords="offset points",
            ha='center', va='bottom')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('R²')
ax.set_title('Baseline model performance by input and output varid')
plt.xticks( list(map(lambda p:p+bar_width/2, x)), [var_ids[vi] for vi in output_varids])
ax.legend()

fig.tight_layout()
plt.show()