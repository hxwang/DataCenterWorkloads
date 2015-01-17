def getColumn(skip, column, inputfile, outputfile):
  with open(inputfile, 'r') as f:
    lines_after_skip = f.readlines()[skip:]

  with open(outputfile, 'w') as f:
    for line in lines_after_skip:
      items = line.split(' ')
      if len(items) > column:
        print >> f, items[column]

if __name__ == '__main__':
  getColumn(skip, column, inputfile, outputfile)
