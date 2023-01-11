import csv

def readCVSf(file):
    f = open(file)
    for row in csv.reader(f):
        print(row)
    f.close()
