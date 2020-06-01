# Analysis for perf_reports/performance_SVR_r2_0.csv

## Best parameter combinations (measured by R^2):

|     |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|----:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
|  77 |           0.594055 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |       10 |
|  76 |           0.586841 | char             | (1, 9)              | Yes (n=232)        | True             | rbf           | scale        |       10 |
|  81 |           0.586284 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |      100 |
|  80 |           0.585687 | char             | (1, 9)              | Yes (n=232)        | True             | rbf           | scale        |      100 |
|  73 |           0.581828 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |        1 |
| 120 |           0.580877 | char             | (1, 9)              | Yes (n=232)        | True             | linear        | nan          |        1 |
| 121 |           0.573268 | char             | (1, 9)              | Yes (n=232)        | False            | linear        | nan          |        1 |
|  72 |           0.569737 | char             | (1, 9)              | Yes (n=232)        | True             | rbf           | scale        |        1 |
|  32 |           0.564018 | word             | (1, 3)              | No                 | False            | rbf           | scale        |       10 |
|  56 |           0.562565 | word             | (1, 3)              | No                 | False            | rbf           | scale        |      100 |

## Performance by parameter:

|vect__analyzer |max R^2 |mean R^2 |
|---|---|---|
|char            | 0.5941| 0.3612|
|word            | 0.5640| 0.3453|


|vect__ngram_range |max R^2 |mean R^2 |
|---|---|---|
|(1, 9)          | 0.5941| 0.3612|
|(1, 3)          | 0.5640| 0.3452|
|(1, 1)          | 0.5478| 0.3681|
|(1, 6)          | 0.5424| 0.3227|


|vect__stop_words |max R^2 |mean R^2 |
|---|---|---|
|Yes (n=232)     | 0.5941| 0.3473|
|No              | 0.5640| 0.3480|


|tfidf__use_idf |max R^2 |mean R^2 |
|---|---|---|
|False           | 0.5941| 0.3564|
|True            | 0.5868| 0.3388|


|svr__kernel |max R^2 |mean R^2 |
|---|---|---|
|rbf             | 0.5941| 0.2935|
|linear          | 0.5809| 0.4558|


|svr__gamma |max R^2 |mean R^2 |
|---|---|---|
|scale           | 0.5941| 0.5448|
|auto            | 0.4421| 0.0421|


|svr__C |max R^2 |mean R^2 |
|---|---|---|
|10              | 0.5941| 0.3486|
|100             | 0.5863| 0.3507|
|1               | 0.5818| 0.3435|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = word:

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 32 |           0.564018 | word             | (1, 3)              | No                 | False            | rbf           | scale        |       10 |
#### vect__analyzer = char:

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 77 |           0.594055 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |       10 |

**Range: 0.0300**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 1):

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 30 |           0.547849 | word             | (1, 1)              | No                 | False            | rbf           | scale        |       10 |
#### vect__ngram_range = (1, 3):

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 32 |           0.564018 | word             | (1, 3)              | No                 | False            | rbf           | scale        |       10 |
#### vect__ngram_range = (1, 6):

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 28 |           0.542433 | word             | (1, 6)              | No                 | True             | rbf           | scale        |       10 |
#### vect__ngram_range = (1, 9):

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 77 |           0.594055 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |       10 |

**Range: 0.0516**

---

### Best parameter combinations for vect__stop_words


#### vect__stop_words = No:

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 32 |           0.564018 | word             | (1, 3)              | No                 | False            | rbf           | scale        |       10 |
#### vect__stop_words = Yes (n=232):

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 77 |           0.594055 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |       10 |

**Range: 0.0300**

---

### Best parameter combinations for tfidf__use_idf


#### tfidf__use_idf = True:

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 76 |           0.586841 | char             | (1, 9)              | Yes (n=232)        | True             | rbf           | scale        |       10 |
#### tfidf__use_idf = False:

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 77 |           0.594055 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |       10 |

**Range: 0.0072**

---

### Best parameter combinations for svr__kernel


#### svr__kernel = rbf:

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 77 |           0.594055 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |       10 |
#### svr__kernel = linear:

|     |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   |   svr__gamma |   svr__C |
|----:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|-------------:|---------:|
| 120 |           0.580877 | char             | (1, 9)              | Yes (n=232)        | True             | linear        |          nan |        1 |

**Range: 0.0132**

---

### Best parameter combinations for svr__gamma


#### svr__gamma = scale:

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 77 |           0.594055 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |       10 |
#### svr__gamma = auto:

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 67 |           0.442051 | word             | (1, 1)              | Yes (n=232)        | False            | rbf           | auto         |      100 |

**Range: 0.1520**

---

### Best parameter combinations for svr__C


#### svr__C = 1:

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 73 |           0.581828 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |        1 |
#### svr__C = 10:

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 77 |           0.594055 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |       10 |
#### svr__C = 100:

|    |   performance_mean | vect__analyzer   | vect__ngram_range   | vect__stop_words   | tfidf__use_idf   | svr__kernel   | svr__gamma   |   svr__C |
|---:|-------------------:|:-----------------|:--------------------|:-------------------|:-----------------|:--------------|:-------------|---------:|
| 81 |           0.586284 | char             | (1, 9)              | Yes (n=232)        | False            | rbf           | scale        |      100 |

**Range: 0.0122**

---
