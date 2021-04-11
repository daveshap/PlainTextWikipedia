from time import sleep
import requests


def solr_index(payload, core='wiki'):
    headers = {'Content-Type':'application/json'}
    if isinstance(payload, dict):  # individual JSON doc
        solr_api = 'http://localhost:8983/solr/%s/update/json/docs?commitWithin=5000' % core
    elif isinstance(payload, list):  # list of JSON docs
        solr_api = 'http://localhost:8983/solr/%s/update?commitWithin=5000' % core
    count = 0
    while True:
        count += 1
        if count > 6:
            return None
        try:
            resp = requests.request(method='POST', url=solr_api, json=payload, headers=headers)
            return resp
        except Exception as oops:
            print(oops)
            sleep(1)