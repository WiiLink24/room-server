import pickle
import binascii
import json
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
Mail, 
Attachment, 
FileContent, 
FileName, 
FileType, 
Disposition
)
class sdk(thetoemail, filetosend, currentnoofpoints, pointsneeded, contenttype):
  def send(thetoemail, filetosend, currentnoofpoints, pointsneeded, contenttype):
    with open(str(os.getcwd()) + "./config.json", "rb") as f:
      config = json.load(f)
    message = Mail(
      from_email=reader.readthefromemail(),
      to_emails=thetoemail,
      subject=reader.readsubject(),
      html_content=reader.readhtml()
    )
    with open(filetosend, 'rb') as f:
      data = f.read()
      f.close()
    encoded_file = binascii.b2a_base64(data).decode()
    attachedFile = Attachment(
      FileContent(encoded_file),
      FileName(filetosend),
      FileType(contenttype),
      Disposition('attachment')
    )
    message.attachment = attachedFile
    sg = SendGridAPIClient(config["sendgrid_api_key"])
    response = sg.send(message)
    data = str(currentnoofpoints - pointsneeded)
    returndata = str(data) + str(defs.padding()) + str(" \\\\\\ ") + str(defs.padding()) + str(response.status_code, response.body, response.headers)
    return returndata;
class writer():
  def writehtml():
    htmldata = '<strong>Check attachments, we attached your purchase!</strong><br><br><br><strong>Sent by 6100m\'s DLC Mail Bot</strong>'
    savefile = open(str(os.getcwd()) + 'html.dat', 'wb')
    pickle.dump(htmldata, savefile)
    savefile.close()
    returndata = defs.zero()
    return returndata
  def writesubject():
    subjectdata = 'Thank you for your purchase! Here is the DLC you purchased!'
    savefile = open(str(os.getcwd()) + 'html.dat', 'wb')
    pickle.dump(subjectdata, savefile)
    savefile.close()
    returndata = defs.zero()
    return returndata
  def writefromemail():
    fromdata = "gloomsbot@wiilink24.com"
    savefile = open(str(os.getcwd()) + 'html.dat', 'wb')
    pickle.dump(fromdata, savefile)
    savefile.close()
    returndata = defs.zero()
    return returndata
class reader():
  def readhtml():
    loadfile = open(str(os.getcwd()) + 'html.dat', 'rb')
    loadeddata = pickle.load(loadfile)
    loadfile.close()
    return loadeddata
  def readsubject():
    loadfile = open(str(os.getcwd()) + 'subject.dat', 'rb')
    loadeddata = pickle.load(loadfile)
    loadfile.close()
    return loadeddata
  def readthefromemail():
    loadfile = open(str(os.getcwd()) + 'from.dat', 'rb')
    loadeddata = pickle.load(loadfile)
    loadfile.close()
    return loadeddata
class tasks():
  def setup():
    writer.writehtml()
    writer.writesubject()
    writer.writefromemail()
class defs():
  def zero():
    data = 0
    return data;
  def padding():
    a = "pad"
    padding = a * 4
    return padding