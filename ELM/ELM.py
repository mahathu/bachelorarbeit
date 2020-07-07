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

    n_neurons = int(1 * n_input_columns)
    model = hpelm.HPELM(n_input_columns, 1)
    model.add_neurons(n_neurons, 'tanh')

    n_runs = 10
    mae = 0
    for i in range(n_runs):
        X_train, X_test, y_train, y_test = train_test_split(X_matrix, y, test_size=.2)
        model.train(X_train, y_train)
        preds = model.predict(X_test)
        mae += get_MAE(preds, y_test)
    mae /= n_runs

    print(f"MAE for n_neurons={n_neurons}: {mae:.3f}")

    
    print(colored(f'Done', 'green'))