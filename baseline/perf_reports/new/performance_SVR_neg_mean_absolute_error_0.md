# Analysis for perf_reports/new/performance_SVR_neg_mean_absolute_error_0.csv (n_samples=3000)

## Best parameter combinations:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 45 |                                   -1.09851 | char             | (2, 6)              | N/A                  | Yes (n=232)        | rbf           |       10 |
| 44 |                                   -1.09851 | char             | (2, 6)              | N/A                  | N/A                | rbf           |       10 |
| 41 |                                   -1.10074 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |
| 40 |                                   -1.10074 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
| 46 |                                   -1.10259 | char             | (2, 6)              | clean_and_stem_text  | N/A                | rbf           |       10 |

## Performance by parameter:

|vect__analyzer |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|char            | -1.0985| -1.3761|
|char_wb         | -1.1156| -1.3700|


|vect__ngram_range |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|(2, 6)          | -1.0985| -1.3604|
|(1, 5)          | -1.1007| -1.3558|
|(4, 9)          | -1.1047| -1.3817|
|(4, 7)          | -1.1063| -1.3766|
|(5, 12)         | -1.1137| -1.4038|


|vect__preprocessor |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|N/A             | -1.0985| -1.3744|
|clean_and_stem_text | -1.1026| -1.3743|


|vect__stop_words |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|Yes (n=232)     | -1.0985| -1.3744|
|N/A             | -1.0985| -1.3744|


|svr__kernel |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|rbf             | -1.0985| -1.3934|
|linear          | -1.1047| -1.3553|


|svr__C |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|10.0            | -1.0985| -1.1644|
|1.0             | -1.1047| -1.1422|
|0.1             | -1.2675| -1.4311|
|0.001           | -1.7519| -1.7597|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 44 |                                   -1.09851 | char             | (2, 6)              | N/A                  | N/A                | rbf           |       10 |
#### vect__analyzer = char_wb:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 176 |                                   -1.11558 | char_wb          | (2, 6)              | N/A                  | N/A                | rbf           |       10 |

**Range: 0.0171**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 5):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 41 |                                   -1.10074 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |
#### vect__ngram_range = (2, 6):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 45 |                                   -1.09851 | char             | (2, 6)              | N/A                  | Yes (n=232)        | rbf           |       10 |
#### vect__ngram_range = (4, 7):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 49 |                                   -1.10628 | char             | (4, 7)              | N/A                  | Yes (n=232)        | rbf           |       10 |
#### vect__ngram_range = (4, 9):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 32 |                                   -1.10471 | char             | (4, 9)              | N/A                  | N/A                | linear        |        1 |
#### vect__ngram_range = (5, 12):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 36 |                                   -1.11373 | char             | (5, 12)             | N/A                  | N/A                | linear        |        1 |

**Range: 0.0152**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 45 |                                   -1.09851 | char             | (2, 6)              | N/A                  | Yes (n=232)        | rbf           |       10 |
#### vect__preprocessor = clean_and_stem_text:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 47 |                                   -1.10259 | char             | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | rbf           |       10 |

**Range: 0.0041**

---

### Best parameter combinations for vect__stop_words


#### vect__stop_words = N/A:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 44 |                                   -1.09851 | char             | (2, 6)              | N/A                  | N/A                | rbf           |       10 |
#### vect__stop_words = Yes (n=232):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 45 |                                   -1.09851 | char             | (2, 6)              | N/A                  | Yes (n=232)        | rbf           |       10 |

**Range: 0.0000**

---

### Best parameter combinations for svr__kernel


#### svr__kernel = rbf:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 44 |                                   -1.09851 | char             | (2, 6)              | N/A                  | N/A                | rbf           |       10 |
#### svr__kernel = linear:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 32 |                                   -1.10471 | char             | (4, 9)              | N/A                  | N/A                | linear        |        1 |

**Range: 0.0062**

---

### Best parameter combinations for svr__C


#### svr__C = 1.0:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 32 |                                   -1.10471 | char             | (4, 9)              | N/A                  | N/A                | linear        |        1 |
#### svr__C = 10.0:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 44 |                                   -1.09851 | char             | (2, 6)              | N/A                  | N/A                | rbf           |       10 |
#### svr__C = 0.1:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 201 |                                    -1.2675 | char_wb          | (2, 6)              | N/A                  | Yes (n=232)        | linear        |      0.1 |
#### svr__C = 0.001:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 219 |                                   -1.75186 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |    0.001 |

**Range: 0.6533**

---
