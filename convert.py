import re
s = "Example String"
replaced = re.sub('', 'a', s)
print(replaced)

import csv

import sys
sys.stdout = open('regex.csv','wt')
with open('NTU_DOI.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile, delimiter=';')
    for row in csvReader:
        print(re.sub(r'^\D+','',row[2]))
    