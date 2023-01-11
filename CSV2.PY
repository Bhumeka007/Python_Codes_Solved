import csv
def readCSVf(file):
    f = open(file)
    data = []
    for row in csv.reader(f):
        data.append(row)
    print(data)
    f.close()
