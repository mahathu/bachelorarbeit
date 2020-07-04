"""
This file contains all steps to build a functioning ELM model,
including the word featurization stage using word2vec.
"""

import pandas as pd
import numpy as np
from utilities import preprocess_texts, get_x_y, transform_texts, test_with_SVM
from build_word2vec import build_w2v_model
from ELM import create_model
from gensim.models import Word2Vec
from termcolor import colored

PAIRS_FILE_PATH = '../data/clean/labels_nearest_all.csv'
W2V_MODEL_PATH = 'data/w2v_models/w2v_070320_7w_100d_1min_15e_1sg.model'
X_MATRIX_PATH = 'data/text_features_100dim.csv'

RASS_VAR_ID = 22086158
Visite_ZNS_VAR_ID = 22085815
Visite_Pflege_VAR_ID = 22085836


ELM_out_dfs = []
SVR_out_dfs = []

dims = [10,30,50,80,100,130,150,200,300]
win_sizes = [2,5,7]
wmcs = [1,3,5]
total_runs = len(dims)*len(win_sizes)*len(wmcs)
runs_done = 0

for dimensions in dims:
    for window_size in win_sizes:
        for word_min_count in wmcs:
            w2v_params = {
                'window_size': window_size,
                'dimensions': 100,
                'word_min_count': 1,
                'training_epochs': 15,
            }

            print()
            print(colored(w2v_params,'cyan'))
            print('*'*80)

            # df = preprocess_texts(PAIRS_FILE_PATH, RASS_VAR_ID)
            df = pd.read_csv('data/pairs_RASS_spellcorrected.csv') # Alternative, wenn Eingabedaten schon bereinigt wurden

            # The texts in the dataframe above are already preprocessed/cleaned (see utiliites.py)

            # w2v_model = build_w2v_model(df,
                                        # window_size=w2v_params['WINDOW_SIZE'], #5 is default
                                        # dimensions=w2v_params['DIMENSIONS'],
                                        # word_min_count=w2v_params['WORD_MIN_COUNT'], #5 is default
                                        # epochs=w2v_params['TRAINING_EPOCHS'],
                                        # use_skipgrams=1)
            w2v_model = Word2Vec.load(W2V_MODEL_PATH) # Alternative, wenn Modell schon gebaut wurde

            X_texts, y = get_x_y(df, Visite_ZNS_VAR_ID, RASS_VAR_ID, 90)

            # X_matrix = transform_texts(w2v_model, X_texts)
            X_matrix = pd.read_csv(X_MATRIX_PATH) # Alternative, wenn Eingabetexte schon vektorisiert wurden

            # Filter out rows that had invalid input data in the X matrix:
            n_rows_before = len(y)
            broken_rows_mask = X_matrix[X_matrix.columns[0]].notnull()
            X_matrix = X_matrix[broken_rows_mask]
            y = y[broken_rows_mask].squeeze()
            # print(f"{n_rows_before-len(y)} rows were filtered because the X matrix contained no data (empty text or text with no known words)")

            # SVR
            for c in [1, 10]:
                print(f"Building SVM with C={c}...", end=' ', flush=True)
                svr_mae = test_with_SVM(X_matrix, y, c)
                svr_df = pd.DataFrame([svr_mae], columns=["SVR_MAE"])
                for param in w2v_params:
                    svr_df["w2v"+param] = w2v_params[param]
                
                SVR_out_dfs.append(svr_df)
                print(colored(f'Done (mae={svr_mae:.3f})', 'green'))

            # ELM
            ELM_perf_df = create_model(X_matrix, y)
            for param in w2v_params:
                ELM_perf_df["w2v"+param] = w2v_params[param]
            
            ELM_out_dfs.append(ELM_perf_df)

            runs_done += 1
            print(colored(f'{runs_done}/{total_runs} runs done ({runs_done/total_runs*100:.1f}%)', 'magenta'))

print('done')
#this is stupid
pd.concat(ELM_out_dfs).to_csv('perf/ELM_performance.csv', index=False)
pd.concat(SVR_out_dfs).to_csv('perf/SVR_performance.csv', index=False)
print('saved to dfs')