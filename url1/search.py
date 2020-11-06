from elasticsearch import Elasticsearch
from flask import request
es = Elasticsearch('http://localhost:9200')
@app.route('/url2/search.cgi')
def search():
    q = request.args.get('q')
    es.search(index='tv_index', body={'query': {'match': {'title': q}}})
    
