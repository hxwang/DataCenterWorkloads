## Process ANL-Intrepid 

### 1. Intro
- The scripts in this folder have the objective to calculate the statistics information of batch jobs. 
  - The job traces is from [ANL-Intrepid](../traces/intrepid.md).
  - The analysis will focus on the job processing time and job arrival time.

### 2. Scripts
|file| function|
|:---|:--------|
|[pystats.py](./scripts/pystats.py)| tool function to process data by column, tool provided by [Zhonghua Xi](https://github.com/xizhonghua/pystats)|
|[getColumn.py](./scripts/getColumn.py)| tool function to extract target column from file|
|[process-intrepid.py](./scripts/process-intrepid.py)| process jobs' running time|
|[getHistogram.m](./scripts/getHistogram.m)| plot histogram of processing time|
|[getKMean.m](./scripts/getKMean.m)| plot k-mean of processing time|
|[getHistogramArrivalTime.m](./scripts/getHistogramArrivalTime.m)| get histogram of arrival time|
|[getHistogramInterArrivalTime.m](./scripts/getHistogramInterArrivalTime.m)| get histogram of interarrival time|
|[getCDFProcessTime.m](./scripts/getCDFProcessTime.m)| get CDF of processing time|

--
### 3. Experiment 1: Analyze Processing Time

#### Statistics (in seconds)

- How to run
  - Step1: pre-processing workloads, make the sperator in each column as a single space
    - open input data `ANL-Intrepid-2009-1.swf` using note-pad++
    - repace 4-space `    ` with 2 spaces `  `
    - repace all 2-space `  ` with 1 space ` `
  - Step2: calculate statistics of processing time. Take `'../data/ANL-Intrepid-2009-1.swf/ANL-Intrepid-2009-1.swf'` as input.
  ```
  python process-intrepid.py
  ```
  
- Statistics 

|Job \#| Mean| Variance| SteDev| Sum|
|:------|:------|:------|:------|:------|
| 68936| 5176.3476| 81807258.969| 9044.737| 356836696.0| 

Min| Max| Median| Confidence| Conf.L| Conf.U|
|:------|:------|:------|:------|:------|:------|
|10.0| 408773.0| 3607.5 |0.95| 5108.828| 5243.868|

#### Histogram
- How to run
  - Step 1: extract processing time column
    - Format `python .\getColumn.py [Skip-lines] [Columns] [InputFile] [OutputFile]`
    - Example 
    ```
    python .\getColumn.py 15 4 ..\data\ANL-Intrepid-2009-1.swf\ANL-Intrepid-2009-1.swf ..\data\ANL-Intrepid-2009-1.swf\processTim
  e.txt
    ```
  - Step 2: plot histogram
- Histogram figures
  - Fig 1: histogram of processing time of all jobs
  - Fig 2: histogram of processing time of all jobs, jobs with processing time larger than 24 hours are filtered out.
  - Fig 2.1: cdf of processing time of all jobs
  - Fig 2.2: cdf of processing time with filtering of jobs larger than 24 hours
  
|Fig 1:Histogram Of Processing Time| 
|:--| 
|![](figs/processingTimeHist.png)| 

|Fig 2:Histogram Of Processing Time with filtering of large jobs| 
|:--| 
|![](figs/processingTimeHist_filtered.png)| 

|Fig 2.1: CDF of Processing Time of jobs| 
|:--| 
|![](figs/processingTimeCDF.png)| 

|Fig 2.2: CDF of Processing Time with filtering of large jobs| 
|:--| 
|![](figs/processingTimeCDF-filtered.png)| 



#### K-mean Clustering
- How to run
  `getKMeanProcessTime`
- Figures
  - Fig 3: cluster the processing time using k-mean with k = 6
  
|Fig 3: K-mean clustering of processing time (k=6)| 
|:----|
|![](./figs/processingTimeHist_k-mean.png)|


### 4. Experiment 2: Analyze Arrive Time
#### Histogram of arrival time
- How to run
  - Step 1: get arrival time column (column =2)
    - Format: `python .\getColumn.py [Skip-lines] [Columns] [InputFile] [OutputFile]`
    - Example: 
    ```
    python .\getColumn.py 15 2 ..\data\ANL-Intrepid-2009-1.swf\ANL-Intrepid-2009-1.swf ..\data\ANL-Intrepid-2009-1.swf\arrivalTim
  e.txt
  ```
  - Step 2: get histogram 
  ```
  getHistogramArrivalTime('..\data\ANL-Intrepid-2009-1.swf\arrivalTime.txt')
  ```
  
- Histogram of arrival time

|Fig 4: Histogram of arrival time |
|:----|
|![](figs/arrivalTimeHist.png)|


#### Inter arrival time
- How to run
  - Step 1:get inter arrival time from arrival time using the following command
  
  ```
python .\getInterArrivalTime.py ..\data\ANL-Intrepid-2009-1.swf\arrivalTime.txt ..\data\ANL-Intrepid-2009-1.swf\interArrivalTime.txt
```
  - Step 2: get histogram
  ```
   getHistogramInterArrivalTime('..\data\ANL-Intrepid-2009-1.swf\interArrivalTime.txt', true)
  ```
- Histogram of inter arrival time

|Fig 5: Histogram of inter arrival time|
|:-----|
|![](./figs/interArrivalTimeHist_filtered.png)|


### 5. Experiment 3: Cumulative workload
- Objective: calculative cumulative workload at each time 
- How to run
 - `getCumulativeProcessTime`
 
- Results
  - Fig 6: cumulative workload
  
|Fig 6: Cumulative workload over time|
|:---|
|![](figs/cumulativeProcessingTime.png)|
