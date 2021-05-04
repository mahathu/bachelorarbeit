import pandas as pd

df = pd.read_csv("../data/clean/all_scores.csv")

var_ids = {
    22085815: "Visite_ZNS",
    22085836: "Visite_Pflege",
    22085820: "Visite_Oberarzt",
}

def count_rass_mentions(series):
    rass_n = 0
    for text in series:
        if type(text) is float:
            continue

        idx = text.find('rass')
        if idx >= 0: # "RASS"  found in text
            rass_n += 1
        
    return rass_n

for v_id in var_ids:
    df_v = df[df['VarID'] == v_id]
    df_v.dropna(inplace=True) #remove nan vals from Visite_Pflege

    rass_mentions = count_rass_mentions(df_v['wert'].apply(lambda s: s.lower()))
    total_texts = len(df_v)
    print(f"{var_ids[v_id]}: {total_texts} Texte, {rass_mentions} enthalten RASS ({rass_mentions/total_texts*100:.2f}%)")