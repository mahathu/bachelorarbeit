# Analysis for perf_reports/SGD/perf_SGDRegression_r2_0.csv (n_samples=13885)

## Best parameter combinations:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
|  78 |              0.53069  | char             | (2, 6)              | N/A                  | squared_loss | l2             |        1e-06 |
| 174 |              0.530473 | char             | (2, 6)              | N/A                  | squared_loss | l2             |        1e-05 |
|  54 |              0.530318 | char             | (2, 6)              | N/A                  | squared_loss | l1             |        1e-06 |
|  74 |              0.529651 | char             | (1, 5)              | N/A                  | squared_loss | l2             |        1e-06 |
| 170 |              0.529488 | char             | (1, 5)              | N/A                  | squared_loss | l2             |        1e-05 |

## Performance by parameter:

|vect__analyzer |max r2 |mean r2 |
|---|---|---|
|char            | 0.5307| 0.0649|
|char_wb         | 0.5267| 0.0764|


|vect__ngram_range |max r2 |mean r2 |
|---|---|---|
|(2, 6)          | 0.5307| 0.0689|
|(1, 5)          | 0.5297| 0.0831|
|(3, 7)          | 0.5270| 0.0599|
|(1, 3)          | 0.5262| 0.0986|
|(1, 9)          | 0.5254| 0.0647|
|(4, 9)          | 0.5190| 0.0489|


|vect__preprocessor |max r2 |mean r2 |
|---|---|---|
|N/A             | 0.5307| 0.0697|
|clean_and_stem_text | 0.5289| 0.0716|


|sgd__loss |max r2 |mean r2 |
|---|---|---|
|squared_loss    | 0.5307| 0.4460|
|huber           | -0.2337| -0.3046|


|sgd__penalty |max r2 |mean r2 |
|---|---|---|
|l2              | 0.5307| 0.0944|
|l1              | 0.5303| 0.0470|


|sgd__alpha |max r2 |mean r2 |
|---|---|---|
|1e-06           | 0.5307| 0.1132|
|1e-05           | 0.5305| 0.1116|
|0.0001          | 0.5286| 0.1022|
|0.001           | 0.5100| 0.0716|
|0.01            | 0.3951| -0.0452|


## Best parameter combination per parameter value:


### Best parameter combinations for vect__analyzer


#### vect__analyzer = char:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 78 |               0.53069 | char             | (2, 6)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__analyzer = char_wb:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 90 |               0.52673 | char_wb          | (2, 6)              | N/A                  | squared_loss | l2             |        1e-06 |

**Range: 0.0040**

---

### Best parameter combinations for vect__ngram_range


#### vect__ngram_range = (1, 3):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 72 |              0.526227 | char             | (1, 3)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (1, 5):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 74 |              0.529651 | char             | (1, 5)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (1, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 76 |              0.525356 | char             | (1, 9)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (2, 6):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 78 |               0.53069 | char             | (2, 6)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (3, 7):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 80 |              0.526974 | char             | (3, 7)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__ngram_range = (4, 9):

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 82 |              0.518996 | char             | (4, 9)              | N/A                  | squared_loss | l2             |        1e-06 |

**Range: 0.0117**

---

### Best parameter combinations for vect__preprocessor


#### vect__preprocessor = N/A:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 78 |               0.53069 | char             | (2, 6)              | N/A                  | squared_loss | l2             |        1e-06 |
#### vect__preprocessor = clean_and_stem_text:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 79 |              0.528884 | char             | (2, 6)              | clean_and_stem_text  | squared_loss | l2             |        1e-06 |

**Range: 0.0018**

---

### Best parameter combinations for sgd__loss


#### sgd__loss = huber:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss   | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:------------|:---------------|-------------:|
| 37 |             -0.233663 | char_wb          | (1, 3)              | clean_and_stem_text  | huber       | l2             |        1e-06 |
#### sgd__loss = squared_loss:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 78 |               0.53069 | char             | (2, 6)              | N/A                  | squared_loss | l2             |        1e-06 |

**Range: 0.7644**

---

### Best parameter combinations for sgd__penalty


#### sgd__penalty = l1:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 54 |              0.530318 | char             | (2, 6)              | N/A                  | squared_loss | l1             |        1e-06 |
#### sgd__penalty = l2:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 78 |               0.53069 | char             | (2, 6)              | N/A                  | squared_loss | l2             |        1e-06 |

**Range: 0.0004**

---

### Best parameter combinations for sgd__alpha


#### sgd__alpha = 1e-06:

|    |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|---:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 78 |               0.53069 | char             | (2, 6)              | N/A                  | squared_loss | l2             |        1e-06 |
#### sgd__alpha = 1e-05:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 174 |              0.530473 | char             | (2, 6)              | N/A                  | squared_loss | l2             |        1e-05 |
#### sgd__alpha = 0.0001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 270 |              0.528639 | char             | (2, 6)              | N/A                  | squared_loss | l2             |       0.0001 |
#### sgd__alpha = 0.001:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 360 |              0.510027 | char             | (1, 3)              | N/A                  | squared_loss | l2             |        0.001 |
#### sgd__alpha = 0.01:

|     |   r2_performance_mean | vect__analyzer   | vect__ngram_range   | vect__preprocessor   | sgd__loss    | sgd__penalty   |   sgd__alpha |
|----:|----------------------:|:-----------------|:--------------------|:---------------------|:-------------|:---------------|-------------:|
| 475 |               0.39507 | char_wb          | (2, 6)              | clean_and_stem_text  | squared_loss | l2             |         0.01 |

**Range: 0.1356**

---
