"""
AUTHOR: Peter Norvig
http://norvig.com/spell-correct.html
"""

import re
import pandas as pd
from collections import Counter
#from utilities import clean_text

def words(text): 
    return re.findall(r'\w+', text.lower())

WORDS_ALL = Counter(words(open('data/texts.txt').read())) #Counter is a special dict for counting
MIN_WORD_OCCURENCES = 3
common_misspellings = ['raas'] # filter such words that occure too often
for m in common_misspellings:
    del WORDS_ALL[m]

WORD_COUNTS = Counter({k: c for k, c in WORDS_ALL.items() if c >= 3})

def P(word, N=sum(WORD_COUNTS.values())): # used as key for max() function when suggesting a correction
    "Probability of `word`."
    return WORD_COUNTS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    """Generate possible spelling corrections for word.
    Only consider edits of max. distance 1
    """
    # possible_replacements = (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
    possible_replacements = (known([word]) or known(edits1(word)) or [word])
    # if len(possible_replacements)>1:
    #     print(f"\nCandidates: {possible_replacements}")
    return possible_replacements

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORD_COUNTS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyzöäüß'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]

    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

if __name__ == '__main__':
    # print(f"spell_checker.py was called directly, so I'm building a dictionary now.")

    # DICTIONARY_OUT_FILE = 'data/texts.txt'
    # CONSIDERED_VAR_IDS = [22085815, 22085836, 22085820] # Visite_{ZNS|Pflege|Oberarzt}

    # df = pd.read_csv('../data/clean/all_scores.csv')
    # n_rows_all = len(df)

    # df = df[df['VarID'].isin(CONSIDERED_VAR_IDS)]
    # print(f"{n_rows_all} rows read in total ({len(df)} relevant Var_IDs)")

    # out_strs = [clean_text(t, remove_stop_words=False) + '\n' for t in df['wert']]
    # with open(DICTIONARY_OUT_FILE, 'w') as f:
    #     f.writelines(out_strs)

    # print(f"Wrote to {DICTIONARY_OUT_FILE}.")
    pass