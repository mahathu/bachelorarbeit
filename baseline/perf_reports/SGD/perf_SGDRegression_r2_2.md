# Analysis for perf_reports/SGD/perf_SGDRegression_r2_2.csv (n_samples=14638)

## Best parameter combinations:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
|  81 |              0.459549 | char             | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
|  93 |              0.459541 | char_wb          | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
|  79 |              0.459363 | char             | (2, 6)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
| 189 |              0.459323 | char_wb          | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        1e-05 |
|  69 |              0.459261 | char_wb          | (3, 7)              | clean_and_stem_text  | squared_loss | l1             |        1e-06 |

## Performance by parameter:

|vect__analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.4595| 0.0311|
|char_wb         | 0.4595| 0.0422|


|vect__ngram_range |max r2 |mean r2 |
|---|---|---|
|(3, 7)          | 0.4595| 0.0342|
|(2, 6)          | 0.4594| 0.0402|
|(4, 9)          | 0.4526| 0.0235|
|(1, 9)          | 0.4513| 0.0336|
|(1, 5)          | 0.4507| 0.0454|
|(1, 3)          | 0.4229| 0.0431|


|vect__preprocessor |max r2 |mean r2 |
|---|---|---|
|clean_and_stem_text | 0.4595| 0.0382|
|N/A             | 0.4589| 0.0352|


|sgd__loss |max r2 |mean r2 |
|---|---|---|
|squared_loss    | 0.4595| 0.3490|
|huber           | -0.2334| -0.2757|


|sgd__penalty |max r2 |mean r2 |
|---|---|---|
|l2              | 0.4595| 0.0592|
|l1              | 0.4593| 0.0141|


|sgd__alpha |max r2 |mean r2 |
|---|---|---|
|1e-06           | 0.4595| 0.0889|
|1e-05           | 0.4593| 0.0867|
|0.0001          | 0.4573| 0.0751|
|0.001           | 0.4331| 0.0288|
|0.01            | 0.2594| -0.0962|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 81 |              0.459549 | char             | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
#### vect__analyzer = char_wb:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 93 |              0.459541 | char_wb          | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |

**Range: 0.0000**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 3):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 73 |              0.422892 | char             | (1, 3)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (1, 5):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 75 |              0.450656 | char             | (1, 5)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (1, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 77 |              0.451263 | char             | (1, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (2, 6):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 79 |              0.459363 | char             | (2, 6)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (3, 7):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 81 |              0.459549 | char             | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (4, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 95 |               0.45255 | char_wb          | (4, 9)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |

**Range: 0.0367**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 80 |              0.458867 | char             | (3, 7)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__preprocessor = clean_and_stem_text:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 81 |              0.459549 | char             | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |

**Range: 0.0007**

---

### Best parameter combinations for sgd__loss


#### sgd__loss = huber:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss   | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:------------|:---------------|-------------:|
| 133 |             -0.233431 | char_wb          | (1, 3)              | clean_and_stem_text  | huber       | l2             |        1e-05 |
#### sgd__loss = squared_loss:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 81 |              0.459549 | char             | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |

**Range: 0.6930**

---

### Best parameter combinations for sgd__penalty


#### sgd__penalty = l1:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 69 |              0.459261 | char_wb          | (3, 7)              | clean_and_stem_text  | squared_loss | l1             |        1e-06 |
#### sgd__penalty = l2:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 81 |              0.459549 | char             | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |

**Range: 0.0003**

---

### Best parameter combinations for sgd__alpha


#### sgd__alpha = 1e-06:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 81 |              0.459549 | char             | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |
#### sgd__alpha = 1e-05:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 189 |              0.459323 | char_wb          | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        1e-05 |
#### sgd__alpha = 0.0001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 285 |              0.457278 | char_wb          | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |       0.0001 |
#### sgd__alpha = 0.001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 381 |              0.433062 | char_wb          | (3, 7)              | clean_and_stem_text  | squared_loss | l2             |        0.001 |
#### sgd__alpha = 0.01:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 475 |              0.259365 | char_wb          | (2, 6)              | clean_and_stem_text  | squared_loss | l2             |         0.01 |

**Range: 0.2002**

---
