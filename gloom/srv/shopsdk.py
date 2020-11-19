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
class sdk():
  def send(thetoemail, filetosend, currentnoofpoints, pointsneeded, contenttype):
    with open(str(os.getcwd()) + "/" + "./config.json", "rb") as f:
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
    savefile = open(str(os.getcwd()) + "/" + 'html.dat', 'wb')
    pickle.dump(htmldata, savefile)
    savefile.close()
    returndata = defs.zero()
    return returndata
  def writesubject():
    subjectdata = 'Thank you for your purchase! Here is the DLC you purchased!'
    savefile = open(str(os.getcwd()) + "/" + 'html.dat', 'wb')
    pickle.dump(subjectdata, savefile)
    savefile.close()
    returndata = defs.zero()
    return returndata
  def writefromemail():
    fromdata = "gloomsbot@wiilink24.com"
    savefile = open(str(os.getcwd()) + "/" + 'html.dat', 'wb')
    pickle.dump(fromdata, savefile)
    savefile.close()
    returndata = defs.zero()
    return returndata
class reader():
  def readhtml():
    loadfile = open(str(os.getcwd()) + "/" + 'html.dat', 'rb')
    loadeddata = pickle.load(loadfile)
    loadfile.close()
    return loadeddata
  def readsubject():
    loadfile = open(str(os.getcwd()) + "/" + 'subject.dat', 'rb')
    loadeddata = pickle.load(loadfile)
    loadfile.close()
    return loadeddata
  def readthefromemail():
    loadfile = open(str(os.getcwd()) + "/" + 'from.dat', 'rb')
    loadeddata = pickle.load(loadfile)
    loadfile.close()
    return loadeddata
class tasks():
  def setup():
    writer.writehtml()
    writer.writesubject()
    writer.writefromemail()
    tasks.check()
    returndata = defs.msg()
    return returndata
  def check(): 
    #All these dat files contain hardcoded data, hence why I didn't put them in the config, so to say.
    if os.path.exists(str(os.getcwd()) + "/" + "html.dat"):
      print("CHECKSUM #0 OK")
    if os.path.exists(str(os.getcwd()) + "/" + "subject.dat"):
      print("CHECKSUM #1 OK")
    if os.path.exists(str(os.getcwd()) + "/" + "from.dat"):
      print("CHECKSUM #2 OK")
    returndata = defs.padding()
    return returndata
class defs():
  def zero():
    data = 0
    return data;
  def padding():
    a = "pad"
    padding = a * 24 #Casual homage to WL24/WC24/RC24
    #You can use this to identify where the returned data seperates
    return padding
  def msg():
    msg = "DONE"
    padding = defs.padding()
    msg2 = msg + padding
    msg3 = str(msg2)
    return msg3
