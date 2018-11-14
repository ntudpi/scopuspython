import sys
# redirect output
sys.stdout = open('compareResult.csv','wt')

# read the csv and store it as dictionary of DOI : URL
import csv
resultScopus = {}
with open('doiScopus.txt') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=',')
    for row in csvReader:
        resultScopus[row[0]]=row[1]

# read the csv from DR-NTU DOIs
resultNTU = []
with open("DR-NTU_ExtractDOI.csv", "r") as ins:
    for line in ins:
        resultNTU.append(line[:-1])

# compare and output
for r in resultScopus:
    if r in resultNTU:
        print("Found",end=",")
        print(r)
    else:
        print("Not found",end=",")
        print(r,end=",")
        print(resultScopus[r])
    