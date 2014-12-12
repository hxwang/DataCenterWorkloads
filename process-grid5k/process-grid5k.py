from pystats import *

processTimeField = 4
skipLines = 11
with open('../data/anon_jobs_gwf/filtered_grid5000_clean_trace.log') as f:
    res = stats(stream = f, field=processTimeField, delimiter='\t', skip = skipLines, confidence=0.95, navalue = '-1')
    print res
