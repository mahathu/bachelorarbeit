import pandas as pd
import SVRmodel
from sklearn.model_selection import cross_validate

def filter_rass_occurences(s):
    l = s.lower()
    i = l.find('rass')
    if i < 0: # rass not found
        return l

    return l[:i] + l[i+7:]

"""
goal: create a dataset that contains all texts that contain "RASS".
      create a copy of it that has rass filtered.
      compare them by 10 fold stratified cross validation.
"""

df = pd.read_csv("../../data/clean/labels_nearest_all.csv")

df['diff'] = (df['label_time'] - df['text_time']).abs()    
df_filter = ((df['text_varid'] == 22085815) # Visite_ZNS
            & (df['label_varid'] == 22086158) # RASS
            & (df['diff'] <= 45*60)  # 45 mins
            & (df['text'].str.contains('rass', case=False))
        )

df = df[df_filter]
out_rows = []

for n_samples in [1000, 2000, 3000]:
    for filter_rass in [False, True]:
        svr = SVRmodel.get_SVR()

        # use a fixed random seed so the two estimators 
        # are tested/trained on the exact same pairs,
        # with or without 'RASS':
        df_sample = df.sample(int(n_samples*1.2), random_state=42)

        if filter_rass:
            df_sample['text'] = df_sample['text'].apply(filter_rass_occurences, 1)

        scores = cross_validate(
            estimator = svr, 
            X = df_sample['text'].astype('U'), 
            y = df_sample['label'].astype(int),
            scoring = 'neg_mean_absolute_error',
            cv = 6,
            n_jobs = -1,
            verbose = 2
        )['test_score']

        out_rows.extend([
            {
                'train_size': n_samples,
                'filter_rass': filter_rass,
                'mae': -score
            } for score in scores
        ])

df = pd.DataFrame(out_rows)
df.to_csv('SVM_performance_RASS_NORASS.csv', index=False)