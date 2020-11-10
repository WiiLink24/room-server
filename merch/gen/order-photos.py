import json as a
import pickle as b
import os as c
import pwinty as d
import time as e
from datadog import (
  initialize,
  api,
)
from utilsbylarsen import (
  setup_log,
)
z = 'rb' #Generic Text Writing Opcode
def orderpwinty(k, l, m, n, o, p, q, r, s, t, u, v, w, x):
  if g["execute_all"]:
    with open("./config.json", "rb") as f:
    g = a.load(f)
  if g["production"] and g["send_logs"] and g["load_options_file"] and g["use_pickle"]:
    h = open(options.dat, z)
    options = b.load(h)
  if g["production"] and g["send_logs"] and g["use_pickle"]:
    setup_log(g["sentry_url"], False)
  if g["production"] and g["use_private_key"] and g["execute_all"]:
    i = open(password.dat, 'rb')
    j = b.load(i) #Private key, still need to import this fully, it doesn't work yet.
    y = g["pwinty_cdn_url"] + "/" + x #Set x to the name of the image you want printed on the photo
    k = recipient_name1
    l = address1
    m = address2
    n = address_town_or_city1
    o = state_or_county1
    p = postal_or_zip_code1
    q = destination_country_code1
    r = countrycode
    s = qualityLevel1
    t = type1
    u = md5Hash1
    v = copies1
    w = sizing1
    if g["production"]
      order = d.Order.create(
          recipient_name =         	recipient_name1,
          address_1 =              	address1,
          address_2 =              	address2,
          address_town_or_city =   	address_town_or_city1,
          state_or_county =        	state_or_county1,
          postal_or_zip_code =     	postal_or_zip_code1,
          destination_country_code =	destination_country_code1,
          country_code =           	countrycode,
          qualityLevel =           	qualityLevel1
      )
      photo = order.photos.create(
        type =   	type1,
        url =    	y,
        md5Hash =	md5Hash1,
        copies = 	copies1,
        sizing = 	sizing1
      )
      initialize(**options)
      t = e.localtime()
      timevar = e.strftime("%H:%M:%S", t)
      title = "Latest Order Script Status @ " + timevar
      text = 'Order Script for Photos was ran!'
      tags = ['version:1', 'application:python']
      api.Event.create(title=title, text=text, tags=tags)
      c._exit(0)
