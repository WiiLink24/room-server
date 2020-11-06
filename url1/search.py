from elasticsearch import Elasticsearch
from flask import request
from helpers import xml_node_name
es = Elasticsearch('http://localhost:9200')
@app.route('/url2/search.cgi')
@xml_node_name('SearchMovies')
def search():
    q = request.args.get('q')
    es.search(index='tv_index', body={'query': {'match': {'title': q}}})
    
