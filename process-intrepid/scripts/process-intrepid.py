from pystats import *

#since the first column is null, thus here processTimeField refers to column 4, i.e., processing time
processTimeField = 5
skipLines = 15
with open('../data\ANL-Intrepid-2009-1.swf\ANL-Intrepid-2009-1.swf') as f:
    res = stats(stream = f, field=processTimeField, delimiter=' ', skip = skipLines, confidence=0.95, navalue = '-1')
    print res
