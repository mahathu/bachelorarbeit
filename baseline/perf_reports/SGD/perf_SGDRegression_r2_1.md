# Analysis for perf_reports/SGD/perf_SGDRegression_r2_1.csv (n_samples=15835)

## Best parameter combinations:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
|  82 |              0.71764  | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-06 |
| 178 |              0.71744  | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-05 |
|  58 |              0.717022 | char             | (4, 9)              | N/A                  | squared_loss | l1             |        1e-06 |
|  83 |              0.716954 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
| 179 |              0.716738 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-05 |

## Performance by parameter:

|vect__analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.7176| -1.1446|
|char_wb         | 0.6973| -0.5811|


|vect__ngram_range |max r2 |mean r2 |
|---|---|---|
|(4, 9)          | 0.7176| -1.7629|
|(3, 7)          | 0.7148| -1.4629|
|(2, 6)          | 0.7084| -1.0216|
|(1, 5)          | 0.7006| -0.2752|
|(1, 9)          | 0.6963| -0.6732|
|(1, 3)          | 0.6891| 0.0185|


|vect__preprocessor |max r2 |mean r2 |
|---|---|---|
|N/A             | 0.7176| -0.8816|
|clean_and_stem_text | 0.7170| -0.8442|


|sgd__loss |max r2 |mean r2 |
|---|---|---|
|squared_loss    | 0.7176| 0.6319|
|huber           | -0.0473| -2.3576|


|sgd__penalty |max r2 |mean r2 |
|---|---|---|
|l2              | 0.7176| -0.7789|
|l1              | 0.7170| -0.9468|


|sgd__alpha |max r2 |mean r2 |
|---|---|---|
|1e-06           | 0.7176| -0.4171|
|1e-05           | 0.7174| -0.4331|
|0.0001          | 0.7148| -0.5402|
|0.001           | 0.6861| -1.0785|
|0.01            | 0.5545| -1.8454|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 82 |               0.71764 | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__analyzer = char_wb:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 92 |              0.697345 | char_wb          | (3, 7)              | N/A                  | squared_loss | l2             |        1e-06 |

**Range: 0.0203**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 3):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 48 |              0.689072 | char             | (1, 3)              | N/A                  | squared_loss | l1             |        1e-06 |
#### vect__ngram_range = (1, 5):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 74 |              0.700553 | char             | (1, 5)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (1, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 76 |              0.696274 | char             | (1, 9)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (2, 6):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 78 |              0.708406 | char             | (2, 6)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (3, 7):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 80 |              0.714795 | char             | (3, 7)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (4, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 82 |               0.71764 | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-06 |

**Range: 0.0286**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 82 |               0.71764 | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__preprocessor = clean_and_stem_text:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 83 |              0.716954 | char             | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |

**Range: 0.0007**

---

### Best parameter combinations for sgd__loss


#### sgd__loss = huber:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss   | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:------------|:---------------|-------------:|
| 36 |            -0.0472851 | char_wb          | (1, 3)              | N/A                  | huber       | l2             |        1e-06 |
#### sgd__loss = squared_loss:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 82 |               0.71764 | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-06 |

**Range: 0.7649**

---

### Best parameter combinations for sgd__penalty


#### sgd__penalty = l1:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 58 |              0.717022 | char             | (4, 9)              | N/A                  | squared_loss | l1             |        1e-06 |
#### sgd__penalty = l2:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 82 |               0.71764 | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-06 |

**Range: 0.0006**

---

### Best parameter combinations for sgd__alpha


#### sgd__alpha = 1e-06:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 82 |               0.71764 | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-06 |
#### sgd__alpha = 1e-05:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 178 |               0.71744 | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-05 |
#### sgd__alpha = 0.0001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 274 |              0.714805 | char             | (4, 9)              | N/A                  | squared_loss | l2             |       0.0001 |
#### sgd__alpha = 0.001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 368 |              0.686123 | char             | (3, 7)              | N/A                  | squared_loss | l2             |        0.001 |
#### sgd__alpha = 0.01:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 475 |              0.554464 | char_wb          | (2, 6)              | clean_and_stem_text  | squared_loss | l2             |         0.01 |

**Range: 0.1632**

---
