"""
This file contains all steps to build a functioning ELM model,
including the word featurization stage using word2vec.
"""

import pandas as pd
import numpy as np
from utilities import preprocess_texts, get_x_y, transform_texts
from build_word2vec import build_w2v_model
from gensim.models import Word2Vec
from termcolor import colored

from sklearn.svm import SVR
from sklearn.model_selection import train_test_split, cross_val_score, cross_validate, ShuffleSplit

PAIRS_FILE_PATH = '../data/clean/labels_nearest_all.csv'
W2V_MODEL_PATH = 'data/w2v_models/w2v_062920_5w_50d_3min_5e_1sg.model'
X_MATRIX_PATH = 'data/text_features_50dim.csv'

RASS_VAR_ID = 22086158
Visite_ZNS_VAR_ID = 22085815
Visite_Pflege_VAR_ID = 22085836


df_rows = []
for dims in [20, 40, 80]:
    for min_count in [1,3,5]:
        for window_size in [2,5]:
            w2v_params = {
                'WINDOW_SIZE': window_size,
                'DIMENSIONS': dims,
                'WORD_MIN_COUNT': min_count,
                'TRAINING_EPOCHS': 10,
            }

            # df = preprocess_texts(PAIRS_FILE_PATH, RASS_VAR_ID)
            df = pd.read_csv('data/pairs_RASS_spellcorrected.csv') # Alternative, wenn Eingabedaten schon bereinigt wurden

            # The texts in the dataframe above are already preprocessed/cleaned (see utiliites.py)

            w2v_model = build_w2v_model(df,
                                        window_size=w2v_params['WINDOW_SIZE'], #5 is default
                                        dimensions=w2v_params['DIMENSIONS'],
                                        word_min_count=w2v_params['WORD_MIN_COUNT'], #5 is default
                                        epochs=w2v_params['TRAINING_EPOCHS'],
                                        use_skipgrams=1)
            # w2v_model = Word2Vec.load(W2V_MODEL_PATH) # Alternative, wenn Modell schon gebaut wurde

            X_texts, y = get_x_y(df, Visite_ZNS_VAR_ID, RASS_VAR_ID, 90)

            X_matrix = transform_texts(w2v_model, X_texts)
            # X_matrix = pd.read_csv(X_MATRIX_PATH) # Alternative, wenn Eingabetexte schon vektorisiert wurden

            # Filter out rows that had invalid input data in the X matrix:
            n_rows_before = len(y)
            broken_rows_mask = X_matrix[X_matrix.columns[0]].notnull()
            X_matrix = X_matrix[broken_rows_mask]
            y = y[broken_rows_mask].squeeze()
            print(f"{n_rows_before-len(y)} rows where filtered because the X matrix contained no data (empty text or text with no known words)")

            # ========================= SVR (just for testing) ========================= #

            for param in w2v_params:
                print(f"{param}: {w2v_params[param]}")
            
            print(colored("="*80, 'cyan'))

            for c in [.1, 1, 10]:
                scores = cross_validate(SVR(cache_size=1024, C=c),
                                        X_matrix,
                                        y,
                                        cv=ShuffleSplit(n_splits=5, test_size=.2),
                                        scoring=['neg_mean_absolute_error']
                )
                
                row = [dims, min_count, window_size, c, -1* np.mean(scores['test_neg_mean_absolute_error'])]
                print(row)
                df_rows.append(row)

df = pd.DataFrame(df_rows, columns=['dimensions', 'word_min_count', 'window_size', 'svr_C', 'MAE'])
df.to_csv('PERFORMANCE.csv')