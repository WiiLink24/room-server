import json as a
import pickle as b
import os as c
import pwinty_py3 as d
import datadog as am
import utilsnotbyme as i
import ntplib as ar
import pyminizip as aq
import digitalcontentsender as au
def pwinty(k, l, m, n, o, p, q, r, s, t, u, v, w, ao, ap, x):
  z='rb'
  with open("./config.json", z) as f:
    g = a.load(f)
    ab=g["pwinty_production"]
    ac=g["pwinty_send_logs"]
    ad=g["pwinty_use_pickle"]
    ae=g["pwinty_execute_all"]
  if ab==True and ac==True and g["pwinty_load_options_file"] and ad==True:
    if c.path.exists("options.dat"):
      h = open(options.dat, z)
      options = b.load(h)
    else:
      bb = "Uh-oh!"
      i.log("options.dat does not exist!! %s" % bb, "CRITICAL")
  if ab==True and ac==True and ad==True:
    i.setup_log(g["pwinty_sentry_url"], False)
  if ab==True and g["pwinty_use_private_key"] and ae==True:
    j = b.load(open(password.dat, z)) 
    #j is the Private key, still need to import this fully, it doesn't work yet.
    y = g["pwinty_cdn_url"] + "/" + x
    #Set x to the name of the image you want printed on the photo
    if ab==True:
      af=d.Order
      order = af.create(
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
      photo = af.photos.create(
        type=t,
        url=y,
        md5Hash=u,
        copies=v,
        sizing=w
      )
      am.initialize(**options)
      c = ar.NTPClient()
      randomizer = digitalcontentsender.ntprandomizer()
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
      ah = au.dateconverter(ao, ap)
      ai = "Latest Order Script Status @ " + ah
      aj = 'Order Script for Photos was ran!'
      ak = ['version:1', 'application:python']
      am.api.Event.create(title=ai, text=aj, tags=ak)
      c._exit(0)
