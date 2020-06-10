# Analysis for perf_reports/new/performance_SVR_r2_2.csv (n_samples=3000)

## Best parameter combinations:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
|  73 |              0.493418 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |
|  72 |              0.493418 | char             | (4, 9)              | N/A                  | N/A                | linear        |       10 |
|  77 |              0.49301  | char             | (5, 12)             | N/A                  | Yes (n=232)        | linear        |       10 |
|  76 |              0.49301  | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |
| 176 |              0.487903 | char_wb          | (2, 6)              | N/A                  | N/A                | rbf           |       10 |

## Performance by parameter:

|vect__analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.4934| 0.1791|
|char_wb         | 0.4879| 0.2012|


|vect__ngram_range |max r2 |mean r2 |
|---|---|---|
|(4, 9)          | 0.4934| 0.1840|
|(5, 12)         | 0.4930| 0.1464|
|(2, 6)          | 0.4879| 0.2010|
|(4, 7)          | 0.4829| 0.1820|
|(1, 5)          | 0.4807| 0.1996|


|vect__preprocessor |max r2 |mean r2 |
|---|---|---|
|N/A             | 0.4934| 0.1846|
|clean_and_stem_text | 0.4846| 0.1862|


|vect__stop_words |max r2 |mean r2 |
|---|---|---|
|Yes (n=232)     | 0.4934| 0.1854|
|N/A             | 0.4934| 0.1854|


|svr__kernel |max r2 |mean r2 |
|---|---|---|
|linear          | 0.4934| 0.2147|
|rbf             | 0.4879| 0.1561|


|svr__C |max r2 |mean r2 |
|---|---|---|
|10.0            | 0.4934| 0.4529|
|1.0             | 0.4674| 0.4055|
|0.1             | 0.2352| 0.0690|
|0.001           | -0.1799| -0.1858|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 72 |              0.493418 | char             | (4, 9)              | N/A                  | N/A                | linear        |       10 |
#### vect__analyzer = char_wb:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 177 |              0.487903 | char_wb          | (2, 6)              | N/A                  | Yes (n=232)        | rbf           |       10 |

**Range: 0.0055**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 5):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 40 |              0.480722 | char             | (1, 5)              | N/A                  | N/A                | rbf           |       10 |
#### vect__ngram_range = (2, 6):

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 176 |              0.487903 | char_wb          | (2, 6)              | N/A                  | N/A                | rbf           |       10 |
#### vect__ngram_range = (4, 7):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 68 |              0.482875 | char             | (4, 7)              | N/A                  | N/A                | linear        |       10 |
#### vect__ngram_range = (4, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 72 |              0.493418 | char             | (4, 9)              | N/A                  | N/A                | linear        |       10 |
#### vect__ngram_range = (5, 12):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 76 |               0.49301 | char             | (5, 12)             | N/A                  | N/A                | linear        |       10 |

**Range: 0.0127**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 73 |              0.493418 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |
#### vect__preprocessor = clean_and_stem_text:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 178 |              0.484551 | char_wb          | (2, 6)              | clean_and_stem_text  | N/A                | rbf           |       10 |

**Range: 0.0089**

---

### Best parameter combinations for vect__stop_words


#### vect__stop_words = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 72 |              0.493418 | char             | (4, 9)              | N/A                  | N/A                | linear        |       10 |
#### vect__stop_words = Yes (n=232):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 73 |              0.493418 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |

**Range: 0.0000**

---

### Best parameter combinations for svr__kernel


#### svr__kernel = rbf:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 176 |              0.487903 | char_wb          | (2, 6)              | N/A                  | N/A                | rbf           |       10 |
#### svr__kernel = linear:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 73 |              0.493418 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |

**Range: 0.0055**

---

### Best parameter combinations for svr__C


#### svr__C = 1.0:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 27 |              0.467426 | char             | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |        1 |
#### svr__C = 10.0:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 73 |              0.493418 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |
#### svr__C = 0.1:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 203 |              0.235244 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |      0.1 |
#### svr__C = 0.001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 219 |              -0.17989 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |    0.001 |

**Range: 0.6733**

---
