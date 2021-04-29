import pandas as pd
import matplotlib.pyplot as plt

in_varid = 22085815 # Visite_ZNS
out_varid = 22086158 # RASS

test_df_path  = f'../data/split_data/{in_varid}_to_{out_varid}_test.csv'
df = pd.read_csv(test_df_path)

bins = df['label'].unique()
bins.sort()
print(bins)
bars = []
colors = ['#3969b1','#da7c30','#3e9651','#cc2529']
cols = ['label', 'predictions_baseline', 'predictions_w2v_svr', 'predictions_ELM']
colNames = ['Actual Value', 'Support Vector Regression', 'SVR with word2vec featurization', 'Extreme Learning Machine']
for col in cols:
    bars.append(df[col])

plt.hist(bars, bins-.5, label=colNames, rwidth=.75, color=colors)
plt.xticks(bins)
plt.xlim(bins[0]-.75, bins[-1]+.75)
plt.legend(loc='upper left')
plt.show()