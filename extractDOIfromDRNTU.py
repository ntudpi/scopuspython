import csv
import sys
import re

# redirect stdout print to file
sys.stdout = open('DR-NTU_ExtractDOI.csv','wt')

with open('NTU_DOI.csv') as csvDataFile:
    # open the file
    csvReader = csv.reader(csvDataFile, delimiter=';')
    for row in csvReader:
        # use regex expression to get only the uniform DOI formatting "10/..."
        print(re.sub(r'^\D+','',row[2]))
    