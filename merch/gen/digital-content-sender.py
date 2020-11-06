import sendgrid
import os
from sendgrid.helpers.mail import *
def send(to, from, subjectdata, contentdata, key):
  sg = sendgrid.SendGridAPIClient(api_key=os.environ.get(key))
  from_email = Email(from)
  to_email = To(to)
  subject = subjectdata
  content = Content("text/plain", contentdata)
  mail = Mail(from_email, to_email, subject, content)
  response = sg.client.mail.send.post(request_body=mail.get())
  print(response.status_code)
  print(response.body)
  print(response.headers)
