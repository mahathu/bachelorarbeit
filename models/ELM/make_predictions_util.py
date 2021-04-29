from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVR
import hpelm

def predict_baseline(train_df, test_df):
    cv = CountVectorizer(
        analyzer='char',
        ngram_range=(1,5),
        preprocessor=lambda s: s.lower()
    )
    clf = Pipeline([
        ('vect', cv),
        ('tfidf', TfidfTransformer()),
        ('svr', SVR(cache_size=1024, C=10)), #das sind wirklich die besten Hyperparameter!
    ])

    clf.fit(train_df['text'], train_df['label'])
    return clf.predict(test_df['text'])

def predict_svr_with_w2v(X_matrix_train, train_labels, X_matrix_test):
    clf = SVR(cache_size=1024, C=10)
    clf.fit(X_matrix_train, train_labels)
    return clf.predict(X_matrix_test)

def predict_elm(X_matrix_train, train_labels, X_matrix_test):
    n_input_columns = len(X_matrix_train.columns)
    n_neurons = int(1 * n_input_columns)

    X_matrix_train = X_matrix_train.to_numpy()
    X_matrix_test = X_matrix_test.to_numpy()
    train_labels = train_labels.to_numpy()

    model = hpelm.HPELM(n_input_columns, 1)
    model.add_neurons(n_neurons, 'tanh')

    model.train(X_matrix_train, train_labels)

    return model.predict(X_matrix_test).flatten()