import json as a
import pickle as b
import os as c
import pwinty as d
import time as e
from datadog import (
  initialize,
  api,
)
import utilsnotbyme as i
def pwinty(k, l, m, n, o, p, q, r, s, t, u, v, w, x):
  ab="production"
  ac="send_logs"
  ad="use_pickle"
  ae="execute_all"
  z='rb'
  if g[ae]:
    with open("./config.json", z) as f:
    g = a.load(f)
  if g[ab] and g[ac] and g["load_options_file"] and g[ad]:
    h = open(options.dat, z)
    options = b.load(h)
  if g[ab] and g[ac] and g[ad]:
    i.setup_log(g["sentry_url"], False)
  if g[ab] and g["use_private_key"] and g[ae]:
    j = b.load(open(password.dat, z)) 
    #j is the Private key, still need to import this fully, it doesn't work yet.
    y = g["pwinty_cdn_url"] + "/" + x
    #Set x to the name of the image you want printed on the photo
    if g[ab]
      aa=d.Order
      order = aa.create(
          recipient_name=k,
          address_1=l,
          address_2=m,
          address_town_or_city=n,
          state_or_county=o,
          postal_or_zip_code=p,
          destination_country_code=q,
          country_code=r,
          qualityLevel=s
      )
      photo = aa.photos.create(
        type=t,
        url=y,
        md5Hash=u,
        copies=v,
        sizing=w
      )
      initialize(**options)
      ab = "Latest Order Script Status @ " + e.strftime("%H:%M:%S", e.localtime())
      ac = 'Order Script for Photos was ran!'
      ad = ['version:1', 'application:python']
      api.Event.create(title=ab, text=ac, tags=ad)
      c._exit(0)
