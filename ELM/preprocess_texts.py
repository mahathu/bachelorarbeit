import pandas as pd
from utilities import clean_text

in_file = '../data/clean/labels_nearest_all.csv'

var_ids = {
    # 20512769: "GCS",
    22086158: "RASS",
}

df = pd.read_csv(in_file)

for v_id in var_ids:
    df_v = df[df['label_varid'] == v_id]

    df_v['time_diff'] = (df_v['text_time'] - df_v['label_time']).abs()

    # tokenization:
    df_v['text'] = df_v['text'].apply(clean_text)
    
    total_pairs = len(df_v)
    df_v['text'] = df_v['text'].astype(str)

    df_v = df_v[df_v['text'] != ''] # remove rows with empty texts
    df_v = df_v[df_v['text'] != 'nan'] 
    # spell checking:
    # dictionary = set([word for text in df_v['text'] for word in text.split()])
    # out_str = ' '.join(w.replace('-','') for w in filter(lambda w: len(w)>2, dictionary))
    # with open('data/dictionary.txt', 'w') as dict_file:
    #     dict_file.write(out_str)
    # print(f"{len(dictionary)} unique words.")
    # exit()

    print(f"Tokenizing {var_ids[v_id]} done ({total_pairs}/{len(df_v)})")
    out_file = f'data/pairs_{var_ids[v_id]}.csv'
    df_v.to_csv(out_file, index=False)