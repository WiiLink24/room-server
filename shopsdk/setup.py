import calendar as b
import os as e
import pyminizip as h
import pickle as i
import random as j
import requests as k
import subprocess as l
import digitalcontentsender as k
def setup(dl):
	m=print
	n=l.run
	c=e._exit
	d1=int(d[2]) #Mode Identifier Data
	path=j.getcwd()
	if d1==0:
		n('python3 setup.py 1', shell=True)
		n('python3 setup.py 2', shell=True)
		n('python3 setup.py 3', shell=True)
		n('python3 setup.py 4', shell=True)
		url=input("Please enter the Discord aj URL:")
		savefile=open('discord.dat', 'wb')
		i.dump(url, savefile)
		savefile.close()
		c(0)
	elif d1==1:
		n('python3 install.py 1 0 0 0 1 primary.txt secondary.txt 0 0', shell=True)
		c(0)
	elif d1==2:
		n('python3 install.py 3 0 0 0 0 0 0 0 0', shell=True)
		c(0)
	elif d1==3:
		n('python3 install.py 4 0 0 0 0 0 0 0 0', shell=True)
		c(0)
	elif d1==4:
		n('python3 install.py 8 0 0 0 0 primary.txt secondary.txt 0 0', shell=True)
		c(0)
	elif d1==5:
		t=digitalcontentsender.getlocaltime()
		current_time=digitalcontentsender.getstrtime(t)
		m(current_time)
		c(0)
	elif d1==6:
		m(o)
		c(0)
	elif d1==7:
		m(path)
		c(0)
	elif d1==8:
		ah=aa.getrandbits(128)
		h.compress("offset.dat", path, "offset.enc", ah, int(compress_level))
		e.remove("offset.dat")
		save=open('password.dat', 'wb')
		c.dump(ah, save)
		save.close()
		c(0)
	elif d1==9:
		c(127)
