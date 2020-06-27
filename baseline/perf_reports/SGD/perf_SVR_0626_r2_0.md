# Analysis for perf_reports/SGD/perf_SVR_0626_r2_0.csv (n_samples=10000)

## Best parameter combinations:

|    |   r2_performance_mean | svr__kernel   | svr__gamma   |
|---:|----------------------:|:--------------|:-------------|
|  1 |             0.584121  | rbf           | scale        |
|  0 |             0.508981  | linear        | N/A          |
|  2 |            -0.0235161 | rbf           | auto         |

## Performance by parameter:

|svr__kernel |max r2 |mean r2 |
|---|---|---|
|rbf             | 0.5841| 0.2803|
|linear          | 0.5090| 0.5090|


|svr__gamma |max r2 |mean r2 |
|---|---|---|
|scale           | 0.5841| 0.5841|
|N/A             | 0.5090| 0.5090|
|auto            | -0.0235| -0.0235|


## Best parameter combination per parameter value:


### Best parameter combinations for svr__kernel


#### svr__kernel = linear:

|    |   r2_performance_mean | svr__kernel   | svr__gamma   |
|---:|----------------------:|:--------------|:-------------|
|  0 |              0.508981 | linear        | N/A          |
#### svr__kernel = rbf:

|    |   r2_performance_mean | svr__kernel   | svr__gamma   |
|---:|----------------------:|:--------------|:-------------|
|  1 |              0.584121 | rbf           | scale        |

**Range: 0.0751**

---

### Best parameter combinations for svr__gamma


#### svr__gamma = N/A:

|    |   r2_performance_mean | svr__kernel   | svr__gamma   |
|---:|----------------------:|:--------------|:-------------|
|  0 |              0.508981 | linear        | N/A          |
#### svr__gamma = scale:

|    |   r2_performance_mean | svr__kernel   | svr__gamma   |
|---:|----------------------:|:--------------|:-------------|
|  1 |              0.584121 | rbf           | scale        |
#### svr__gamma = auto:

|    |   r2_performance_mean | svr__kernel   | svr__gamma   |
|---:|----------------------:|:--------------|:-------------|
|  2 |            -0.0235161 | rbf           | auto         |

**Range: 0.6076**

---
