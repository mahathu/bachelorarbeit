import pandas as pd
import numpy as np
import SVRmodel
from utilities import iprint, sprint, wprint, eprint, test_estimator, get_x_y, var_ids, clean_and_stem_text
import methods

input_varids = [22085815, 22085836]
output_varids = [22086158, 20512769]

df_all = pd.read_csv("../../data/clean/labels_nearest_all.csv")
MAX_MIN_BETWEEN_EVENTS = 60
train_size = 5000
test_size = 2000

out_dict = {
    'text_varid': [],
    'score_varid': [],
    'x': [],
    'yactual': [],
    'ypred': [],
}

for input_varid in input_varids:
    for output_varid in output_varids:
        X, y = get_x_y(df_all, input_varid, output_varid, 
            max_min_between=MAX_MIN_BETWEEN_EVENTS, 
            max_samples=train_size+test_size
        )

        print(f"Fitting model for {input_varid} - {output_varid}")

        svr = SVRmodel.get_SVR()
        svr.fit(X[:train_size], y[:train_size])

        print("Predicting...")

        preds = svr.predict(X[train_size:])

        out_dict['text_varid'].extend([input_varid] * test_size)
        out_dict['score_varid'].extend([output_varid] * test_size)
        out_dict['x'].extend(X[train_size:])
        out_dict['yactual'].extend(y[train_size:])
        out_dict['ypred'].extend(np.around(preds))

df = pd.DataFrame(out_dict)
print(df)
df.to_csv("preds.csv", index=False)