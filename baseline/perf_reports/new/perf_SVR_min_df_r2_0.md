# Analysis for perf_reports/new/perf_SVR_min_df_r2_0.csv (n_samples=3000)

## Best parameter combinations:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:--------------|---------:|
|  0 |              0.53623  | char             | (1, 5)              | linear        |        1 |
|  7 |              0.53478  | char             | (1, 5)              | rbf           |       10 |
|  6 |              0.52329  | char             | (1, 5)              | sigmoid       |        1 |
|  4 |              0.522901 | char             | (1, 5)              | rbf           |        1 |
|  1 |              0.446306 | char             | (1, 5)              | linear        |       10 |

## Performance by parameter:

|vect__analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.5362| 0.2499|


|vect__ngram_range |max r2 |mean r2 |
|---|---|---|
|(1, 5)          | 0.5362| 0.2499|


|svr__kernel |max r2 |mean r2 |
|---|---|---|
|linear          | 0.5362| 0.3480|
|rbf             | 0.5348| 0.3244|
|sigmoid         | 0.5233| 0.1140|
|poly            | 0.4337| 0.2134|


|svr__C |max r2 |mean r2 |
|---|---|---|
|1.0             | 0.5362| 0.4901|
|10.0            | 0.5348| 0.2352|
|0.1             | 0.4327| 0.3026|
|0.001           | -0.0234| -0.0282|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:--------------|---------:|
|  0 |               0.53623 | char             | (1, 5)              | linear        |        1 |

**Range: 0.0000**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 5):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:--------------|---------:|
|  0 |               0.53623 | char             | (1, 5)              | linear        |        1 |

**Range: 0.0000**

---

### Best parameter combinations for svr__kernel


#### svr__kernel = linear:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:--------------|---------:|
|  0 |               0.53623 | char             | (1, 5)              | linear        |        1 |
#### svr__kernel = rbf:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:--------------|---------:|
|  7 |               0.53478 | char             | (1, 5)              | rbf           |       10 |
#### svr__kernel = poly:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:--------------|---------:|
|  8 |              0.433708 | char             | (1, 5)              | poly          |       10 |
#### svr__kernel = sigmoid:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:--------------|---------:|
|  6 |               0.52329 | char             | (1, 5)              | sigmoid       |        1 |

**Range: 0.1025**

---

### Best parameter combinations for svr__C


#### svr__C = 1.0:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:--------------|---------:|
|  0 |               0.53623 | char             | (1, 5)              | linear        |        1 |
#### svr__C = 10.0:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:--------------|---------:|
|  7 |               0.53478 | char             | (1, 5)              | rbf           |       10 |
#### svr__C = 0.1:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:--------------|---------:|
|  2 |              0.432718 | char             | (1, 5)              | linear        |      0.1 |
#### svr__C = 0.001:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | svr__kernel   |   svr__C |
|---:|----------------------:|:-----------------|:--------------------|:--------------|---------:|
|  3 |            -0.0233709 | char             | (1, 5)              | linear        |    0.001 |

**Range: 0.5596**

---
