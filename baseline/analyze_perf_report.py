import os
import pandas as pd
import numpy as np
from termcolor import cprint

filenames = ['perf_reports/performance_SVR_r2_0.csv']
perf_metric = "R^2"
for fn in filenames:
    out_file_name = fn.split('.')[0]+".md"
    df = pd.read_csv(fn)
    df.drop(['estimator', 'scoring_method', 'performance_std'], axis=1, inplace=True)
    
    out_str = f"# Analysis for {fn}\n\n"

    cprint("### Top parameters: ###", "green")
    print(df.sort_values('performance_mean', ascending=False).head(5))
    out_str += f"## Best parameter combinations (measured by {perf_metric}):\n\n"
    out_str += df.sort_values('performance_mean', ascending=False).head(10).to_markdown()
    print()
    out_str += "\n\n"

    print("Analysis for "+fn)

    out_str += "## Performance by parameter:\n\n"

    tuned_params = df.columns[1:]
    for param in tuned_params:
        unique_vals = df.sort_values('performance_mean', ascending=False)[param].unique()
        cprint(f"#### {param:18} ({len(unique_vals):2} unique values) ####", "green")

        #out_str += f"**{param:18} ({len(unique_vals):2} unique values)** \n\n"
        out_str += f"|{param} |max {perf_metric} |mean {perf_metric} |\n|---|---|---|\n"

        for val in filter(lambda v: type(v) != float or not np.isnan(v), unique_vals):
            perf_mean = df[ df[param]==val ]['performance_mean'].mean()
            perf_max = df[ df[param]==val ]['performance_mean'].max()

            print(f"{str(val):15} - best: {perf_mean:5.4f}")
            out_str += f"|{str(val):15} | {perf_max:5.4f}| {perf_mean:5.4f}|\n"
        print()
        out_str += "\n\n"

    print(50*"#"+"\n\n")

    cprint("### Best parameter combination per parameter: ###", "green")
    out_str += "## Best parameter combination per parameter value:\n\n"

    for param in tuned_params:
        unique_vals = df[param].unique()
        perfs = []
        out_str += f"\n### Best parameter combinations for {param}\n\n"
        for val in filter(lambda v: type(v) != float or not np.isnan(v), unique_vals):
            cprint(f"{param} = {val}", attrs=['bold'])
        
            out_str += f"\n#### {param} = {val}:\n\n"
            filtered_df = df[df[param]==val]
            print(filtered_df.sort_values('performance_mean', ascending=False).head(1).to_markdown())
            out_str += filtered_df.sort_values('performance_mean', ascending=False).head(1).to_markdown()
            
            perfs.append(filtered_df['performance_mean'].max())
        range = max(perfs) - min(perfs)
        cprint(f"Range for {param}: {range:5.4f}", "cyan")
        out_str += f"\n\n**Range: {range:5.4f}**\n\n---\n"

    with open(out_file_name, "w") as f:
        f.write(out_str)
    print("Saved output to "+out_file_name)