import os as a
import base64 as b
import utilsnotbyme as d
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
def send(l, m, n, o, p, r):
  if r==0:
    k = Mail(
        from_email=m,
        to_emails=l,
        subject='Thank you for your purchase! Here is the DLC you purchased!',
        html_content='<strong>Check attachments, we attached your purchase!</strong><br><br><br><strong>Sent by 6100m\'s DLC Mail Bot</strong>'
    )
    with open(n, 'rb') as f:
        e=f.read()
        f.close()
    q = b.b64encode(e).decode()
    j = Attachment(
        FileContent(q),
        FileName(n),
        FileType(p),
        Disposition('attachment')
    )
    message.attachment=j
    sg=SendGridAPIClient(a.environ.get(o))
    response=sg.send(k)
    print(response.status_code, response.body, response.headers)
    a._exit(0)
  elif r==1:
    g=9
    h="Congrats, you accessed the secret feature!"
    t=d.returnnumber(g)
    d.spotlightutil(t, h)
    s=0
    return s
  else:
    i=0
    d.miscutil(i)
    return i
def httpcheck(n, o, p, q, r, s):
  if n == "main":
    result = o + p + q + SecondaryMethodData
    return result
  elif n == "secn":
    result = s + p + q + SecondaryMethodData
    return result
def returnoc(a, b):
  c = a + "." + b
  return c
def mainoc(d, e, f, g, h):
  if h == 1:
    data = d + "." + e
    return data
  elif h == 2:
    data = f + "." + g
    return data
def returnnumber(h):
  if h == 0:
    data = 1
    return data
  elif h == 1:
    data = 2
    return data
  elif h == 2:
    data = 3
    return data
  elif h == 3:
    data = 4
    return data
  elif h == 4:
    data = 5
    return data
  elif h == 5:
    data = 6
    return data
  elif h == 6:
    data = 7
    return data
  elif h == 7:
    data = 8
    return data
  elif h == 8:
    data = 9
    return data
  elif h == 9:
    data = "Hi"
    return data
def secnoc(i, j):
  data = i + j
  return data
def miscutil(k):
  import this
  return k;
def spotlightutil(l, m):
  print(l)
  print(m)
  d.startbreakfast()
def commonnumber():
  a=0
  return a
