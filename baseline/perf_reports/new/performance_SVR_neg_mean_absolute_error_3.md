# Analysis for perf_reports/new/performance_SVR_neg_mean_absolute_error_3.csv (n_samples=3000)

## Best parameter combinations:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 75 |                                   -2.22122 | char             | (4, 9)              | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
| 74 |                                   -2.22122 | char             | (4, 9)              | clean_and_stem_text  | N/A                | linear        |       10 |
| 79 |                                   -2.22691 | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
| 78 |                                   -2.22691 | char             | (5, 12)             | clean_and_stem_text  | N/A                | linear        |       10 |
| 73 |                                   -2.23366 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |

## Performance by parameter:

|vect__analyzer |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|char            | -2.2212| -2.9900|
|char_wb         | -2.2901| -2.9341|


|vect__ngram_range |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|(4, 9)          | -2.2212| -2.9771|
|(5, 12)         | -2.2269| -3.0500|
|(4, 7)          | -2.2468| -2.9901|
|(2, 6)          | -2.2659| -2.9395|
|(1, 5)          | -2.2776| -2.9451|


|vect__preprocessor |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|clean_and_stem_text | -2.2212| -2.9645|
|N/A             | -2.2337| -2.9836|


|vect__stop_words |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|Yes (n=232)     | -2.2212| -2.9741|
|N/A             | -2.2212| -2.9741|


|svr__kernel |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|linear          | -2.2212| -2.8891|
|rbf             | -2.2901| -3.0590|


|svr__C |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|10.0            | -2.2212| -2.3314|
|1.0             | -2.3320| -2.6072|
|0.1             | -3.0587| -3.3507|
|0.001           | -3.6025| -3.6069|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 75 |                                   -2.22122 | char             | (4, 9)              | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
#### vect__analyzer = char_wb:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 179 |                                   -2.29007 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | rbf           |       10 |

**Range: 0.0689**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 5):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 63 |                                   -2.27758 | char             | (1, 5)              | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
#### vect__ngram_range = (2, 6):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 67 |                                   -2.26586 | char             | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
#### vect__ngram_range = (4, 7):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 71 |                                   -2.24682 | char             | (4, 7)              | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
#### vect__ngram_range = (4, 9):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 75 |                                   -2.22122 | char             | (4, 9)              | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
#### vect__ngram_range = (5, 12):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 79 |                                   -2.22691 | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |

**Range: 0.0564**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 73 |                                   -2.23366 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |
#### vect__preprocessor = clean_and_stem_text:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 75 |                                   -2.22122 | char             | (4, 9)              | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |

**Range: 0.0124**

---

### Best parameter combinations for vect__stop_words


#### vect__stop_words = N/A:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 74 |                                   -2.22122 | char             | (4, 9)              | clean_and_stem_text  | N/A                | linear        |       10 |
#### vect__stop_words = Yes (n=232):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 75 |                                   -2.22122 | char             | (4, 9)              | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |

**Range: 0.0000**

---

### Best parameter combinations for svr__kernel


#### svr__kernel = rbf:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 178 |                                   -2.29007 | char_wb          | (2, 6)              | clean_and_stem_text  | N/A                | rbf           |       10 |
#### svr__kernel = linear:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 75 |                                   -2.22122 | char             | (4, 9)              | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |

**Range: 0.0689**

---

### Best parameter combinations for svr__C


#### svr__C = 1.0:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 171 |                                   -2.33204 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |        1 |
#### svr__C = 10.0:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 74 |                                   -2.22122 | char             | (4, 9)              | clean_and_stem_text  | N/A                | linear        |       10 |
#### svr__C = 0.1:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 203 |                                   -3.05867 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |      0.1 |
#### svr__C = 0.001:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 219 |                                   -3.60251 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |    0.001 |

**Range: 1.3813**

---
