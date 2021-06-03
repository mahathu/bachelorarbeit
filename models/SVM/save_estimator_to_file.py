from SVRmodel import get_SVR
from utilities import get_x_y
import pickle
import pandas as pd

input_varids = [22085815, 22085836]
output_varids = [22086158, 20512769]
df_all = pd.read_csv("../../data/clean/labels_nearest_all.csv")

for input_varid in input_varids:
    for output_varid in output_varids:
        X, y = get_x_y(df_all, input_varid, output_varid, 
            max_min_between=60*60,
            max_samples = 15000
        )

        print(f"Training model for {input_varid}->{output_varid}")
        svr = get_SVR()
        svr.fit(X, y)

        file_path = f'baked_models/svr-{input_varid}-{output_varid}.est'
        with open(file_path,'wb') as f: #wb = writing in binary
            pickle.dump(svr,f)

        print(f"Saved file to {file_path}")