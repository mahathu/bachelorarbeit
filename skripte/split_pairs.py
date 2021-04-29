"""split an input file of data pairs
into a training set and a set to make
predictions on."""

import pandas as pd
pd.options.mode.chained_assignment = None

in_varids = [22085815, 22085836]
out_varids = [22086158, 20512769]

N_TEST_ROWS = 4000 # number of rows for testing
out_dir = ('../data/split_data/')

df = pd.read_csv('../data/clean/labels_nearest_all.csv')
df['abs_diff'] = (df['text_time'] - df['label_time']).abs()

for in_v in in_varids:
    for out_v in out_varids:
        df_filtered = df.loc[
              (df['abs_diff'] <= 60*60*2) # 2 hours or less between text and score
            & (df['text_varid'] == in_v)
            & (df['label_varid'] == out_v)
        ]

        df_filtered.drop(['text_varid', 'label_varid', 'abs_diff', 'patient_id', 'text_time', 'label_time'], axis=1, inplace=True)
        df_filtered = df_filtered.sample(frac=1).reset_index(drop=True) #shuffle

        df_test = df_filtered[:N_TEST_ROWS] # first N_TEST_ROWS rows
        df_train = df_filtered[N_TEST_ROWS:] # the rest of the rows

        for (out_df, name) in zip([df_test, df_train], ['test', 'train']):
            fn = f"{out_dir}{in_v}_to_{out_v}_{name}.csv"
            out_df.to_csv(fn, index=False)
            print(f"Saved file to {fn} ({len(out_df)} rows)")
        print()