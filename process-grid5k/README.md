## Processing Grid5k Workload

### Intro
- The scripts in this folder have the objective to calculate the statistics information of prallel jobs. In specific, the job traces is from [GWA-T-2 Grid5000](../traces/grid5.md).

### Files
|file| function|
|:---|:--------|
|[pystats.py](./pystats.py)| tool function to process data by column, tool provided by [Zhonghua Xi](https://github.com/xizhonghua/pystats)|
|[filterUnExecuteJobs.py](./filterUnExecuteJobs.py)| pre-processing jobs, filter out other jobs that didn't execute|
|[process-grid5k.py](./process-grid5k.py)| process jobs' running time|


### Results
- Processing time (In seconds)

|Records| Mean| Variance| SteDev| Sum|
|:------|:------|:------|:------|:------|
|811062| 3097.653| 728082271.585| 26982.9997| 2512389038.0|


Min| Max| Median| Confidence| Conf.L| Conf.U|
|:------|:------|:------|:------|:------|:------|
| 1.0| 3015459.0| 43239.5|0.95| 3038.93| 3156.4|

### How to run
- Step1: pre-processing workloads, filter out jobs that didn't started. 
  - Input: this scripts will take file `'../data/anon_jobs_gwf/grid5000_clean_trace.log'` as input
  - Output: output the processed jobs to `'../data/anon_jobs_gwf/filtered_grid5000_clean_trace.log'`.

```
python filterUnExecuteJob.py
```

- Step2: calculate statistics of processing time. Take `'../data/anon_jobs_gwf/filtered_grid5000_clean_trace.log'` as input.

```
python process-grid5k.py
