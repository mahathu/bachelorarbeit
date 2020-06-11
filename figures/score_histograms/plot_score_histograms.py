import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def abbreviate(s):
    s = str(s)
    if len(s) > 8:
        return(s[:6]+'...')
    return s

var_id_names = {
    22085897: "Ramsay Sedation Scale",
    22086170: "BPS-Bewertung",
    20512801: "Behavior Pain Scale",
    22086172: "NRS/VAS Bedingungen",
    22085911: "Visual Analogue Scale",
    20512802: "Delirium Detection Score",
    20512769: "Glasgow Coma Scale",
    22086169: "CAM-ICU",
    22086158: "Richmond Agitation Sedation Scale",
}

df = pd.read_csv('../../data/clean/all_scores.csv')
# pats = pd.read_csv('../../data/patienten/patienten_neu.csv', sep=';')
# pats['days'] = pats['time_in_ICU'] / 60 / 60 / 24
# print(pats.head())
# n_days = pats['days'].sum()
n_days = 9885.57639

for v_id in var_id_names:
    v_id_name = var_id_names[v_id]
    df_v = df[df['VarID'] == v_id]

    
    bar_vals = df_v['wert'].value_counts()

    print(f"{'='*80}\n{v_id_name} - n={len(bar_vals)}")    
    
    if all(x.isdigit() for x in bar_vals.index):
        u = df_v['wert'].unique().astype(int)
        u.sort()
        print(u)
        bar_vals.index = bar_vals.index.astype(int)
        mi = min(bar_vals.index)
        ma = max(bar_vals.index) + 1
        plt.xlim(mi-1,ma)
        if ma - mi < 15:
            plt.xticks(np.arange(mi,ma), np.arange(mi,ma))

    else:
        print(bar_vals)
    bar_vals = bar_vals.sort_index()

    x = bar_vals.index
    y = bar_vals.to_numpy()

    
    plt.bar(x, y)
    
    #plt.ylabel('Anzahl eingetragener Werte')
    plt.title(v_id_name)
    #plt.xlabel(v_id_name)
    
    #plt.show()
    
    fn = f"hist_{v_id_name}.png".replace('/','-').replace(' ','_')
    plt.savefig("out/"+fn, bbox_inches='tight', dpi=300)
    plt.clf() #clear figure
    plt.close() #close plot and release memory (in theory?)
    #break