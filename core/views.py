from flask import request, jsonify
from flask.views import MethodView
import requests
import json
import settings
from solr import Solr

'''
    Solr base class to define global paramaters

'''
class SolrAPI(MethodView):
    def __init__(self):
        self.url = "http://{}:{}/solr/{}".format(settings.HOST,settings.PORT,settings.COLLECTION)
        self.s = Solr(self.url, timeout=10)

    def get(self):
        pass

'''
    Implement the SolrAPI interface for plain text search

'''
class DataAPI(SolrAPI):

    def get(self, field, params):
        rows = 20
        page = 0
        query = "*:*"
        if field:
            query = "{}:*{}*".format(field, params)
        print "[QUERY] - field: {}, params: {}, query: {}".format(field, params, query)
        response = self.s.search(query)
        return json.dumps(response.raw_response['response'])


'''
    Implement the SolrAPI interface for SUGGESTION search

'''
class SuggestionAPI(SolrAPI):

    def get(self, field, params):
        results = []
        response = self.s.suggest_terms(field,params)
        for item in response.itervalues():
            results.append(item)
        print "[SUGGESTION] - {}".format(json.dumps(results))
        return json.dumps(results)
        # return json.dumps(response.raw_response['response'])
