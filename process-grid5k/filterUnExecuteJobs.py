from pystats import *
import re

patt = re.compile("[^\t]+")
#filter unstarted workloads, which has value in column smaller than 0
def filterUnExecuteJobs():
	with open('../data/anon_jobs_gwf/grid5000_clean_trace.log') as f:
		outfile = open('../data/anon_jobs_gwf/filtered_grid5000_clean_trace.log','w')
		skip = 13
		colIndex = 3
		lines = f.readlines()[skip:]
		for line in lines:
			items = patt.findall(line)      
			# print len(items)
			if (int)(items[colIndex]) > 0:
				outfile.write(line +'\n')

    
if __name__ == "__main__":
	filterUnExecuteJobs()
