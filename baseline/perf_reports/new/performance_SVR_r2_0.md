# Analysis for perf_reports/new/performance_SVR_r2_0.csv (n_samples=3000)

## Best parameter combinations:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
|  41 |              0.539908 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |
|  40 |              0.539908 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
|  44 |              0.536886 | char             | (2, 6)              | N/A                  | N/A                | rbf           |       10 |
|  45 |              0.536886 | char             | (2, 6)              | N/A                  | Yes (n=232)        | rbf           |       10 |
| 176 |              0.536163 | char_wb          | (2, 6)              | N/A                  | N/A                | rbf           |       10 |

## Performance by parameter:

|vect__analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.5399| 0.3136|
|char_wb         | 0.5362| 0.3223|


|vect__ngram_range |max r2 |mean r2 |
|---|---|---|
|(1, 5)          | 0.5399| 0.3337|
|(2, 6)          | 0.5369| 0.3296|
|(4, 7)          | 0.5269| 0.3139|
|(4, 9)          | 0.5254| 0.3098|
|(5, 12)         | 0.5145| 0.2863|


|vect__preprocessor |max r2 |mean r2 |
|---|---|---|
|N/A             | 0.5399| 0.3168|
|clean_and_stem_text | 0.5307| 0.3154|


|vect__stop_words |max r2 |mean r2 |
|---|---|---|
|Yes (n=232)     | 0.5399| 0.3161|
|N/A             | 0.5399| 0.3161|


|svr__kernel |max r2 |mean r2 |
|---|---|---|
|rbf             | 0.5399| 0.3009|
|linear          | 0.5331| 0.3313|


|svr__C |max r2 |mean r2 |
|---|---|---|
|10.0            | 0.5399| 0.4795|
|1.0             | 0.5331| 0.5055|
|0.1             | 0.4290| 0.2936|
|0.001           | -0.0064| -0.0143|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 41 |              0.539908 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |
#### vect__analyzer = char_wb:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 176 |              0.536163 | char_wb          | (2, 6)              | N/A                  | N/A                | rbf           |       10 |

**Range: 0.0037**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 5):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 41 |              0.539908 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |
#### vect__ngram_range = (2, 6):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 44 |              0.536886 | char             | (2, 6)              | N/A                  | N/A                | rbf           |       10 |
#### vect__ngram_range = (4, 7):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 28 |              0.526941 | char             | (4, 7)              | N/A                  | N/A                | linear        |        1 |
#### vect__ngram_range = (4, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 32 |              0.525408 | char             | (4, 9)              | N/A                  | N/A                | linear        |        1 |
#### vect__ngram_range = (5, 12):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 38 |               0.51446 | char             | (5, 12)             | clean_and_stem_text  | N/A                | linear        |        1 |

**Range: 0.0254**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 41 |              0.539908 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |
#### vect__preprocessor = clean_and_stem_text:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 43 |               0.53071 | char             | (1, 5)              | clean_and_stem_text  | Yes (n=232)        | rbf           |       10 |

**Range: 0.0092**

---

### Best parameter combinations for vect__stop_words


#### vect__stop_words = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 40 |              0.539908 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
#### vect__stop_words = Yes (n=232):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 41 |              0.539908 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |

**Range: 0.0000**

---

### Best parameter combinations for svr__kernel


#### svr__kernel = rbf:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 41 |              0.539908 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |
#### svr__kernel = linear:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 24 |              0.533114 | char             | (2, 6)              | N/A                  | N/A                | linear        |        1 |

**Range: 0.0068**

---

### Best parameter combinations for svr__C


#### svr__C = 1.0:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 24 |              0.533114 | char             | (2, 6)              | N/A                  | N/A                | linear        |        1 |
#### svr__C = 10.0:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 40 |              0.539908 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
#### svr__C = 0.1:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 201 |               0.42897 | char_wb          | (2, 6)              | N/A                  | Yes (n=232)        | linear        |      0.1 |
#### svr__C = 0.001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 219 |           -0.00639302 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |    0.001 |

**Range: 0.5463**

---
