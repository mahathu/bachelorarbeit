import pandas as pd
import matplotlib.pyplot as plt

df_sgd = pd.read_csv('sgd_perf_by_n_samples.csv')
df_svr = pd.read_csv('svr_perf_by_n_samples.csv')

df_sgd['rmse'] = (df_sgd['neg_mean_squared_error']*-1).pow(1./2)
df_sgd['rmse_std'] = df_sgd['neg_mean_squared_error_std']

df_svr['rmse'] = (df_svr['neg_mean_squared_error']*-1).pow(1./2)
df_svr['rmse_std'] = df_svr['neg_mean_squared_error_std']

plt.grid()
plt.xlim(df_sgd['x'].min(), df_sgd['x'].max() + (df_sgd['x'].min()/2) )

#SGD MSE
plt.plot(df_sgd['x'], df_sgd['rmse'], linestyle='-', marker='x', ms=4, color='r', label="SGD RMSE")
plt.fill_between(df_sgd['x'], df_sgd['rmse'] - df_sgd['rmse_std'], df_sgd['rmse'] + df_sgd['rmse_std'], alpha=0.1, color="r", lw=0)

#SVR MSE
plt.plot(df_svr['x'], df_svr['rmse'], linestyle='--', marker='x', ms=4, color='r', label="SVR RMSE")
plt.fill_between(df_svr['x'], df_svr['rmse'] - df_svr['rmse_std'], df_svr['rmse'] + df_svr['rmse_std'], alpha=0.1, color="r", lw=0)

#SGD R^2
plt.plot(df_sgd['x'], df_sgd['r2'], linestyle='-', marker='x', ms=4, color='g', label="SGD R^2")
plt.fill_between(df_sgd['x'], df_sgd['r2'] - df_sgd['r2_std'], df_sgd['r2'] + df_sgd['r2_std'], alpha=0.1, color="g", lw=0)

#SVR R^2
plt.plot(df_svr['x'], df_svr['r2'], linestyle='--', marker='x', ms=4, color='g', label="SVR R^2")
plt.fill_between(df_svr['x'], df_svr['r2'] - df_svr['r2_std'], df_svr['r2'] + df_svr['r2_std'], alpha=0.1, color="g", lw=0)

plt.title("Baseline model performance by number of samples")
plt.ylabel("R^2")
plt.xlabel("Number of training samples")
plt.legend(loc="upper right")
plt.show()