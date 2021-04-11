import requests


def solr_index(payload, core='wiki'):
    headers = {'Content-Type':'application/json'}
    if isinstance(payload, dict):  # individual JSON doc
        solr_api = 'http://localhost:8983/solr/%s/update/json/docs' % core
    elif isinstance(payload, list):  # list of JSON docs
        solr_api = 'http://localhost:8983/solr/%s/update' % core
    resp = requests.request(method='POST', url=solr_api, json=payload, headers=headers)
    return resp