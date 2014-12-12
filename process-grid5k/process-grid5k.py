from pystats import *

processTimeField = 4
skipLines = 11
with open('../data/anon_jobs_gwf/testSample.log') as f:
    res = stats(stream = f, field=processTimeField, delimiter=' ', skip = skipLines, confidence=0.95)
    print res
