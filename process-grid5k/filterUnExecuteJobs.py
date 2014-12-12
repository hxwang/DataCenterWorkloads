from pystats import *

#filter unstarted workloads
def filterUnExecuteJobs():
	with open('../data/anon_jobs_gwf/grid5000_clean_trace.log') as f:
		outfile = open('../data/anon_jobs_gwf/filtered_grid5000_clean_trace.log','w')
		skip = 12
		colIndex = 3
		lines = f.readlines()[skip:]
		for line in lines:
			if (int)(line[colIndex]) > 0:
				outfile.write(line +'\n')

    
if __name__ == "__main__":
	filterUnExecuteJobs()
