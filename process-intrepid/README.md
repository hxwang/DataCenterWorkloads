## Process ANL-Intrepid 

### Intro
- The scripts in this folder have the objective to calculate the statistics information of prallel jobs. In specific, the job traces is from [ANL-Intrepid](https://github.com/hxwang/GreenDC-Summary/blob/master/traces/file/intrepid.md).

### Files
|file| function|
|:---|:--------|
|[pystats.py](./pystats.py)| tool function to process data by column, tool provided by [Zhonghua Xi](https://github.com/xizhonghua/pystats)|
|[process-intrepid.py](./process-grid5k.py)| process jobs' running time|



### Results
- Processing time (in seconds)

|Records| Mean| Variance| SteDev| Sum|
|:------|:------|:------|:------|:------|
| 68936| 5176.3476| 81807258.969| 9044.737| 356836696.0| 

Min| Max| Median| Confidence| Conf.L| Conf.U|
|:------|:------|:------|:------|:------|:------|
|10.0| 408773.0| 3607.5 |0.95| 5108.828| 5243.868|




### How to run
- Step1: pre-processing workloads, make the sperator in each column as a single space
  - open input data `ANL-Intrepid-2009-1.swf` using note-pad++
  - repace 4-space `    ` with 2 spaces `  `
  - repace all 2-space `  ` with 1 space ` `
- Step2: calculate statistics of processing time. Take `'../data/ANL-Intrepid-2009-1.swf/ANL-Intrepid-2009-1.swf'` as input.

```
python process-intrepid.py
