import imp
from scopus import ScopusSearch
import pandas as pd
s = ScopusSearch('AF-ID(60005510) AND SUBJAREA(ceng)', refresh=False)

res = pd.DataFrame(s.results)

import sys
sys.stdout = open('doiScopus.txt','wt')

for i in range(len(res)):
        print(res.iloc[i,1], end=",")
        print(res.iloc[i,0])
