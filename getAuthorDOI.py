import imp
import scopus
from scopus import AuthorRetrieval
from scopus import AbstractRetrieval
import pandas as pd

# put the ID of the author you want to get the DOIs
author_id = 18439033600

# pull the data
au = AuthorRetrieval(author_id)

# parse the data as DataFrame
eids = pd.DataFrame(au.get_document_eids(refresh=False))

# direct the stdout print to text file
import sys
sys.stdout = open('doiScopus.txt','wt')

# get the number of DOI pulled
n=len(eids[0])

for i in range(n):
    # pull the details of the article, FULL means get all the fields.
    ab = AbstractRetrieval(eids[0][i], view='FULL')
    print(ab.doi, end=",")
    print(ab.scopus_link)
