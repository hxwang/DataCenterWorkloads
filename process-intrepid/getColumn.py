import sys

def getColumn(skip, column, inputfile, outputfile):
  
  # read from file, skip lines
  with open(inputfile, 'r') as f:
    lines_after_skip = f.readlines()[(int)(skip):]
  
  # write target column to output files
  with open(outputfile, 'w') as f2:
    for line in lines_after_skip:
      items = line.split(' ')
      if len(items) >= column:
        print >> f2, items[column]

if __name__ == '__main__':
  getColumn(int(sys.argv[1]), int(sys.argv[2]), sys.argv[3],sys.argv[4])
