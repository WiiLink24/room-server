import json as a
import pickle as b
import os as c
import pwinty as d
import time as e
from datadog import (
  initialize,
  api,
)
import utilsbylarsen as i
z = 'rb' #Generic Text Writing Opcode
def orderpwinty(k, l, m, n, o, p, q, r, s, t, u, v, w, x):
  if g["execute_all"]:
    with open("./config.json", "rb") as f:
    g = a.load(f)
  if g["production"] and g["send_logs"] and g["load_options_file"] and g["use_pickle"]:
    h = open(options.dat, z)
    options = b.load(h)
  if g["production"] and g["send_logs"] and g["use_pickle"]:
    i.setup_log(g["sentry_url"], False)
  if g["production"] and g["use_private_key"] and g["execute_all"]:
    j = b.load(open(password.dat, z)) 
    #j is the Private key, still need to import this fully, it doesn't work yet.
    y = g["pwinty_cdn_url"] + "/" + x
    #Set x to the name of the image you want printed on the photo
    if g["production"]
      order = d.Order.create(
          recipient_name =         	k,
          address_1 =              	l,
          address_2 =              	m,
          address_town_or_city =   	n,
          state_or_county =        	o,
          postal_or_zip_code =     	p,
          destination_country_code =	q,
          country_code =           	r,
          qualityLevel =           	s
      )
      photo = order.photos.create(
        type =   	t,
        url =    	y,
        md5Hash =	u,
        copies = 	v,
        sizing = 	w
      )
      initialize(**options)
      title = "Latest Order Script Status @ " + e.strftime("%H:%M:%S", e.localtime())
      text = 'Order Script for Photos was ran!'
      tags = ['version:1', 'application:python']
      api.Event.create(title=title, text=text, tags=tags)
      c._exit(0)
