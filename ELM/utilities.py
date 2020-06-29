import pandas as pd
from string import ascii_letters, digits
#from nltk import bigrams
from termcolor import colored

allowed_chars = set(ascii_letters + digits + 'öäüßÖÄÜẞ =-%')
stop_words = set("""pat -pat patient patientin - sich zu hat und
    weiter weiterhin weitere weiteren weiteres weiterer bitte
    """.split())

def clean_text(s, remove_stop_words=True):
    """remove special characters and return lowercase text"""
    if type(s) is float: # some elements in Visite_ZNS are "nan"
        return ""
    
    s.replace('4/4', '44')
    s.replace('/', '/ ') # extra leerzeichen, sodass Worte die
                         # vorher durch '/' getrennt waren nicht
                         # zu einem gemeinsamen Token werden

    filtered_str = ''.join(filter(lambda ch: ch in allowed_chars, s.lower()))
    tokens = filtered_str.split()

    if not remove_stop_words:
        return " ".join(tokens) # remove multiple whitespaces in a row

    tokens = [word.replace('=', '') for word in tokens if not word in stop_words] #removes stop words from tokens and '=' from individual tokens
    return " ".join(tokens)

def get_ngrams(s, ngram_range=1):
    """return a list of word ngrams from string"""
    # tokens = s.split()
    # return filter(lambda token: len(token)>1, tokens)
    # return bigrams(s.split()) # NLTK bigrams method
    words = s.split()
    return [' '.join(words[i:i+ngram_range]) for i in range(len(words)-1)]

def preprocess_texts(filepath, v_id):
    """
    filepath should be a csv file containing the relevant columns:
    text_varid, text_time, text, label_varid, label_time, label

    Return value of the function is a dataframe containing cleaned
    texts for the given var_id.
    """
    pd.options.mode.chained_assignment = None #suppress false-positive warnings

    var_id_names = {
        20512769: "GCS",
        22086158: "RASS",
    }
    v_id_name = var_id_names.get(v_id, "UNKNOWN_VARID")

    print(f"Cleaning entries for {v_id_name}...", end=' ', flush=True)
    df = pd.read_csv(filepath)

    df_v = df[df['label_varid'] == v_id]

    df_v['time_diff'] = (df_v['text_time'] - df_v['label_time']).abs()

    # tokenization:
    df_v['text'] = df_v['text'].apply(clean_text)
    df_v['text'] = df_v['text'].astype(str)

    n_pairs = len(df_v)

    df_v = df_v[df_v['text'] != ''] # remove rows with empty texts
    df_v = df_v[df_v['text'] != 'nan'] 

    out_file = f'data/pairs_{v_id_name}.csv'
    df_v.to_csv(out_file, index=False)

    print(colored('Done', 'green'))
    print(f"Dataframe saved to {out_file}. ({n_pairs} rows in total, {n_pairs-len(df_v)} empty rows were filtered)")

    return df_v