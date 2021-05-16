'''import pysolr
from pprint import pprint as pp

solr = pysolr.Solr('http://localhost:8983/solr/wiki/', always_commit=True) # , [timeout=10], [auth=<type of authentication>])
print(solr.ping())

results = solr.search('bacon')
print(len(results))

for result in results:
    print(result['title'])'''


from solr_functions import *

results = solr_search("Abraham")
print(results.json())