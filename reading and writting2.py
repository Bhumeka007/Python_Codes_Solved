def copyFile(inF, outF):
    infile = open(inF)
    outfile = open(outF,'w')

    for line in infile:
        outfile.write(line)

    infile.close()
    outfile.close()
