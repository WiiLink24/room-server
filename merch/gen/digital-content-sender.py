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
