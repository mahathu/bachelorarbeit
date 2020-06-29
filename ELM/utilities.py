import numpy as np
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

def get_x_y(df, input_varid, output_varid, max_min_between, max_samples=0):
    """Returns X and y columns from dataframe for given
    input and output varids"""

    df_filter = ((df['text_varid'] == input_varid) 
                & (df['label_varid'] == output_varid) 
                & (df['time_diff'] <= (max_min_between*60)))

    df = df[df_filter].reset_index() # remove unwanted rows
    
    if max_samples > 0: # maximum n of training pairs. Should only be used to speed up testing
        df = df.sample(max_samples) #randomly chose max_samples samples
        print(f"Only considering the first {max_samples} samples!")

    if output_varid == 22086169: # CAM-ICU
        df = df.replace({'label': {
            'neg.': 0,
            'pos.': 1,
            'unmögl.': 2,
        }})

    # reset index for y column. This way, we can more easily filter
    # y columns out for such rows where the x matrix is empty (due
    # to the input text containing no known words.)
    return df['text'], df['label'].astype(int)

def transform_texts(model, texts_series):
    """Transforms a series of input texts to 
    their representations as n-dimensional
    vectors through the w2v model.
    
    Return value is a pandas dataframe with
    1 row per input text, and the number of
    columns equivalent to the word2vec vector
    dimensions."""

    # falls ein unbekanntes wort vorkommt, dieses ignorieren, d.h. auch
    # nicht zur gesamtzahl der worte zählen, durch die am Ende geteilt wird
    
    n_dims = model.layer1_size # 100 by default
    text_vectors = []
    n_broken_rows = 0
    n_unknown_words = 0
    
    for j, text in enumerate(texts_series):
        tokens = text.split()
    
        known_words = [w for w in tokens if w in model.wv] # only consider words in the dictionary of the w2v model
        if len(tokens) != len(known_words):
            # print(f"Text: {text} ({len(tokens)} total, {len(known_words)} known)")
            n_unknown_words += len(tokens) - len(known_words)
        if len(known_words) == 0:
            print(colored(f'"{text}" enthält 0 bekannte Wörter!', 'red'))
            
            text_vectors.append([np.nan for i in range(n_dims)])
            n_broken_rows += 1
            continue # to next text
        
        text_vector = [
            np.mean([model.wv[word][i] for word in known_words])
            for i in range(n_dims)
        ]
        text_vectors.append(text_vector)
    
    df = pd.DataFrame(text_vectors)
    df.to_csv(f'data/text_features_{n_dims}dim.csv', index=False)

    print(f"{len(texts_series)} texts vectorized in total ({n_unknown_words/len(texts_series):.3f} mean unknown words per text.)")
    c = 'green' if n_broken_rows == 0 else 'red'
    print(colored(f"{n_broken_rows} invalid input texts!", c))

    return df