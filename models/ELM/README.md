# wichtige Erkenntnisse:
schon SVM performance nach word2vec vectorization sehr gut: [-0.95293017 -0.93870698 -0.97874304 -0.96000418 -0.96607399]

je größer word_min_count (minimale vorkommen von wort, um von w2v berücksichtigt zu werden), desto größer die gefahr,
dass es texte gibt, die ausschließlich unbekannte worte enthalten. insbesondere der fall, wenn text nur ein wort enthält,
und dieses auch noch falsch geschrieben ist.

Beim spell check ist ein "naiver" Ansatz sicherer. nur fehler der entfernung 1 korrigieren
'pipillen' > pupillen
'dadruch' > dadurch

# Ergebnis mit ELM:


# Pipeline:

## Preprocessing: (preprocess_texts.py)
1.1) Tokenization **(done)**
1.2) Stopwörter filtern **(done)**
1.3) Spell Corrections

## Text Modeling:
2.1) Vectorization **(done)**
    * mithilfe von word2vec skip-gram, 100 dimensionen (50 dim genauso gut scheinbar) **(done)**

## Prediction Model:
3.1) ELM bauen
    * 50 knoten in input layer, so viele wie word2vec dimensionen ausgibt
    * 25 knoten in hidden layer (?)