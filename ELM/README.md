SVM performance nach word2vec vectorization: [-0.95293017 -0.93870698 -0.97874304 -0.96000418 -0.96607399]

# Pipeline:

## Preprocessing: (preprocess_texts.py)
1.1) Tokenization
1.2) (Stopwörter filtern)
1.3) (Stemming/Suffixe entfernen)

## Text Modeling:
2.1) Vectorization 
    * mithilfe von word2vec skip-gram, 100 dimensionen
2.2) (Data Cleansing)
    * samples in verschiedene cluster einordnen. samples, die im falschen cluster landen, aus trainingsdaten rausnehmen

## Prediction Model:
3.1) ELM bauen
    * 100 knoten in input layer, so viele wie word2vec dimensionen ausgibt
    * 50 knoten in hidden layer
    * 1 knoten output layer: linear activation function zwischen -5 und 4?