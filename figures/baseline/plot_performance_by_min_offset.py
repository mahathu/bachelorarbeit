import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('performance_by_min_offset.csv')

plt.plot(df['min'], df['mae'], marker='x', ms=4, label="SVR")
plt.fill_between(df['min'], df['mae']-df['std'], df['mae']+df['std'], alpha=.1, lw=0)

plt.grid()

plt.title("Baseline model performance by minutes between text and label")
plt.ylabel("Mean absolute error")
plt.xlabel("Allowed timeframe for training samples")
plt.xticks(df['min'], [f"{min}-{min+20}m" for min in df['min'].astype(int)])
plt.legend(loc="upper right")
plt.show()