import pandas as pd
from os.path import isfile
from nltk.stem import SnowballStemmer
from termcolor import cprint
from sklearn.model_selection import cross_val_score, cross_validate, ShuffleSplit
import re

COLOR_OUTPUT_ENABLE = True

var_ids = {
    22086067: "Vigilanz",
    22085897: "Ramsay",
    22086170: "BPS-Bewertung",
    20512801: "BPS",
    22086172: "NRS/VAS Bedingungen",
    22085911: "NRS/VAS",
    20512802: "DDS",
    20512769: "GCS",
    22086169: "CAM-ICU",
    22086158: "RASS",
    22085815: "Visite_ZNS",
    22085836: "Visite_Pflege",
    22085820: "Visite_Oberarzt",
}

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

def test_estimator(estimator, X_col, y_col, scoring_methods, n_cv_splits=5):
    cross_val_split = ShuffleSplit(n_splits=n_cv_splits, test_size=.25)

    '''this would train a new model for each CV fold and
    each scoring method and thus can be done much faster!'''
    # for scoring_method in scoring_methods:
    #     scores = cross_val_score(estimator, X_col, y_col, cv=cross_val, scoring=scoring_method)
    #     all_scores.append((scores.mean(), scores.std()))
    scores = cross_validate(estimator, X_col, y_col,
        cv=cross_val_split,
        scoring=scoring_methods
    )

    mean_scores = {
        key[5:] if key.startswith('test_') else key: (value.mean(), value.std())
            for key, value in scores.items()
    }
    return mean_scores

def plot_performance_by_n_samples():
    pass
    #https://scikit-learn.org/stable/auto_examples/model_selection/plot_multi_metric_evaluation.html