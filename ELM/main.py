"""
This file contains all steps to build a functioning ELM model,
including the word featurization stage using word2vec.
"""

import pandas as pd
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

# df = preprocess_texts(PAIRS_FILE_PATH, RASS_VAR_ID)
df = pd.read_csv('data/pairs_RASS.csv') # Alternative, wenn Eingabedaten schon bereinigt wurden

w2v_model = build_w2v_model(df,
                            window_size=5,
                            dimensions=20,
                            word_min_count=3, #5 is default
                            epochs=10,
                            use_skipgrams=1)
# w2v_model = Word2Vec.load(W2V_MODEL_PATH) # Alternative, wenn Modell schon gebaut wurde

X_texts, y = get_x_y(df, Visite_ZNS_VAR_ID, RASS_VAR_ID, 60)

X_matrix = transform_texts(w2v_model, X_texts)
# X_matrix = pd.read_csv(X_MATRIX_PATH) # Alternative, wenn Eingabetexte schon vektorisiert wurden

# Filter out rows that had invalid input data in the X matrix:
n_rows_before = len(y)
broken_rows_mask = X_matrix[X_matrix.columns[0]].notnull()
X_matrix = X_matrix[broken_rows_mask]
y = y[broken_rows_mask].squeeze()
print(f"{n_rows_before-len(y)} rows where filtered because the X matrix contained no data (empty text or text with no known words)")

# ========================= SVR (just for testing) ========================= #
svr = SVR(cache_size=1024, C=10)

print("Running cross validation...")

scores = cross_validate(svr,
                        X_matrix,
                        y,
                        cv=ShuffleSplit(n_splits=1, test_size=.2),
                        scoring=['neg_mean_absolute_error', 'neg_root_mean_squared_error', 'r2']
)
for k in scores:
    print(f"{k}: {scores[k]}")