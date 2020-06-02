# Analysis for perf_reports/performance_SGDRegression_r2_1.csv

## Best parameter combinations (measured by r2):

|    |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    |
|---:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|
|  1 |              0.498259 | char       | (1,9)         | yes          | False            | squared_loss |
|  0 |              0.493757 | char       | (1,9)         | yes          | True             | squared_loss |
|  3 |             -0.25219  | char       | (1,9)         | yes          | False            | huber        |
|  2 |             -0.321198 | char       | (1,9)         | yes          | True             | huber        |

## Performance by parameter:

|analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.4983| 0.1047|


|ngram_range |max r2 |mean r2 |
|---|---|---|
|(1,9)           | 0.4983| 0.1047|


|stop_words |max r2 |mean r2 |
|---|---|---|
|yes             | 0.4983| 0.1047|


|tfidf__use_idf |max r2 |mean r2 |
|---|---|---|
|False           | 0.4983| 0.1230|
|True            | 0.4938| 0.0863|


|sgd__loss |max r2 |mean r2 |
|---|---|---|
|squared_loss    | 0.4983| 0.4960|
|huber           | -0.2522| -0.2867|


## Best parameter combination per parameter value:


### Best parameter combinations for analyzer


#### analyzer = char:

|    |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    |
|---:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|
|  1 |              0.498259 | char       | (1,9)         | yes          | False            | squared_loss |

**Range: 0.0000**

---

### Best parameter combinations for ngram_range


#### ngram_range = (1,9):

|    |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    |
|---:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|
|  1 |              0.498259 | char       | (1,9)         | yes          | False            | squared_loss |

**Range: 0.0000**

---

### Best parameter combinations for stop_words


#### stop_words = yes:

|    |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    |
|---:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|
|  1 |              0.498259 | char       | (1,9)         | yes          | False            | squared_loss |

**Range: 0.0000**

---

### Best parameter combinations for tfidf__use_idf


#### tfidf__use_idf = True:

|    |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    |
|---:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|
|  0 |              0.493757 | char       | (1,9)         | yes          | True             | squared_loss |
#### tfidf__use_idf = False:

|    |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    |
|---:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|
|  1 |              0.498259 | char       | (1,9)         | yes          | False            | squared_loss |

**Range: 0.0045**

---

### Best parameter combinations for sgd__loss


#### sgd__loss = squared_loss:

|    |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    |
|---:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|
|  1 |              0.498259 | char       | (1,9)         | yes          | False            | squared_loss |
#### sgd__loss = huber:

|    |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss   |
|---:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:------------|
|  3 |              -0.25219 | char       | (1,9)         | yes          | False            | huber       |

**Range: 0.7504**

---
