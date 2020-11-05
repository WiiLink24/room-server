import json
import pickle
import pathlib
import os
import printful
import pprint
import pyminizip
import subprocess
import time
from datadog import (
  initialize,
  api,
)
from utilsbylarsen import (
  setup_log,
)
def orderprintful(a, b, c, d, e, f, g, h, i, j, k, privatekey):
  if config["execute_all"]:
    with open("./config.json", "rb") as f:
    config = json.load(f)
  if config["production"] and config["send_logs"] and config["load_options_file"] and config["use_pickle"]:
    load_file1 = open(options.dat, 'rb')
    options = pickle.load(load_file1)
  if config["production"] and config["send_logs"] and config["use_pickle"]:
    setup_log(config["sentry_url"], False)
  if config["production"] and config["use_private_key"]:
    load_file2 = open(password.dat, 'rb')
    privatekey = pickle.load(load_file2)
    path = pathlib.Path(__file__).parent.absolute()
    imgpath = config["printful_cdn_url"] + "/" + jpgname
    a = jpgname
    b = variantid
    c = productname
    d = noofpoints
    e = quantityno
    f = shippingname
    g = address
    h = shippingcity
    i = countrycode
    j = zipno
    pyminizip.uncompress("offset.enc", privatekey, path, int(withoutpath))
    load_file3 = open(offset.dat, 'rb')
    confirmoffset = pickle.load(load_file3)
    if config["production"]
      key = config["printful_api_key"]
      client = Client(key)
      pprint(client.post('orders',
          {
              'recipient':  {
                  'name': shippingname,
                  'address1': address,
                  'city': shippingcity,
                  'state_code': countrycode,
                  'country_code': countrycode,
                  'zip': zipno
              },
              'items': [
                  {
                      'variant_id': variantid, #Small poster
                      'name': productname, #Display name
                      'retail_price': noofpoints, #Retail price for packing slip
                      'quantity': quantityno,
                      'files': [
                          {'url': imgpath}
                      ]
                  }
              ]
          },
          {'confirm': confirmoffset}
      ))
      if os.path.exists("offset.dat"):
        os.remove("offset.dat")
      initialize(**options)
      t = time.localtime()
      timevar = time.strftime("%H:%M:%S", t)
      title = "Latest Order Script Status @ " + timevar
      text = 'Order Script for Printful was ran!'
      tags = ['version:1', 'application:python']
      api.Event.create(title=title, text=text, tags=tags)
      os._exit(0)
