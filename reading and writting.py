def printFile(file):
    infile = open(file)
    for line in infile:
        print(line,end=" ")

    infile.close()
