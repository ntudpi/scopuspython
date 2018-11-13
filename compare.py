import sys
sys.stdout = open('result.csv','wt')

import csv
resultScopus = {}
with open('doi.txt') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        resultScopus[row[0]]=row[1]

resultNTU = []
with open("regex.csv", "r") as ins:
    for line in ins:
        resultNTU.append(line[:-1])

for r in resultScopus:
    if r in resultNTU:
        print("Found",end=",")
        print(r)
    else:
        print("Not found",end=",")
        print(r,end=",")
        print(resultScopus[r])
    