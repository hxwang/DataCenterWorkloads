import sys

def getColumn(skip, column, inputfile, outputfile):
  with open(inputfile, 'r') as f:
    lines_after_skip = f.readlines()[(int)(skip):]

  print len(lines_after_skip)
  with open(outputfile, 'w') as f2:
    for line in lines_after_skip:
      items = line.split(' ')
      if len(items) >= column:
      	print items[column]
        print >> f2, items[column]

if __name__ == '__main__':
  getColumn( sys.argv[1], sys.argv[2], sys.argv[3],sys.argv[4])
