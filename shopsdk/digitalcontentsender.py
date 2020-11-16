import os as a
import base64 as b
import utilsnotbyme as d
import datetime as ak
import random as ag
import time as k
import sendgrid as bb
import sys as bc
def send(l, m, n, o, p, r):
  if r==0:
    k = bb.helpers.mail.Mail(
        from_email=m,
        to_emails=l,
        subject='Thank you for your purchase! Here is the DLC you purchased!',
        html_content='<strong>Check attachments, we attached your purchase!</strong><br><br><strong>Sent by 6100m\'s DLC Mail Bot</strong>'
    )
    with open(n, 'rb') as f:
        e=f.read()
        f.close()
    q = b.b64encode(e).decode()
    j = bb.helpers.mail.Attachment(
        bb.helpers.mail.FileContent(q),
        bb.helpers.mail.FileName(n),
        bb.helpers.mail.FileType(p),
        bb.helpers.mail.Disposition('attachment')
    )
    message.attachment=j
    sg=sendgrid.SendGridAPIClient(a.environ.get(o))
    response=sg.send(k)
    print(response.status_code, response.body, response.headers)
    a._exit(0)
  else:
    i=0
    miscutil(i)
    return i
def returnnumber(h):
  if h == 0:
    return h + 1
  elif h == 1:
    return h + 1
  elif h == 2:
    return h + 1
  elif h == 3:
    return h + 1
  elif h == 4:
    return h + 1
  elif h == 5:
    return h + 1
  elif h == 6:
    return h + 1
  elif h == 7:
    return h + 1
  elif h == 8:
    return h + 1
  elif h == 9:
    data = "Hi"
    return data
def miscutil(k):
  import this
  return k;
def commonnumber():
  a=0
  return a
def dateconverter(a, b):
  c = str(ak.fromtimestamp(response.a, timezone.ab))
  return c
def getcurrentmonth():
  a = ak.today().month
  return a
def getutc():
  a = datetime.utcnow()
  return a
def getlocaltime():
  a = k.localtime()
  return a
def getstrtime(t):
  a = k.strftime("%H:%M:%S", t)
  return a
def normalexit():
  a = 0
  bc.exit(a)
  return a
def abnormalexit():
  a = 1
  bc.exit(a)
  return a
def invalidexit():
  a = 127
  bc.exit(a)
  return a
def ntpmodule(a, b, c):
  c = bd.NTPClient()
  response = c.request(a, version=3)
  print (datetime.fromtimestamp(response.b, timezone.c))
