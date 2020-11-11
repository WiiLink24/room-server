import json as a
import pickle as b
import ntplib as am
import printful as e
import pprint as i
import pyminizip as g
import random as ah
import datetime as ak
import datadog as an
import utilsnotbyme as ao
def orderprintful(k, l, m, n, o, p, q, r, s, t, u, v, w, ao, ap):
  aa="production"
  ab="send_logs"
  ac="use_pickle"
  ad="execute_all"
  ae='rb'
  af="offset.dat"
  if j[ad]:
    with open("./config.json", ae) as f:
    j = a.load(f)
  if j[aa] and j[ab] and j["load_options_file"] and j[ac]:
    y = open(options.dat, ae)
    options = b.load(y)
  if j[aa] and j[ab] and j[ac]:
    ao.setup_log(j["sentry_url"], False)
  if j[aa] and j["use_private_key"] and j[ad]:
    x = open(password.dat, 'rb')
    ag = b.load(x)
    w = str(j.getcwd())
    v = j["printful_cdn_url"] + "/" + k
    g.uncompress("offset.enc",vag, w, int(withoutpath))
    z = open(af, ae)
    confirmoffset = b.load(z)
    if j[aa]
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
      if os.path.exists(af):
        os.remove(af)
      an.initialize(**options)
      c = am.NTPClient()
      randomizer = ah.randint(0, 24)
      if randomizer==1:
        response = c.request('time1.google.com', version=3)
      elif randomizer==2:
        response = c.request('time2.google.com', version=3)
      elif randomizer==3:
        response = c.request('time3.google.com', version=3)
      elif randomizer==4:
        response = c.request('time4.google.com', version=3)
      elif randomizer==5:
        response = c.request('0.pool.ntp.org', version=3)
      elif randomizer==6:
        response = c.request('1.pool.ntp.org', version=3)
      elif randomizer==7:
        response = c.request('2.pool.ntp.org', version=3)
      elif randomizer==8:
        response = c.request('time-a-g.nist.gov', version=3)
      elif randomizer==9:
        response = c.request('time-c-g.nist.gov', version=3)
      elif randomizer==10:
        response = c.request('time-d-g.nist.gov', version=3)
      elif randomizer==11:
        response = c.request('time-e-g.nist.gov', version=3)
      elif randomizer==12:
        response = c.request('time-a-wwv.nist.gov', version=3)
      elif randomizer==13:
        response = c.request('time-b-wwv.nist.gov', version=3)
      elif randomizer==14:
        response = c.request('time-c-wwv.nist.gov', version=3)
      elif randomizer==15:
        response = c.request('time-d-wwv.nist.gov', version=3)
      elif randomizer==16:
        response = c.request('time-e-wwv.nist.gov', version=3)
      elif randomizer==17:
        response = c.request('time-a-b.nist.gov', version=3)
      elif randomizer==18:
        response = c.request('time-b-b.nist.gov', version=3)
      elif randomizer==19:
        response = c.request('time-c-b.nist.gov', version=3)
      elif randomizer==20:
        response = c.request('time-d-b.nist.gov', version=3)
      elif randomizer==21:
        response = c.request('time-e-b.nist.gov', version=3)
      elif randomizer==22:
        response = c.request('time.nist.gov', version=3)
      elif randomizer==23:
        response = c.request('utcnist.colorado.edu', version=3)
      elif randomizer==24:
        response = c.request('tcnist2.colorado.edu', version=3)
      else:
        response = c.request('time.cloudflare.com', version=3)
      response.offset
      ah = str(ak.fromtimestamp(response.ao, timezone.ap)))
      ai = "Latest Order Script Status @ " + ah
      aj = 'Order Script for Printful was ran!'
      al = ['version:1', 'application:python']
      an.api.Event.create(title=ai, text=aj, tags=al)
      exit()
