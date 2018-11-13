import imp
import scopus
from scopus import AuthorRetrieval
from scopus import AbstractRetrieval
import pandas as pd
au = AuthorRetrieval(18439033600)

eids = pd.DataFrame(au.get_document_eids(refresh=False))
data = []

import sys
sys.stdout = open('doi.txt','wt')

n=len(eids[0])

resultScopus = []

for i in range(n):
    ab = AbstractRetrieval(eids[0][i], view='FULL')
    resultScopus.append(str(ab.doi))
    print(ab.doi, end=",")
    print(ab.scopus_link)

# resultNTU = []
# with open("regex.csv", "r") as ins:
#     for line in ins:
#         resultNTU.append(line)

# for r in resultScopus:
#     if r in resultNTU:
#         print("Found ", r)
#     else:
#         print("Not found ", r)
    