import json
import sys
import sentry_sdk
import subprocess
import pathlib
from datadog import statsd
from pprint import pprint
from printfulutils import (
    Printful,
    setup_log,
    log,
    senddatadoglogs,
    statisticssender,
    configpathreturner,
    rbdata,
    dynamicmain,
    dynamicsecn,
    dynamicmainothr,
    datareturner,
    Client,
    PrintfulApiException,
)

currentpath = pathlib.Path(__file__).parent.absolute()
scriptidmain = datareturner(currentpath)
scriptidsecn = dynamicmain(scriptidmain)
filenamemain = dynamicsecn(scriptidsecn)
filenamesecn = dynamicothr(scriptidsecn)
configpathvar = configpathreturner(filenamemain)
rbdatavar = rbdata(filenamesecn)
with open(configpathvar, rbdatavar) as f:
    config = json.load(f)
sentryurl = config["sentry_url"]
key = config["printful_key"]
production = config["production"]
sender = config["send_stats"]
appkey = config["datadog_api_key"]
apikey = config["datadog_app_key"]
phpname = config["phpfilename"]
logphp = config["php_logger_path"]
method = config["php_logger_method"]
booleanvariable = config["send_php_logs"]
setup_log(sentryurl, False)
pf = Printful(key)
client = Client(key)
orders = pf.get("orders")
options = {"api_key": appkey, "app_key": apikey}
if production and sender:
    senddatadoglogs(production, sender, options, data)
if production and sender and booleanvariable:
    statisticssender(logphp, method, phpname)
#     pprint(client.post('orders',
#         {
#             'recipient':  {
#                 'name': 'John Doe',
#                 'address1': '172 W Providencia Ave #105',
#                 'city': 'Burbank',
#                 'state_code': 'CA',
#                 'country_code': 'US',
#                 'zip': '91502'
#             },
#             'items': [
#                 {
#                     'variant_id': 1, #Small poster
#                     'name': 'Niagara Falls poster', #Display name
#                     'retail_price': '19.99', #Retail price for packing slip
#                     'quantity': 1,
#                     'files': [
#                         {'url': 'http://example.com/files/posters/poster_1.jpg'}
#                     ]
#                 }
#             ]
#         },
#         {'confirm': 1}
#     ))
# #Calculate shipping rates for an order
# pprint(client.post('shipping/rates', data=json.dumps({
#     'recipient': {
#         'country_code': 'DE',
#     },
#     'items': [
#        {'variant_id': 1, 'quantity': 1}, #Small poster
#        {'variant_id': 1118, 'quantity': 2} #Alternative T-Shirt
#     ]
# })).json())
# obtain info about orders
# pf.get('orders', params={'offset': 5, 'limit':10})
print("Currently incomplete.")
sys.exit(1)
