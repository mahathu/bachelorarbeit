# Analysis for perf_reports/new/performance_SVR_r2_1.csv (n_samples=3000)

## Best parameter combinations:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 41 |              0.721012 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |
| 40 |              0.721012 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
| 43 |              0.720557 | char             | (1, 5)              | clean_and_stem_text  | Yes (n=232)        | rbf           |       10 |
| 42 |              0.720557 | char             | (1, 5)              | clean_and_stem_text  | N/A                | rbf           |       10 |
| 46 |              0.718536 | char             | (2, 6)              | clean_and_stem_text  | N/A                | rbf           |       10 |

## Performance by parameter:

|vect__analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.7210| 0.4048|
|char_wb         | 0.7145| 0.4275|


|vect__ngram_range |max r2 |mean r2 |
|---|---|---|
|(1, 5)          | 0.7210| 0.4331|
|(2, 6)          | 0.7185| 0.4309|
|(4, 7)          | 0.7111| 0.4055|
|(4, 9)          | 0.7077| 0.4057|
|(5, 12)         | 0.7026| 0.3674|


|vect__preprocessor |max r2 |mean r2 |
|---|---|---|
|N/A             | 0.7210| 0.4102|
|clean_and_stem_text | 0.7206| 0.4124|


|vect__stop_words |max r2 |mean r2 |
|---|---|---|
|Yes (n=232)     | 0.7210| 0.4113|
|N/A             | 0.7210| 0.4113|


|svr__kernel |max r2 |mean r2 |
|---|---|---|
|rbf             | 0.7210| 0.3771|
|linear          | 0.7058| 0.4455|


|svr__C |max r2 |mean r2 |
|---|---|---|
|10.0            | 0.7210| 0.6948|
|1.0             | 0.7058| 0.6557|
|0.1             | 0.5232| 0.3066|
|0.001           | -0.0059| -0.0118|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 40 |              0.721012 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
#### vect__analyzer = char_wb:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 177 |              0.714475 | char_wb          | (2, 6)              | N/A                  | Yes (n=232)        | rbf           |       10 |

**Range: 0.0065**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 5):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 40 |              0.721012 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
#### vect__ngram_range = (2, 6):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 47 |              0.718536 | char             | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | rbf           |       10 |
#### vect__ngram_range = (4, 7):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 51 |              0.711126 | char             | (4, 7)              | clean_and_stem_text  | Yes (n=232)        | rbf           |       10 |
#### vect__ngram_range = (4, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 55 |               0.70772 | char             | (4, 9)              | clean_and_stem_text  | Yes (n=232)        | rbf           |       10 |
#### vect__ngram_range = (5, 12):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 79 |              0.702558 | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |

**Range: 0.0185**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 40 |              0.721012 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
#### vect__preprocessor = clean_and_stem_text:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 43 |              0.720557 | char             | (1, 5)              | clean_and_stem_text  | Yes (n=232)        | rbf           |       10 |

**Range: 0.0005**

---

### Best parameter combinations for vect__stop_words


#### vect__stop_words = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 40 |              0.721012 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
#### vect__stop_words = Yes (n=232):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 41 |              0.721012 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |

**Range: 0.0000**

---

### Best parameter combinations for svr__kernel


#### svr__kernel = rbf:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 41 |              0.721012 | char             | (1, 5)              | N/A                  | Yes (n=232)        | rbf           |       10 |
#### svr__kernel = linear:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 24 |              0.705778 | char             | (2, 6)              | N/A                  | N/A                | linear        |        1 |

**Range: 0.0152**

---

### Best parameter combinations for svr__C


#### svr__C = 1.0:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 25 |              0.705778 | char             | (2, 6)              | N/A                  | Yes (n=232)        | linear        |        1 |
#### svr__C = 10.0:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 40 |              0.721012 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
#### svr__C = 0.1:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 203 |              0.523172 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |      0.1 |
#### svr__C = 0.001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 219 |           -0.00587993 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |    0.001 |

**Range: 0.7269**

---
