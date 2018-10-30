
import imp
import scopus
from scopus import AuthorRetrieval
from scopus import AbstractRetrieval
au = AuthorRetrieval(18439033600)
import pandas as pd
eids = pd.DataFrame(au.get_document_eids(refresh=False))
data = []

import sys
sys.stdout = open('output.txt','wt')

n=len(eids[0])

for i in range(n):
	print("<tr>")
	# print("<td>"+ str(i+1) + "</td>")
	ab = AbstractRetrieval(eids[0][i], view='FULL')
	print("<td>" + ab.title + "</td>")

	auths = ""
	for author in ab.authorgroup:
		auths = auths + author[5] + ", "
	auths = auths[0:len(auths)-2]
	print("<td>" + auths + "</td>")

	print("<td>" + ab.coverDate[0:4] + "</td>")
	print("<td>" + ab.publicationName + "</td>")
	print("<td>" + str(ab.citedby_count) + "</td>")
	print("</tr>")
