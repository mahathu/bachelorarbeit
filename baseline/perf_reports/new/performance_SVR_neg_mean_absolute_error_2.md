# Analysis for perf_reports/new/performance_SVR_neg_mean_absolute_error_2.csv (n_samples=3000)

## Best parameter combinations:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 77 |                                   -1.15866 | char             | (5, 12)             | N/A                  | Yes (n=232)        | linear        |       10 |
| 76 |                                   -1.15866 | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |
| 73 |                                   -1.16114 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |
| 72 |                                   -1.16114 | char             | (4, 9)              | N/A                  | N/A                | linear        |       10 |
| 78 |                                   -1.16969 | char             | (5, 12)             | clean_and_stem_text  | N/A                | linear        |       10 |

## Performance by parameter:

|vect__analyzer |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|char            | -1.1587| -1.4114|
|char_wb         | -1.1879| -1.4041|


|vect__ngram_range |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|(5, 12)         | -1.1587| -1.4343|
|(4, 9)          | -1.1611| -1.4114|
|(2, 6)          | -1.1753| -1.4000|
|(4, 7)          | -1.1761| -1.4086|
|(1, 5)          | -1.1881| -1.3996|


|vect__preprocessor |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|N/A             | -1.1587| -1.4090|
|clean_and_stem_text | -1.1697| -1.4097|


|vect__stop_words |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|Yes (n=232)     | -1.1587| -1.4093|
|N/A             | -1.1587| -1.4093|


|svr__kernel |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|linear          | -1.1587| -1.3847|
|rbf             | -1.1879| -1.4340|


|svr__C |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|10.0            | -1.1587| -1.2200|
|1.0             | -1.1753| -1.2456|
|0.1             | -1.3965| -1.5209|
|0.001           | -1.6486| -1.6508|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 77 |                                   -1.15866 | char             | (5, 12)             | N/A                  | Yes (n=232)        | linear        |       10 |
#### vect__analyzer = char_wb:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 177 |                                   -1.18785 | char_wb          | (2, 6)              | N/A                  | Yes (n=232)        | rbf           |       10 |

**Range: 0.0292**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 5):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 20 |                                    -1.1881 | char             | (1, 5)              | N/A                  | N/A                | linear        |        1 |
#### vect__ngram_range = (2, 6):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 24 |                                   -1.17528 | char             | (2, 6)              | N/A                  | N/A                | linear        |        1 |
#### vect__ngram_range = (4, 7):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 28 |                                   -1.17609 | char             | (4, 7)              | N/A                  | N/A                | linear        |        1 |
#### vect__ngram_range = (4, 9):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 72 |                                   -1.16114 | char             | (4, 9)              | N/A                  | N/A                | linear        |       10 |
#### vect__ngram_range = (5, 12):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 76 |                                   -1.15866 | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |

**Range: 0.0294**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 76 |                                   -1.15866 | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |
#### vect__preprocessor = clean_and_stem_text:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 78 |                                   -1.16969 | char             | (5, 12)             | clean_and_stem_text  | N/A                | linear        |       10 |

**Range: 0.0110**

---

### Best parameter combinations for vect__stop_words


#### vect__stop_words = N/A:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 76 |                                   -1.15866 | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |
#### vect__stop_words = Yes (n=232):

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 77 |                                   -1.15866 | char             | (5, 12)             | N/A                  | Yes (n=232)        | linear        |       10 |

**Range: 0.0000**

---

### Best parameter combinations for svr__kernel


#### svr__kernel = rbf:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 176 |                                   -1.18785 | char_wb          | (2, 6)              | N/A                  | N/A                | rbf           |       10 |
#### svr__kernel = linear:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 76 |                                   -1.15866 | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |

**Range: 0.0292**

---

### Best parameter combinations for svr__C


#### svr__C = 1.0:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 24 |                                   -1.17528 | char             | (2, 6)              | N/A                  | N/A                | linear        |        1 |
#### svr__C = 10.0:

|    |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 77 |                                   -1.15866 | char             | (5, 12)             | N/A                  | Yes (n=232)        | linear        |       10 |
#### svr__C = 0.1:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 203 |                                   -1.39649 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |      0.1 |
#### svr__C = 0.001:

|     |   neg_mean_absolute_error_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|-------------------------------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 219 |                                    -1.6486 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |    0.001 |

**Range: 0.4899**

---
