from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json


myCl = ElsClient('e3de4eeb2b27bef1c2435a7147eeab8a')
myCl.inst_token = 'bb3c94e90c93ee90ebaf74ae13126167'
myAuth = ElsAuthor(uri = 'http://api.elsevier.com/content/author/author_id/18439033600')
print(myAuth.read(myCl))
print(myAuth.full_name)

