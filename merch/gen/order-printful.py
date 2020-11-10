import json as a
import pickle as b
import pathlib as c
import os as d
import printful as e
import pprint as i
import pyminizip as g
import time as h
from datadog import (
  initialize,
  api,
)
from utilsbylarsen import (
  setup_log,
)
def orderprintful(k, l, m, n, o, p, q, r, s, t, u):
  if j["execute_all"]:
    with open("./config.json", "rb") as f:
    j = a.load(f)
  if j["production"] and j["send_logs"] and j["load_options_file"] and j["use_pickle"]:
    y = open(options.dat, 'rb')
    options = b.load(y)
  if j["production"] and j["send_logs"] and j["use_pickle"]:
    setup_log(j["sentry_url"], False)
  if j["production"] and j["use_private_key"] and j["execute_all"]:
    x = open(password.dat, 'rb')
    privatekey = b.load(x)
    w = c.Path(__file__).parent.absolute()
    v = j["printful_cdn_url"] + "/" + k
    g.uncompress("offset.enc", privatekey, w, int(withoutpath))
    z = open(offset.dat, 'rb')
    confirmoffset = b.load(z)
    if j["production"]
      key = j["printful_api_key"]
      client = e.Client(key)
      i(client.post('orders',
          {
              'recipient':  {
                  'name': p,
                  'address1': q,
                  'city': r,
                  'state_code': u,
                  'country_code': s,
                  'zip': t
              },
              'items': [
                  {
                      'variant_id': l, #Small poster
                      'name': m, #Display name
                      'retail_price': n, #Retail price for packing slip
                      'quantity': o,
                      'files': [
                          {'url': v}
                      ]
                  }
              ]
          },
          {'confirm': confirmoffset}
      ))
      if os.path.exists("offset.dat"):
        os.remove("offset.dat")
      initialize(**options)
      t = h.localtime()
      timevar = h.strftime("%H:%M:%S", t)
      title = "Latest Order Script Status @ " + timevar
      text = 'Order Script for Printful was ran!'
      tags = ['version:1', 'application:python']
      api.Event.create(title=title, text=text, tags=tags)
      d._exit(0)
