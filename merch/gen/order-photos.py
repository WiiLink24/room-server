import json
import pickle
import pathlib
import os
import pwinty
import pyminizip
import time
from datadog import (
  initialize,
  api,
)
from utilsbylarsen import (
  setup_log,
)
def orderpwinty(a, b, c, d, e, f, g, h, i, j, k, l, m):
  if config["execute_all"]:
    with open("./config.json", "rb") as f:
    config = json.load(f)
  if config["production"] and config["send_logs"] and config["load_options_file"] and config["use_pickle"]:
    load_file1 = open(options.dat, 'rb')
    options = pickle.load(load_file1)
  if config["production"] and config["send_logs"] and config["use_pickle"]:
    setup_log(config["sentry_url"], False)
  if config["production"] and config["use_private_key"] and config["execute_all"]:
    load_file2 = open(password.dat, 'rb')
    privatekey = pickle.load(load_file2)
   path = pathlib.Path(__file__).parent.absolute()
   imgpath = config["pwinty_cdn_url"] + "/" + jpgname
    a = recipient_name1
    b = address1
    c = address2
    d = address_town_or_city1
    e = state_or_county1
    f = postal_or_zip_code1
    g = destination_country_code1
    h = countrycode
    i = qualityLevel1
    j = type1
    k = md5Hash1
    l = copies1
    m = sizing1
    pyminizip.uncompress("offset.enc", privatekey, path, int(withoutpath))
    load_file3 = open(offset.dat, 'rb')
    confirmoffset = pickle.load(load_file3)
    if config["production"]
      order = pwinty.Order.create(
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
        url =    	imgpath,
        md5Hash =	md5Hash1,
        copies = 	copies1,
        sizing = 	sizing1
      )
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
