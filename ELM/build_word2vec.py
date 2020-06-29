import pandas as pd
from gensim.models import Word2Vec
from termcolor import colored
from datetime import datetime

def build_w2v_model(df, window_size=5, dimensions=100, word_min_count=2, epochs=30, use_skipgrams=1):
    """Builds a word2vec model based on the texts that appear
    in the dataframe. The input file should have a 'text'
    column containing all the texts. The model is saved in a
    file and returned by the function."""

    print("Processing input file...", end=' ', flush=True)
    df['text'] = df['text'].astype(str)
    texts = [t.split() for t in df['text']] #a list of lists, containing separate words
    print(colored('Done', 'green'))

    # all_words = [word for text in texts for word in text]
    # n_unique_words = len(set(all_words))
    # print(colored(f"{n_unique_words} unique words seen, {len(all_words)} in total.", 'cyan'))

    print("Setting up model...", end=' ', flush=True)
    model = Word2Vec(min_count=word_min_count, sg=use_skipgrams, workers=4, size=dimensions, window=window_size)
    print(colored('Done', 'green'))

    print("Building vocabulary...", end=' ', flush=True)
    model.build_vocab(texts, progress_per=5000)
    print(colored('Done', 'green'))

    print(f"Training model for {epochs} epochs...", end=' ', flush=True)
    model.train(texts, total_examples=model.corpus_count, epochs=epochs)
    #model can't be trained any further after this:
    model.wv.init_sims(replace=True) # https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Word2VecKeyedVectors.init_sims
    print(colored('Done', 'green'))

    date_str = datetime.now().strftime("%m%d%y")
    fn = f'data/w2v_models/w2v_{date_str}_{window_size}w_{dimensions}d_{word_min_count}min_{epochs}e_{use_skipgrams}sg.model'
    model.save(fn)
    print(colored("Saved model to "+fn, 'green'))

    return model