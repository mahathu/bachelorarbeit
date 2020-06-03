# Analysis for perf_reports/performance_SGDRegression_r2_2.csv

## Best parameter combinations:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 123 |              0.577134 | char       | (1,9)         | yes          | False            | squared_loss | l2             |       0.0001 | constant             |
| 159 |              0.574091 | char       | (1,9)         | yes          | False            | squared_loss | l2             |       1e-05  | constant             |
| 161 |              0.573429 | char       | (1,9)         | yes          | False            | squared_loss | elasticnet     |       1e-05  | constant             |
| 157 |              0.572653 | char       | (1,9)         | yes          | False            | squared_loss | l1             |       1e-05  | constant             |
| 197 |              0.571819 | char       | (1,9)         | yes          | False            | squared_loss | elasticnet     |       1e-06  | constant             |
| 195 |              0.571647 | char       | (1,9)         | yes          | False            | squared_loss | l2             |       1e-06  | constant             |
| 193 |              0.571334 | char       | (1,9)         | yes          | False            | squared_loss | l1             |       1e-06  | constant             |
| 177 |              0.570785 | char       | (1,9)         | yes          | False            | huber        | l2             |       1e-05  | optimal              |
| 125 |              0.568497 | char       | (1,9)         | yes          | False            | squared_loss | elasticnet     |       0.0001 | constant             |
| 122 |              0.565308 | char       | (1,9)         | yes          | True             | squared_loss | l2             |       0.0001 | constant             |

## Performance by parameter:

|analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.5771| -8686060078680853504.0000|


|ngram_range |max r2 |mean r2 |
|---|---|---|
|(1,9)           | 0.5771| -8686060078680853504.0000|


|stop_words |max r2 |mean r2 |
|---|---|---|
|yes             | 0.5771| -8686060078680853504.0000|


|tfidf__use_idf |max r2 |mean r2 |
|---|---|---|
|False           | 0.5771| -12058086711386073088.0000|
|True            | 0.5653| -5314033445975631872.0000|


|sgd__loss |max r2 |mean r2 |
|---|---|---|
|squared_loss    | 0.5771| -17372120157361704960.0000|
|huber           | 0.5708| -0.0451|


|sgd__penalty |max r2 |mean r2 |
|---|---|---|
|l2              | 0.5771| -2135187048139034.2500|
|elasticnet      | 0.5734| -12736250638572702.0000|
|l1              | 0.5727| -26043308798355845120.0000|


|sgd__alpha |max r2 |mean r2 |
|---|---|---|
|0.0001          | 0.5771| -17090815593359951872.0000|
|1e-05           | 0.5741| -14597742226364205056.0000|
|1e-06           | 0.5718| -20427802652233056256.0000|
|0.001           | 0.5271| -127904464.6254|
|0.01            | 0.3747| -0.0347|
|0.1             | 0.1171| -0.1559|


|sgd__learning_rate |max r2 |mean r2 |
|---|---|---|
|constant        | 0.5771| 0.2100|
|optimal         | 0.5708| -26058180236042559488.0000|
|invscaling      | 0.5004| 0.0246|


## Best parameter combination per parameter value:


### Best parameter combinations for analyzer


#### analyzer = char:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 123 |              0.577134 | char       | (1,9)         | yes          | False            | squared_loss | l2             |       0.0001 | constant             |

**Range: 0.0000**

---

### Best parameter combinations for ngram_range


#### ngram_range = (1,9):

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 123 |              0.577134 | char       | (1,9)         | yes          | False            | squared_loss | l2             |       0.0001 | constant             |

**Range: 0.0000**

---

### Best parameter combinations for stop_words


#### stop_words = yes:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 123 |              0.577134 | char       | (1,9)         | yes          | False            | squared_loss | l2             |       0.0001 | constant             |

**Range: 0.0000**

---

### Best parameter combinations for tfidf__use_idf


#### tfidf__use_idf = True:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 122 |              0.565308 | char       | (1,9)         | yes          | True             | squared_loss | l2             |       0.0001 | constant             |
#### tfidf__use_idf = False:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 123 |              0.577134 | char       | (1,9)         | yes          | False            | squared_loss | l2             |       0.0001 | constant             |

**Range: 0.0118**

---

### Best parameter combinations for sgd__loss


#### sgd__loss = squared_loss:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 123 |              0.577134 | char       | (1,9)         | yes          | False            | squared_loss | l2             |       0.0001 | constant             |
#### sgd__loss = huber:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss   | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:------------|:---------------|-------------:|:---------------------|
| 177 |              0.570785 | char       | (1,9)         | yes          | False            | huber       | l2             |        1e-05 | optimal              |

**Range: 0.0063**

---

### Best parameter combinations for sgd__penalty


#### sgd__penalty = l1:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 157 |              0.572653 | char       | (1,9)         | yes          | False            | squared_loss | l1             |        1e-05 | constant             |
#### sgd__penalty = l2:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 123 |              0.577134 | char       | (1,9)         | yes          | False            | squared_loss | l2             |       0.0001 | constant             |
#### sgd__penalty = elasticnet:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 161 |              0.573429 | char       | (1,9)         | yes          | False            | squared_loss | elasticnet     |        1e-05 | constant             |

**Range: 0.0045**

---

### Best parameter combinations for sgd__alpha


#### sgd__alpha = 0.1:

|    |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|---:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 15 |              0.117072 | char       | (1,9)         | yes          | False            | squared_loss | l2             |          0.1 | constant             |
#### sgd__alpha = 0.01:

|    |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|---:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 51 |              0.374676 | char       | (1,9)         | yes          | False            | squared_loss | l2             |         0.01 | constant             |
#### sgd__alpha = 0.001:

|    |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|---:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 87 |              0.527114 | char       | (1,9)         | yes          | False            | squared_loss | l2             |        0.001 | constant             |
#### sgd__alpha = 0.0001:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 123 |              0.577134 | char       | (1,9)         | yes          | False            | squared_loss | l2             |       0.0001 | constant             |
#### sgd__alpha = 1e-05:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 159 |              0.574091 | char       | (1,9)         | yes          | False            | squared_loss | l2             |        1e-05 | constant             |
#### sgd__alpha = 1e-06:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 197 |              0.571819 | char       | (1,9)         | yes          | False            | squared_loss | elasticnet     |        1e-06 | constant             |

**Range: 0.4601**

---

### Best parameter combinations for sgd__learning_rate


#### sgd__learning_rate = invscaling:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 147 |              0.500351 | char       | (1,9)         | yes          | False            | squared_loss | l2             |        1e-05 | invscaling           |
#### sgd__learning_rate = constant:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss    | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:-------------|:---------------|-------------:|:---------------------|
| 123 |              0.577134 | char       | (1,9)         | yes          | False            | squared_loss | l2             |       0.0001 | constant             |
#### sgd__learning_rate = optimal:

|     |   r2_performance_mean | analyzer   | ngram_range   | stop_words   | tfidf__use_idf   | sgd__loss   | sgd__penalty   |   sgd__alpha | sgd__learning_rate   |
|----:|----------------------:|:-----------|:--------------|:-------------|:-----------------|:------------|:---------------|-------------:|:---------------------|
| 177 |              0.570785 | char       | (1,9)         | yes          | False            | huber       | l2             |        1e-05 | optimal              |

**Range: 0.0768**

---
