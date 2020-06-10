# Analysis for perf_reports/SGD/perf_SGDRegression_r2_3.csv (n_samples=17519)

## Best parameter combinations:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
|  83 |              0.603052 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
| 179 |              0.60258  | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-05 |
|  59 |              0.602091 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l1             |        1e-06 |
|  82 |              0.601971 | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-06 |
| 178 |              0.601517 | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-05 |

## Performance by parameter:

|vect__analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.6031| -1.3200|
|char_wb         | 0.5904| -0.8293|


|vect__ngram_range |max r2 |mean r2 |
|---|---|---|
|(4, 9)          | 0.6031| -2.2080|
|(3, 7)          | 0.6012| -1.8709|
|(2, 6)          | 0.5954| -1.3005|
|(1, 9)          | 0.5890| -0.7261|
|(1, 5)          | 0.5858| -0.3092|
|(1, 3)          | 0.5549| -0.0334|


|vect__preprocessor |max r2 |mean r2 |
|---|---|---|
|clean_and_stem_text | 0.6031| -1.0355|
|N/A             | 0.6020| -1.1139|


|sgd__loss |max r2 |mean r2 |
|---|---|---|
|squared_loss    | 0.6031| 0.4858|
|huber           | -0.0823| -2.6351|


|sgd__penalty |max r2 |mean r2 |
|---|---|---|
|l2              | 0.6031| -1.0152|
|l1              | 0.6021| -1.1341|


|sgd__alpha |max r2 |mean r2 |
|---|---|---|
|1e-06           | 0.6031| -0.6985|
|1e-05           | 0.6026| -0.7168|
|0.0001          | 0.5969| -0.8255|
|0.001           | 0.5578| -1.1849|
|0.01            | 0.3652| -1.9477|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 83 |              0.603052 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
#### vect__analyzer = char_wb:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 94 |              0.590411 | char_wb          | (4, 9)              | N/A                  | squared_loss | l2             |        1e-06 |

**Range: 0.0126**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 3):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 72 |              0.554875 | char             | (1, 3)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (1, 5):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 74 |              0.585819 | char             | (1, 5)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (1, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 77 |              0.588961 | char             | (1, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (2, 6):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 78 |              0.595428 | char             | (2, 6)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (3, 7):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 80 |              0.601205 | char             | (3, 7)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (4, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 83 |              0.603052 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |

**Range: 0.0482**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 82 |              0.601971 | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__preprocessor = clean_and_stem_text:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 83 |              0.603052 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |

**Range: 0.0011**

---

### Best parameter combinations for sgd__loss


#### sgd__loss = huber:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss   | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:------------|:---------------|-------------:|
| 133 |            -0.0823184 | char_wb          | (1, 3)              | clean_and_stem_text  | huber       | l2             |        1e-05 |
#### sgd__loss = squared_loss:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 83 |              0.603052 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |

**Range: 0.6854**

---

### Best parameter combinations for sgd__penalty


#### sgd__penalty = l1:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 59 |              0.602091 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l1             |        1e-06 |
#### sgd__penalty = l2:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 83 |              0.603052 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |

**Range: 0.0010**

---

### Best parameter combinations for sgd__alpha


#### sgd__alpha = 1e-06:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 83 |              0.603052 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
#### sgd__alpha = 1e-05:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 179 |               0.60258 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-05 |
#### sgd__alpha = 0.0001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 275 |              0.596916 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |       0.0001 |
#### sgd__alpha = 0.001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 381 |              0.557799 | char_wb          | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        0.001 |
#### sgd__alpha = 0.01:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 475 |              0.365208 | char_wb          | (2, 6)              | clean_and_stem_text  | squared_loss | l2             |         0.01 |

**Range: 0.2378**

---
