import pandas as pd
from utilities import clean_text

in_file = '../data/clean/labels_nearest_all.csv'

var_ids = {
    20512769: "GCS",
    22086158: "RASS",
}

df = pd.read_csv(in_file)

for v_id in var_ids:
    out_file = f'data/pairs_{var_ids[v_id]}.csv'
    df_v = df[df['label_varid'] == v_id]


    df_v['time_diff'] = (df_v['text_time'] - df_v['label_time']).abs()
    df_v['text'] = df_v['text'].apply(clean_text)

    df_v = df_v[df_v['text'] != ''] # remove rows with empty texts
    df_v.to_csv(out_file, index=False)

    print(f"{var_ids[v_id]} done.")