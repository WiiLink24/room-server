import os
import base64
import sys
import utilsbygloom
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)
def send(to, fromdata, subjectdata, nameofattachment, key, filetype, offset):
  if offset == 0:
    message = Mail(
        from_email=fromdata,
        to_emails=to,
        subject='Thank you for your purchase! Here is the DLC you purchased!',
        html_content='<strong>Check attachments, we attached your purchase!</strong><br><br><br><strong>Sent by 6100m\'s DLC Mail Bot</strong>'
    )
    with open(nameofattachment, 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()
    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName(nameofattachment),
        FileType(filetype),
        Disposition('attachment')
    )
    message.attachment = attachedFile
    sg = SendGridAPIClient(os.environ.get(key))
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)
    sys.exit(0)
  elif offset == 1:
    print("Congrats, you accessed the secret feature!")
    offset = 9
    echodata = utilsbygloom.returnnumber(offset)
    utilsbygloom.spotlightutil(echodata)
