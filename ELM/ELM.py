import hpelm
from utilities import get_MAE
from sklearn.model_selection import train_test_split
import pandas as pd
from termcolor import colored

def create_model(X_df, y):
    print(f"Building ELM models...", end=' ', flush=True)
    n_input_columns = len(X_df.columns)
    X_matrix = X_df.to_numpy()
    y = y.to_numpy()

    rows = []
    for n_mult in [1/3, .5, .75, 1, 1.25, 1.5, 1.75, 2]:
        for func in ['sigm', 'lin', 'tanh', 'rbf_l2', 'rbf_linf']:
            n_neurons = int(n_mult * n_input_columns)
            print(n_neurons, end=' ', flush=True)
            model = hpelm.HPELM(n_input_columns, 1)
            model.add_neurons(n_neurons, func)

            n_runs = 10
            mae = 0
            for i in range(n_runs):
                X_train, X_test, y_train, y_test = train_test_split(X_matrix, y, test_size=.2)
                model.train(X_train, y_train)
                preds = model.predict(X_test)
                mae += get_MAE(preds, y_test)
            mae /= n_runs

            #print(f"MAE for n_neurons={n_neurons}: {mae:.3f}")
            rows.append(
                [func, n_neurons, mae]
            )
    
    print(colored(f'Done', 'green'))

    df = pd.DataFrame(rows, columns=['elm_func', 'elm_n_neurons', 'MAE'])
    # df.to_csv('ELM_performance.csv', index=False)
    return df