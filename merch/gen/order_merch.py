import json
import sys
import sentry_sdk
import pathlib
from datavars import (
    data00,
    data01,
    data02,
    data03,
    data04,
    data05,
    data06,
    data07,
    data08,
    data09,
    data10,
    data11,
    data12,
)
from datadog import statsd
from pprint import pprint
from printfulutils import ( # printfulutils can be downloaded at github.com/WiiLink24/printful
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
    zero,
    one,
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
sentryurl = config[data00]
key = config[data01]
production = config[data02]
sender = config[data03]
appkey = config[data04]
apikey = config[data05]
phpname = config[data06]
logphp = config[data07]
method = config[data08]
booleanvariable = config[data09]
setup_log(sentryurl, False)
pf = Printful(key)
client = Client(key)
orders = pf.get(data11)
options = {data10: appkey, data12: apikey}
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
sys.exit(one)
# When the script is done, replace the word one with the word zero and it will auto-update the script to output the proper return code.
