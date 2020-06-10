# Analysis for perf_reports/new/performance_SVR_min_df_r2_0.csv (n_samples=7667)

## Best parameter combinations:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  0 |              0.531469 |       10 | rbf           | char             | (1, 5)              |            0.1 |
|  1 |              0.513263 |       10 | rbf           | char             | (1, 5)              |            0.2 |
|  2 |              0.479244 |       10 | rbf           | char             | (1, 5)              |            0.3 |
|  3 |              0.422703 |       10 | rbf           | char             | (1, 5)              |            0.4 |
|  4 |              0.395864 |       10 | rbf           | char             | (1, 5)              |            0.5 |

## Performance by parameter:

|svr__C |max r2 |mean r2 |
|---|---|---|
|10              | 0.5315| 0.3896|


|svr__kernel |max r2 |mean r2 |
|---|---|---|
|rbf             | 0.5315| 0.3896|


|vect__analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.5315| 0.3896|


|vect__ngram_range |max r2 |mean r2 |
|---|---|---|
|(1, 5)          | 0.5315| 0.3896|


|vect__min_df |max r2 |mean r2 |
|---|---|---|
|0.1             | 0.5315| 0.5315|
|0.2             | 0.5133| 0.5133|
|0.30000000000000004 | 0.4792| 0.4792|
|0.4             | 0.4227| 0.4227|
|0.5             | 0.3959| 0.3959|
|0.6             | 0.3664| 0.3664|
|0.7000000000000001 | 0.3470| 0.3470|
|0.8             | 0.2888| 0.2888|
|0.9             | 0.1621| 0.1621|
|1.0             |   nan|   nan|


## Best parameter combination per parameter value:


### Best parameter combinations for svr__C


#### svr__C = 10:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  0 |              0.531469 |       10 | rbf           | char             | (1, 5)              |            0.1 |

**Range: 0.0000**

---

### Best parameter combinations for svr__kernel


#### svr__kernel = rbf:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  0 |              0.531469 |       10 | rbf           | char             | (1, 5)              |            0.1 |

**Range: 0.0000**

---

### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  0 |              0.531469 |       10 | rbf           | char             | (1, 5)              |            0.1 |

**Range: 0.0000**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 5):

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  0 |              0.531469 |       10 | rbf           | char             | (1, 5)              |            0.1 |

**Range: 0.0000**

---

### Best parameter combinations for vect__min_df


#### vect__min_df = 0.1:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  0 |              0.531469 |       10 | rbf           | char             | (1, 5)              |            0.1 |
#### vect__min_df = 0.2:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  1 |              0.513263 |       10 | rbf           | char             | (1, 5)              |            0.2 |
#### vect__min_df = 0.30000000000000004:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  2 |              0.479244 |       10 | rbf           | char             | (1, 5)              |            0.3 |
#### vect__min_df = 0.4:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  3 |              0.422703 |       10 | rbf           | char             | (1, 5)              |            0.4 |
#### vect__min_df = 0.5:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  4 |              0.395864 |       10 | rbf           | char             | (1, 5)              |            0.5 |
#### vect__min_df = 0.6:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  5 |              0.366378 |       10 | rbf           | char             | (1, 5)              |            0.6 |
#### vect__min_df = 0.7000000000000001:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  6 |              0.347008 |       10 | rbf           | char             | (1, 5)              |            0.7 |
#### vect__min_df = 0.8:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  7 |              0.288796 |       10 | rbf           | char             | (1, 5)              |            0.8 |
#### vect__min_df = 0.9:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  8 |              0.162083 |       10 | rbf           | char             | (1, 5)              |            0.9 |
#### vect__min_df = 1.0:

|    |   r2_performance_mean |   svr__C | svr__kernel   | vect__analyzer   | vect__ngram_range   |   vect__min_df |
|---:|----------------------:|---------:|:--------------|:-----------------|:--------------------|---------------:|
|  9 |                   nan |       10 | rbf           | char             | (1, 5)              |              1 |

**Range: 0.3694**

---
