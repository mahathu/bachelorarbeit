# Analysis for perf_reports/new/performance_SVR_neg_mean_absolute_error_1.csv (n_samples=3000)

## Best parameter combinations:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 77 |                                   -1.79645 | char             | (5, 12)             | N/A                  | Yes (n=232)        | linear        |       10 |
| 76 |                                   -1.79645 | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |
| 73 |                                   -1.79646 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |
| 72 |                                   -1.79646 | char             | (4, 9)              | N/A                  | N/A                | linear        |       10 |
| 79 |                                   -1.7991  | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |

## Performance by parameter:

|vect__analyzer |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|char            | -1.7965| -2.6969|
|char_wb         | -1.8162| -2.6458|


|vect__ngram_range |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|(5, 12)         | -1.7965| -2.7933|
|(4, 9)          | -1.7965| -2.6977|
|(1, 5)          | -1.8004| -2.6258|
|(2, 6)          | -1.8143| -2.6334|
|(4, 7)          | -1.8175| -2.6948|


|vect__preprocessor |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|N/A             | -1.7965| -2.6847|
|clean_and_stem_text | -1.7991| -2.6799|


|vect__stop_words |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|Yes (n=232)     | -1.7965| -2.6823|
|N/A             | -1.7965| -2.6823|


|svr__kernel |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|linear          | -1.7965| -2.5855|
|rbf             | -1.8004| -2.7791|


|svr__C |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|10.0            | -1.7965| -1.8648|
|1.0             | -1.8564| -2.0544|
|0.1             | -2.5400| -3.0416|
|0.001           | -3.7532| -3.7684|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 77 |                                   -1.79645 | char             | (5, 12)             | N/A                  | Yes (n=232)        | linear        |       10 |
#### vect__analyzer = char_wb:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 176 |                                   -1.81616 | char_wb          | (2, 6)              | N/A                  | N/A                | rbf           |       10 |

**Range: 0.0197**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 5):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 40 |                                   -1.80044 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
#### vect__ngram_range = (2, 6):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 44 |                                   -1.81433 | char             | (2, 6)              | N/A                  | N/A                | rbf           |       10 |
#### vect__ngram_range = (4, 7):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 68 |                                   -1.81749 | char             | (4, 7)              | N/A                  | N/A                | linear        |       10 |
#### vect__ngram_range = (4, 9):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 73 |                                   -1.79646 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |
#### vect__ngram_range = (5, 12):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 76 |                                   -1.79645 | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |

**Range: 0.0210**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 77 |                                   -1.79645 | char             | (5, 12)             | N/A                  | Yes (n=232)        | linear        |       10 |
#### vect__preprocessor = clean_and_stem_text:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 79 |                                    -1.7991 | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |

**Range: 0.0027**

---

### Best parameter combinations for vect__stop_words


#### vect__stop_words = N/A:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 76 |                                   -1.79645 | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |
#### vect__stop_words = Yes (n=232):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 77 |                                   -1.79645 | char             | (5, 12)             | N/A                  | Yes (n=232)        | linear        |       10 |

**Range: 0.0000**

---

### Best parameter combinations for svr__kernel


#### svr__kernel = rbf:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 41 |                                   -1.80044 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |
#### svr__kernel = linear:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 76 |                                   -1.79645 | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |

**Range: 0.0040**

---

### Best parameter combinations for svr__C


#### svr__C = 1.0:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 26 |                                   -1.85642 | char             | (2, 6)              | clean_and_stem_text  | N/A                | linear        |        1 |
#### svr__C = 10.0:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 76 |                                   -1.79645 | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |
#### svr__C = 0.1:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 203 |                                      -2.54 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |      0.1 |
#### svr__C = 0.001:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 219 |                                   -3.75316 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |    0.001 |

**Range: 1.9567**

---
