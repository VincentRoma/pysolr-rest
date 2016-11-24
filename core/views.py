from flask import request, jsonify
from flask.views import MethodView
import requests
import json
import settings
from solr import Solr


'''
    Create a connection to a solr server

'''
class DataAPI(MethodView):
    def __init__(self):
        self.url = "http://{}:{}/solr/{}".format(settings.HOST,settings.PORT,settings.COLLECTION)
        self.s = Solr(self.url, timeout=10)

    def get(self, field, params):
        rows = 20
        page = 0
        query = "*:*"
        if field:
            query = "{}:*{}*".format(field, params)
        print "[QUERY] - field: {}, params: {}, query: {}".format(field, params, query)
        response = self.s.search(query)
        return json.dumps(response.raw_response['response'])
