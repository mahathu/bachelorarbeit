import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error
from make_predictions_util import *
from termcolor import colored

from utilities import clean_text, transform_texts
from build_word2vec import build_w2v_model_from_series
from gensim.models import Word2Vec

in_varid = 22085815 # Visite_ZNS
out_varid = 22086158 # RASS

train_df_path = f'../data/split_data/{in_varid}_to_{out_varid}_train.csv'
test_df_path  = f'../data/split_data/{in_varid}_to_{out_varid}_test.csv'

train_df = pd.read_csv(train_df_path)
test_df = pd.read_csv(test_df_path)
actual_vals = test_df['label']

print(f"{len(train_df)} training samples loaded.")

def round_preds_and_print(prediction_series, name):
    preds_rounded = np.rint(prediction_series).astype(int)
    for (t, c, p) in zip(['not rounded', '    rounded'], ['yellow', 'green'], [prediction_series, preds_rounded]):
        mae = mean_absolute_error(actual_vals, p)
        print(colored(f"MAE for {name} ({t}) = {mae:.3f}", c))
    return preds_rounded

# 1) BASELINE MOODEL #
# print("Building baseline model...")

# preds = predict_baseline(train_df, test_df)
# preds_rounded = round_preds_and_print(preds, "baseline model")
# test_df['predictions_baseline'] = preds_rounded

# 2) SVR WITH W2V #
clean_texts_train = train_df['text'].apply(clean_text)
clean_texts_test = test_df['text'].apply(clean_text)

#w2v_model = build_w2v_model_from_series(clean_texts_train, dimensions=200)
w2v_model = Word2Vec.load('temp_w2v.model')

X_matrix_train = transform_texts(w2v_model, clean_texts_train).fillna(0)
X_matrix_test  = transform_texts(w2v_model, clean_texts_test).fillna(0)
X_matrix_train = X_matrix_train.fillna(0)
X_matrix_test = X_matrix_test.fillna(0)

preds = predict_svr_with_w2v(X_matrix_train, train_df['label'], X_matrix_test)
preds_rounded = round_preds_and_print(preds, "w2v+svr")
test_df['predictions_w2v_svr'] = preds_rounded

# 3) ELM WITH W2V #
preds = predict_elm(X_matrix_train, train_df['label'], X_matrix_test)
preds_rounded = round_preds_and_print(preds, "ELM")
test_df['predictions_ELM'] = preds_rounded

test_df.to_csv(test_df_path, index=False)
print(colored("Done!", "green"))
print(f"Output   written to {test_df_path}")