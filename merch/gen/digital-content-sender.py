import os as a
import base64 as b
import sys as c
import utilsbygloom as d
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
def send(l, m, n, o, p, r):
  if r == 0:
    s = 'rb' #Generic Text File Writing Opcode
    t = 'attachment' #Attachment Idenitifer Data
    u = SendGridAPIClient #APIClient Class Definition
    v = a.environ.get(o) #Key Data Definition
    w = sg.send #Sendgrid Sender Class Definition
    x = b.b64encode #Base64 Encode Class Definition
    y = 'Thank you for your purchase! Here is the DLC you purchased!' #Hardcoded Subject Data
    z = '<strong>Check attachments, we attached your purchase!</strong><br><br><br><strong>Sent by 6100m\'s DLC Mail Bot</strong>' #Hardcoded HTML Data
    k = Mail(
        from_email=m,
        to_emails=l,
        subject=y,
        html_content=z
    )
    with open(n, s) as f:
        e = f.read()
        f.close()
    q = x(e).decode()
    j = Attachment(
        FileContent(q),
        FileName(n),
        FileType(p),
        Disposition(t)
    )
    message.attachment = j
    sg = u(v)
    response = w(k)
    print(response.status_code, response.body, response.headers)
    c.exit(0)
  elif r == 1:
    g = 9
    h = "Congrats, you accessed the secret feature!"
    echodata = utilsbygloom.returnnumber(g)
    d.spotlightutil(echodata, h)
  else:
    i = 0
    d.miscutil(i)
    return i
