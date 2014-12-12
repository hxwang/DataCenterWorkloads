from pystats import *

processTimeField = 4
skipLines = 12
with open('../data/anon_jobs_gwf/testSample.log') as f:
    res = stats(stream = f, field=processTimeField, delimiter=' ', skip = skipLines, confidence=0.95)
    print res
