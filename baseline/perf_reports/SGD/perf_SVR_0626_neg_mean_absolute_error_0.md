# Analysis for perf_reports/SGD/perf_SVR_0626_neg_mean_absolute_error_0.csv (n_samples=10000)

## Best parameter combinations:

|    |   neg_mean_absolute_error_performance_mean | svr__kernel   | svr__gamma   |
|---:|-------------------------------------------:|:--------------|:-------------|
|  1 |                                   -1.01024 | rbf           | scale        |
|  0 |                                   -1.113   | linear        | N/A          |
|  2 |                                   -1.75926 | rbf           | auto         |

## Performance by parameter:

|svr__kernel |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|rbf             | -1.0102| -1.3848|
|linear          | -1.1130| -1.1130|


|svr__gamma |max neg_mean_absolute_error |mean neg_mean_absolute_error |
|---|---|---|
|scale           | -1.0102| -1.0102|
|N/A             | -1.1130| -1.1130|
|auto            | -1.7593| -1.7593|


## Best parameter combination per parameter value:


### Best parameter combinations for svr__kernel


#### svr__kernel = linear:

|    |   neg_mean_absolute_error_performance_mean | svr__kernel   | svr__gamma   |
|---:|-------------------------------------------:|:--------------|:-------------|
|  0 |                                     -1.113 | linear        | N/A          |
#### svr__kernel = rbf:

|    |   neg_mean_absolute_error_performance_mean | svr__kernel   | svr__gamma   |
|---:|-------------------------------------------:|:--------------|:-------------|
|  1 |                                   -1.01024 | rbf           | scale        |

**Range: 0.1028**

---

### Best parameter combinations for svr__gamma


#### svr__gamma = N/A:

|    |   neg_mean_absolute_error_performance_mean | svr__kernel   | svr__gamma   |
|---:|-------------------------------------------:|:--------------|:-------------|
|  0 |                                     -1.113 | linear        | N/A          |
#### svr__gamma = scale:

|    |   neg_mean_absolute_error_performance_mean | svr__kernel   | svr__gamma   |
|---:|-------------------------------------------:|:--------------|:-------------|
|  1 |                                   -1.01024 | rbf           | scale        |
#### svr__gamma = auto:

|    |   neg_mean_absolute_error_performance_mean | svr__kernel   | svr__gamma   |
|---:|-------------------------------------------:|:--------------|:-------------|
|  2 |                                   -1.75926 | rbf           | auto         |

**Range: 0.7490**

---
