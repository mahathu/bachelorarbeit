# wichtige Erkenntnisse:
schon SVM performance nach word2vec vectorization sehr gut: [-0.95293017 -0.93870698 -0.97874304 -0.96000418 -0.96607399]

je größer word_min_count (minimale vorkommen von wort, um von w2v berücksichtigt zu werden), desto größer die gefahr,
dass es texte gibt, die ausschließlich unbekannte worte enthalten. insbesondere der fall, wenn text nur ein wort enthält,
und dieses auch noch falsch geschrieben ist.

# Pipeline:

## Preprocessing: (preprocess_texts.py)
1.1) Tokenization **(done)**
1.2) Stopwörter filtern **(done)**
1.3) Spell Corrections

## Text Modeling:
2.1) Vectorization **(done)**
    * mithilfe von word2vec skip-gram, 100 dimensionen (50 dim genauso gut scheinbar) **(done)**
2.2) (Data Cleansing)
    * samples in verschiedene cluster einordnen. samples, die im falschen cluster landen, aus trainingsdaten rausnehmen

## Prediction Model:
3.1) ELM bauen
    * 50 knoten in input layer, so viele wie word2vec dimensionen ausgibt
    * 25 knoten in hidden layer?
    * 1 knoten output layer: linear activation function zwischen -5 und 4?