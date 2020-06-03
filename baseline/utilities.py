import pandas as pd
from os.path import isfile
from nltk.stem import SnowballStemmer
from termcolor import cprint
from sklearn.model_selection import cross_val_score, ShuffleSplit
import re

COLOR_OUTPUT_ENABLE = True

# === printing functions ===
def iprint(s): # print information
    if not COLOR_OUTPUT_ENABLE:
        print(s)
        return
    cprint(s, "cyan")

def sprint(s): # print success
    if not COLOR_OUTPUT_ENABLE:
        print(s)
        return
    cprint(s, "green", attrs=['bold'])

def wprint(s): # print warning
    if not COLOR_OUTPUT_ENABLE:
        print(s)
        return
    cprint(s, "yellow")

def eprint(s): # print error
    if not COLOR_OUTPUT_ENABLE:
        print(s)
        return
    cprint(s, "red")

def clean_text(text):
    stemmer = SnowballStemmer('german')
    pattern = re.compile('[^a-zA-Z0-9äöüÄÖÜß \.]', re.UNICODE)

    text = pattern.sub(' ', text) # remove special characters
    text = ' '.join( [stemmer.stem(word) for word in text.split()] ) # stem words
    return text

def save_performance_report(estimator_name, regressor_obj, all_params, scoring_method, fixed_params={}):
    #fixed params can be used to save hyperparams in columns that aren't actually tuned by GSCV.

    means = regressor_obj.cv_results_['mean_test_score']
    stds = regressor_obj.cv_results_['std_test_score']
    df_rows = []
    df_colnames = ["estimator", scoring_method+"_performance_mean", scoring_method+"_performance_std"] + [*fixed_params] + all_params

    for mean, std, params in zip(means, stds, regressor_obj.cv_results_['params']):
        if 'vect__stop_words' in params and params['vect__stop_words']: # use a different string instead of printing the entire list
            params['vect__stop_words'] = f"Yes (n={len(params['vect__stop_words'])})"
        
        row = [estimator_name, mean, std] + [fixed_params[k] for k in fixed_params] + ['N/A' for p in all_params]

        for p in params:
            idx = all_params.index(p) + 3 + len(fixed_params)
            row[idx] = params[p]

        df_rows.append(row)

    df = pd.DataFrame(df_rows, columns=df_colnames)

    out_file_name_base = f"perf_reports/performance_{estimator_name}_{scoring_method}"
    file_n = 0
    #change to walrus operator!
    fn = f"{out_file_name_base}_{file_n}.csv"
    while isfile(fn):
        wprint("Skipping file name: "+fn)
        file_n += 1
        fn = f"{out_file_name_base}_{file_n}.csv"

    df.to_csv(fn, index=False)
    sprint("Saved performance report to "+fn)
    if len(fixed_params):
        iprint("Included fixed parameters:" + str([k for k in fixed_params]))

def test_estimator(estimator, X_col, y_col, scoring_methods):
    cross_val = ShuffleSplit(n_splits=5, test_size=.25)

    all_scores = []
    for scoring_method in scoring_methods:
        scores = cross_val_score(estimator, X_col, y_col, cv=cross_val, scoring=scoring_method)
        all_scores.append([scoring_method, scores.mean(), scores.std()])

    return all_scores