

def getColumn(skip, column, inputfile, outputfile):
	with open(inputfile) as f:
		lines_after_skip = f.readlines()[(int)skip:]
	close(inputfile)
	with open(outputfile) as f:
		for item in lines_after_skip:
			print >> f, item

if name == '__name__':
	getColumn(skip, column, inputfile, outputfile)

