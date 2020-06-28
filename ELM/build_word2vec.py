import pandas as pd
from gensim.models import Word2Vec

print("Reading input file...", end=' ')
df = pd.read_csv('data/pairs_RASS.csv')
print("Done")

df['text'] = df['text'].astype(str)

texts = [t.split() for t in df['text']]

print("Building model...", end=' ', flush=True)
model = Word2Vec(min_count=2, sg=1, workers=4, size=100) #sg=1: use skip-grams #100 dimensions
print("Done")

print("Building vocabulary...", end=' ', flush=True)
model.build_vocab(texts, progress_per=100)
print("Done")

print("Training model...", end=' ', flush=True)
model.train(texts, total_examples=model.corpus_count, epochs=30, report_delay=1)
print("Done")

#model can't be trained any further after this:
model.wv.init_sims(replace=True) # https://radimrehurek.com/gensim/models/keyedvectors.html#gensim.models.keyedvectors.Word2VecKeyedVectors.init_sims

print(model.wv.most_similar(positive=["sediert"]))

model.save('w2v.model')