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
W2V_MODEL_PATH = 'data/w2v_models/w2v_062920_5w_50d_3min_25e_1sg.model'
RASS_VAR_ID = 22086158
Visite_ZNS_VAR_ID = 22085815

# df = preprocess_texts(PAIRS_FILE_PATH, RASS_VAR_ID)
df = pd.read_csv('data/pairs_RASS.csv') # Alternative, wenn Eingabedaten schon bereinigt wurden

# w2v_model = build_w2v_model(df,
#                             window_size=5,
#                             dimensions=50,
#                             word_min_count=3, #5 is default
#                             epochs=25,
#                             use_skipgrams=1)
w2v_model = Word2Vec.load(W2V_MODEL_PATH) # Alternative, wenn Modell schon gebaut wurde

X_texts, y = get_x_y(df, Visite_ZNS_VAR_ID, RASS_VAR_ID, 60)

# X_matrix = transform_texts(w2v_model, X_texts)
X_matrix = pd.read_csv('data/text_features_100dim.csv')


# ========================= SVR ========================= #
svr = SVR(cache_size=1024, C=10)

print("Running cross validation...", end=' ', flush=True)
scores = cross_validate(svr, 
                        X_matrix,
                        y,
                        cv=ShuffleSplit(n_splits=5, test_size=.2),
                        scoring=['neg_mean_absolute_error', 'neg_root_mean_squared_error', 'r2']
)
print(colored('Done', 'green'))

for k in scores:
    print(f"{k}: {scores[k]}")