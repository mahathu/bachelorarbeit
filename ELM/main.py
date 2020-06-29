"""
This file contains all steps to build a functioning ELM model,
including the word featurization stage using word2vec.
"""

import pandas as pd
from utilities import preprocess_texts
from build_word2vec import build_w2v_model
from gensim.models import Word2Vec

PAIRS_FILE_PATH = '../data/clean/labels_nearest_all.csv'
W2V_MODEL_PATH = 'data/w2v_models/w2v_062920_5w_100d_1min_25e_1sg.model'
RASS_VAR_ID = 22086158

# df = preprocess_texts(PAIRS_FILE_PATH, RASS_VAR_ID)
df = pd.read_csv('data/pairs_RASS.csv') # Alternative, wenn Eingabedaten schon bereinigt wurden

# w2v_model = build_w2v_model(df,
#                             window_size=5,
#                             dimensions=100,
#                             word_min_count=1, #1 is default
#                             epochs=25,
#                             use_skipgrams=1)
w2v_model = Word2Vec.load(W2V_MODEL_PATH) # Alternative, wenn Modell schon gebaut wurde

#print(w2v_model.wv.most_similar(positive=["rass"]))