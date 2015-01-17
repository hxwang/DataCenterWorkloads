[GWA-T-2 Grid5000](http://gwa.ewi.tudelft.nl/datasets/gwa-t-2-grid5000)
---


### Introduction
- Grid5k is a real workload trace which was collected from Grid'5000 system, a 2218 node experimental grid platform consisting of 9 sites geographically distributed in France, from May 2004 to November 2006. 
- Grid'5000 platform: it is an experimental grid platform consisting of 9 sites geographically distributed in France. Each site comprises one or several clusters, for a total of 15 clusters insider grid'5000.
- Type: batch schedulers

### Download
- [Download Page](http://gwa.ewi.tudelft.nl/datasets/gwa-t-2-grid5000)
  - GWF format: [Download the GWA-T-2 trace in GWF format [9MB]](http://gwa.ewi.tudelft.nl/fileadmin/pds/trace-archives/grid-workloads-archive/datasets/gwa-t-2/anon_jobs_gwf.zip)
  - SQLite format: [Download the GWA-T-2 trace in SQLite format [11MB]](http://gwa.ewi.tudelft.nl/fileadmin/pds/trace-archives/grid-workloads-archive/datasets/gwa-t-2/anon_jobs_sqlite.zip)
  
### Files Format
- The file we used is `grid5000_clean_trace.log`, it contains the trace of Grid'5000 (all OAR databases information about jobs) from the beginning of the project up to the 10th of November 2006.
- Note: some jobs may have wait time of < 0 due to the scheduler behavior (OAR) especially reservations, 
	      e.g., a reservation for the period 8am-2pm can be submitted at 8:01am the same day, for a wait time of -1 min.
	      (see also grid5000_reservation_jobs|Jobs_Reservation)
- the trace also includes jobs that have NOT run on Grid'5000, e.g., but canceled before resources are actually allocated to them.  Is up to you to filter these jobs (fields WaitTime=-1 and RunTime=-1)
- This file contains each job in a row, with each column has the following definition: 		   ```
```
JobId
SubmitTime
WaitTime
RunTime
NProc
AverageCPUTimeUsed
UsedMemory
ReqNProcs
ReqTime
ReqMemory
Status
UserId
GroupId
ExecutableId
QueueId
PartitionId
OrigSiteId
LastRunSiteId
JobStructure
JobStructureParams
UsedNetwork
UsedLocalDiskSpace
UsedResources
ReqPlatform
ReqNetwork
RequestedLocalDiskSpace
RequestedResources
VirtualOrganizationId<TAB>ProjectId
```


	    


### Proprocess
- [Trace Analysis](https://github.com/hxwang/DataCenterWorkloads/tree/master/process-grid5k)



### Copyright note
The Grid'5000 traces were kindly provided by the [Grid'5000 team](http://www.grid5000.org/) (special thanks to Dr. Franck Cappello and to Dr. Olivier Richard), the owners of the Grid'5000 system, and by the OAR team (special thanks to Nicolas Capit), the developers of the Grid'5000 resource management infrastructure. To use these traces, you must include an acknowledgement to the source of the data in any published material that refers to the data. Please also consider refering to the [Grid Workloads Archive](http://gwa.ewi.tudelft.nl/) in the acknowledgements.
