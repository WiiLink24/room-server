import binascii as l
import logging
import os as j
import pyminizip as n
import pickle as m
import requests as g
import sentry_sdk as e
import struct as a
import time as r
import sys as s
import codecs as zz
from sentry_sdk.integrations.logging import LoggingIntegration
g.packages.urllib3.disable_warnings()  # This is so we don't get some warning about SSL.
h=False
k=True
z="batter.dat"
y='batter.dat'
production=h
p_errors=h
o=print
def setup_log(sentry_url,print_errors):
  global logger,production
  sentry_logging=LoggingIntegration(
    level=logging.INFO,
    event_level=logging.INFO
  )
  e.init(dsn=sentry_url,integrations=[sentry_logging])
  logger=logging.getLogger(__name__)
  p_errors=print_errors
  production=k
def log(msg,level):  
  # TODO: Use number levels instead of strings
  if p_errors:
    o(msg)
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
  if not 0<=b<=255:
    log("u8 out of range: %s" % b,"INFO")
    b=0
  return a.pack(">B",b)
def u16(b):
  if not 0<=b<=65535:
    log("u16 out of range: %s" % b,"INFO")
    b=0
  return a.pack(">H",b)
def u32(b):
  if not 0<=b<=4294967295:
    log("u32 out of range: %s" % b,"INFO")
    b=0
  return a.pack(">I",b)
def pad(c):
  d=""
  for _ in range(c): d+="\0"
  return d
def downloadtask(a,b):
	r=requests.get(b,allow_redirects=k)
	open(a,'wb').write(r.content)
	msg=returnmsg()
	return msg
def getcurrentpath():
	a=str(j.getcwd())
	return a
def compressmultiple(a,b,c,d):
	n.compress_multiple([a,b],d,c,4,progress)
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
def check(a):
        if (a % 2) == 0:
                print("{0} is Even".format(a))
        else:
                print("{0} is Odd".format(a))
def to_bytes(s):
        if type(s) is bytes:
                return s
        elif type(s) is str or (sys.version_info[0] < 3 and type(s) is unicode):
                return zz.encode(s, 'utf-8')
        else:
                raise TypeError("Expected bytes or string, but got %s." % type(s))
