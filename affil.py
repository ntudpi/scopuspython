import imp
from scopus import ScopusSearch
import pandas as pd
s = ScopusSearch('AF-ID(60005510) AND SUBJAREA(nurs)', refresh=False)

res = pd.DataFrame(s.results)

import sys
sys.stdout = open('NanyangNursing.txt','wt')

for c in res.columns:
	print(c, end="	")

print()
for i in range(5):
	for j in range(len(res.columns)):
		print(res.iloc[i,j], end="	")
	print()