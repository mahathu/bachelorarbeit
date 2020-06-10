# Analysis for perf_reports/new/performance_SVR_r2_3.csv (n_samples=3000)

## Best parameter combinations:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 79 |              0.565071 | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
| 78 |              0.565071 | char             | (5, 12)             | clean_and_stem_text  | N/A                | linear        |       10 |
| 75 |              0.563686 | char             | (4, 9)              | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
| 74 |              0.563686 | char             | (4, 9)              | clean_and_stem_text  | N/A                | linear        |       10 |
| 73 |              0.561985 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |

## Performance by parameter:

|vect__analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.5651| 0.2340|
|char_wb         | 0.5538| 0.2606|


|vect__ngram_range |max r2 |mean r2 |
|---|---|---|
|(5, 12)         | 0.5651| 0.2032|
|(4, 9)          | 0.5637| 0.2393|
|(4, 7)          | 0.5549| 0.2345|
|(2, 6)          | 0.5538| 0.2590|
|(1, 5)          | 0.5517| 0.2570|


|vect__preprocessor |max r2 |mean r2 |
|---|---|---|
|clean_and_stem_text | 0.5651| 0.2456|
|N/A             | 0.5620| 0.2376|


|vect__stop_words |max r2 |mean r2 |
|---|---|---|
|Yes (n=232)     | 0.5651| 0.2416|
|N/A             | 0.5651| 0.2416|


|svr__kernel |max r2 |mean r2 |
|---|---|---|
|linear          | 0.5651| 0.2776|
|rbf             | 0.5538| 0.2056|


|svr__C |max r2 |mean r2 |
|---|---|---|
|10.0            | 0.5651| 0.5321|
|1.0             | 0.5374| 0.4250|
|0.1             | 0.2340| 0.0811|
|0.001           | -0.0690| -0.0718|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 79 |              0.565071 | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
#### vect__analyzer = char_wb:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 179 |              0.553806 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | rbf           |       10 |

**Range: 0.0113**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 5):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 43 |              0.551746 | char             | (1, 5)              | clean_and_stem_text  | Yes (n=232)        | rbf           |       10 |
#### vect__ngram_range = (2, 6):

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 178 |              0.553806 | char_wb          | (2, 6)              | clean_and_stem_text  | N/A                | rbf           |       10 |
#### vect__ngram_range = (4, 7):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 68 |              0.554927 | char             | (4, 7)              | N/A                  | N/A                | linear        |       10 |
#### vect__ngram_range = (4, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 75 |              0.563686 | char             | (4, 9)              | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
#### vect__ngram_range = (5, 12):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 79 |              0.565071 | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |

**Range: 0.0133**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 73 |              0.561985 | char             | (4, 9)              | N/A                  | Yes (n=232)        | linear        |       10 |
#### vect__preprocessor = clean_and_stem_text:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 79 |              0.565071 | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |

**Range: 0.0031**

---

### Best parameter combinations for vect__stop_words


#### vect__stop_words = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 78 |              0.565071 | char             | (5, 12)             | clean_and_stem_text  | N/A                | linear        |       10 |
#### vect__stop_words = Yes (n=232):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 79 |              0.565071 | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |

**Range: 0.0000**

---

### Best parameter combinations for svr__kernel


#### svr__kernel = rbf:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 178 |              0.553806 | char_wb          | (2, 6)              | clean_and_stem_text  | N/A                | rbf           |       10 |
#### svr__kernel = linear:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 79 |              0.565071 | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |

**Range: 0.0113**

---

### Best parameter combinations for svr__C


#### svr__C = 1.0:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 171 |              0.537449 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |        1 |
#### svr__C = 10.0:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 79 |              0.565071 | char             | (5, 12)             | clean_and_stem_text  | Yes (n=232)        | linear        |       10 |
#### svr__C = 0.1:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 203 |              0.234041 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |      0.1 |
#### svr__C = 0.001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | vect__stop_words   | svr__kernel   |   svr__C |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------------|:--------------|---------:|
| 219 |            -0.0690039 | char_wb          | (2, 6)              | clean_and_stem_text  | Yes (n=232)        | linear        |    0.001 |

**Range: 0.6341**

---
