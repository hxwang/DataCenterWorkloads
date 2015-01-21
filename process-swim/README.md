## [SWIM](https://github.com/SWIMProjectUCB/SWIM/wiki)

### Objective
Analyze the **release time** and **processing time** of Facebook workload [SWIM](https://github.com/SWIMProjectUCB/SWIM/wiki). 
- However, in the workload traces, they only made public of the following field
  - job release time
  - job map bytes, shuffle bytes and reduce bytes
- What we need is processing time, which unfortunately, is not made public.

### Altenative Solution
- [[Cheng-2014]](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6877265&tag=1) mimic the characteristics of the jobs using "loadgen". Loadgen is a configurable MapReduce job from the Gridmix2 benchmark in the Hadoop distribution.
