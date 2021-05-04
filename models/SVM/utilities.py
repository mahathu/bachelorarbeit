import pandas as pd
import numpy as np
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

def safe_filename(fn_base, ending):
    file_n = 0
    fn = f"{fn_base}_{file_n}.{ending}"
    while isfile(fn):
        wprint("Skipping file name: "+fn)
        file_n += 1
        fn = f"{fn_base}_{file_n}.{ending}"
    
    return fn

def brief_dict(d): #make dict look nicer in text output
    for key in d:
        if isinstance(d[key], list) and len(d[key]) > 20:
            d[key] = f"Yes (n={len(d[key])})"
    return d

def clean_text(text):
    pattern = re.compile('[^a-zA-Z0-9äöüÄÖÜß \.]', re.UNICODE)

    text = pattern.sub(' ', text) # remove special characters
    return text

def clean_and_stem_text(text):
    stemmer = SnowballStemmer('german')
    pattern = re.compile('[^a-zA-Z0-9äöüÄÖÜß \.]', re.UNICODE)

    text = pattern.sub(' ', text) # remove special characters
    text = ' '.join( [stemmer.stem(word) for word in text.split()] ) # stem words
    return text

def save_performance_report(estimator_name, regressor_obj, all_params, scoring_method, n_samples, fixed_params=None):
    #fixed params can be used to save hyperparams in columns that aren't actually tuned by GSCV.
    if not fixed_params:
        fixed_params={}
        
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
            if params[p]:
                if callable(params[p]):
                    params[p] = params[p].__name__
                row[idx] = params[p]

        df_rows.append(row)

    df = pd.DataFrame(df_rows, columns=df_colnames)

    out_file_name_base = f"perf_reports/perf_{estimator_name}_{scoring_method}"
    file_n = 0
    fn = f"{out_file_name_base}_{file_n}.csv"
    while isfile(fn):
        wprint("Skipping file name: "+fn)
        file_n += 1
        fn = f"{out_file_name_base}_{file_n}.csv"

    df.to_csv(fn, index=False, na_rep='N/A')
    sprint("Saved performance report to "+fn)
    if len(fixed_params)>0:
        iprint("Included fixed parameters:" + str([k for k in fixed_params]))

    save_perf_report_as_md(df, scoring_method, fn, n_samples)

def save_perf_report_as_md(df, scoring_method, fn, n_samples):
    perf_col_name = scoring_method+'_performance_mean'

    out_file_name = fn.split('.')[0]+".md"
    df.drop(['estimator', scoring_method+'_performance_std'], axis=1, inplace=True)

    out_str = f"# Analysis for {fn} (n_samples={n_samples})\n\n"

    out_str += f"## Best parameter combinations:\n\n"
    out_str += df.sort_values(perf_col_name, ascending=False).head(5).to_markdown()
    out_str += "\n\n"

    tuned_params = df.columns[1:]

    out_str += "## Performance by parameter:\n\n"
    for param in tuned_params:
        unique_vals = df.sort_values(perf_col_name, ascending=False)[param].unique()
        
        #out_str += f"**{param:18} ({len(unique_vals):2} unique values)** \n\n"
        out_str += f"|{param} |max {scoring_method} |mean {scoring_method} |\n|---|---|---|\n"

        for val in filter(lambda v: type(v) != float or not np.isnan(v), unique_vals):
            perf_mean = df[ df[param]==val ][perf_col_name].mean()
            perf_max = df[ df[param]==val ][perf_col_name].max()

            out_str += f"|{str(val):15} | {perf_max:5.4f}| {perf_mean:5.4f}|\n"
        out_str += "\n\n"

    out_str += "## Best parameter combination per parameter value:\n\n"

    for param in tuned_params:
        unique_vals = df[param].unique()
        perfs = []
        out_str += f"\n### Best parameter combinations for {param}\n\n"
        for val in filter(lambda v: type(v) != float or not np.isnan(v), unique_vals):        
            out_str += f"\n#### {param} = {val}:\n\n"
            filtered_df = df[df[param]==val]
            out_str += filtered_df.sort_values(perf_col_name, ascending=False).head(1).to_markdown()
            
            perfs.append(filtered_df[perf_col_name].max())
        d_range = max(perfs) - min(perfs)

        out_str += f"\n\n**Range: {d_range:5.4f}**\n\n---\n"

    with open(out_file_name, "w") as f:
        f.write(out_str)
    print("Saved output to "+out_file_name)

# =============================================================================

def test_estimator(estimator, X_col, y_col, test_size, scoring_methods):
    scores = cross_validate(estimator, X_col, y_col,
        cv=ShuffleSplit(n_splits=1, test_size=test_size),
        scoring=scoring_methods,
        #n_jobs = -1
    )

    return {
        key[5:] if key.startswith('test_') else key: (value.mean(), value.std())
            for key, value in scores.items()
    }


def get_x_y(df, input_varid, output_varid, max_min_between, min_min_between=0, max_samples=0):
    df['diff'] = (df['label_time'] - df['text_time']).abs()
    
    df_filter = ((df['text_varid'] == input_varid) 
                & (df['label_varid'] == output_varid) 
                & (df['diff'] <= (max_min_between*60)))
    #print(df_filter)
    # remove unwanted rows:
    df = df[df_filter]
    
    if max_samples>0: # maximum n of training pairs. Should only be used to speed up testing
        #df = df[:max_samples]
        df = df.sample(max_samples) #randomly chose max_samples samples
        #eprint(f"Only considering the first {max_samples} samples!")

    # remove irrelevant columns:
    # df = df[['text', 'label']]
    # if output_varid == 22086169: # CAM-ICU
    #     df = df.replace({'label': {
    #         'neg.': 0,
    #         'pos.': 1,
    #         'unmögl.': 2,
    #     }})

    return df['text'].astype('U'), df['label'].astype(int)


if __name__ == '__main__':
    # test clean_and_stem_text()
    text = "dieseröü täxtß sollte 9 898 (:):)) gecleaned sein und gestemmt laufen ruft schreit X*)'"
    print(clean_and_stem_text(text))