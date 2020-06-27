import pandas as pd
import matplotlib.pyplot as plt
# plt.grid()
# plt.xlim(df_sgd['x'].min(), df_sgd['x'].max() + (df_sgd['x'].min()/2) )

# #SGD MSE
# plt.plot(df_sgd['x'], df_sgd['rmse'], linestyle='-', marker='x', ms=4, color='r', label="SGD RMSE")
# plt.fill_between(df_sgd['x'], df_sgd['rmse'] - df_sgd['rmse_std'], df_sgd['rmse'] + df_sgd['rmse_std'], alpha=0.1, color="r", lw=0)

# #SVR MSE
# plt.plot(df_svr['x'], df_svr['rmse'], linestyle='--', marker='x', ms=4, color='r', label="SVR RMSE")
# plt.fill_between(df_svr['x'], df_svr['rmse'] - df_svr['rmse_std'], df_svr['rmse'] + df_svr['rmse_std'], alpha=0.1, color="r", lw=0)

df = pd.read_csv('performances_max_30min_rassonly.csv')
df['mae'] = df['neg_mean_absolute_error']*-1
df['mae_std'] = df['neg_mean_absolute_error_std']

fig,ax = plt.subplots()
#colors = ['#fb8072', '#80b1d3']
colors = ['#3969b1', '#cc2529']
for estimator_name, c, ls, marker in zip(['SGDRegressor', 'SVR'], colors, ['-','--'], ['x','o']):
    e_df = df.loc[df['estimator'] == estimator_name]

    plt.plot(e_df['n_samples'], e_df['mae'], linestyle=ls, marker=marker, ms=4, color=c, label=estimator_name)
    plt.fill_between(e_df['n_samples'], e_df['mae']-e_df['mae_std'], e_df['mae']+e_df['mae_std'], alpha=.15, color=c, lw=0)

plt.grid()

plt.title("Baseline model performance by number of training samples")
plt.ylabel("Mean absolute error")
plt.xlabel("Number of training samples")
plt.legend(loc="upper right")
# plt.show()
fig.set_size_inches(10, 6)
plt.savefig("performance_by_n_samples.png", bbox_inches='tight', dpi=300)