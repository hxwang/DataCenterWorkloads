import sys

def getInterArrivalTime(inputfile, outputfile):
  
  # read from file, skip lines
  with open(inputfile, 'r') as f:
    lines = f.readlines()
  
  # write target column to output files
  with open(outputfile, 'w') as f2:
    for i in range(len(lines)-1):
      item = (int)(lines[i+1])- (int)(lines[i])
      print >> f2, item

if __name__ == '__main__':
  getInterArrivalTime(sys.argv[1],sys.argv[2])
