import sys as a
import pathlib as af
import pickle as c
import random as as aa
import io as e
import os as ac
import binascii as g
import collections as h
import json as p
import utilsnotbyme as ad
def run(ai, aj, ak, al, am, an, ao, ap, aq, ar):
	ag=int
	ap=print
	au=list
	ba=range
	j=ad.u8
	l=ad.u32
	m=ad.pad
	n=ad.setup_log
	o=ad.log
	q=ad.u16
	path=af.Path(__file__).parent.absolute()
	with open("./config.json", "rb") as f:
	    r=p.load(f)
	if r["production"] and r["send_logs"]:
	    n(r["sentry_url"], False)
	if r["production"]:
	  dirdd=r["bcdata"]
	  f.mkdir(dirdd)
	ar=ag(ai) #Converts the mode specification Data to a integer
	w="Congrats, you accessed the secret feature!" #This script can also function as a My Aquarium DLC randomizer. You will see the message when you access that mode.
	u="Exit code 127 Occured" #Error code 127 message, this is usually called if args aren't specified correctly and/or if args aren't even there.
	at="Error code 1 Occured." #Error code 1 message, this is a generic error for all other errors.
	au="Error Code 1 Occured" #This error typically happens when the exit code fails, however it is currently unknown what would make that happen.
	av=a.exit
	aw="/n" #New line Opcode
	y="w" #Tav Writing Opcode
	z='r' #Generic Tavar Opcode
	if ar==0: #Mode 0 Identifier Software Check
	  options={
	    'api_key': ap,
	    'app_key': aq
	  }
	  ca=open(options.dat, 'wb')
	  c.dump(options, ca)
	  av(0)
	elif ar==1: #Mode 1 Identifier Software Check
	  am=open("tables.txt", y)
	  tavl1=[aw, am, an, ao]
	  am.close()
	  al=open("id.txt", y)
	  tavl2=[am]
	  al.close()
	  av(0)
	elif ar==2: #Mode 2 Identifier Software Check
	  ar=open(ak)
	  aq=ar.readlines()
	  ap((aq[aj]))  
	  av(0)
	elif ar==3: #Mode 3 Identifier Software Check
	  un=ac.system
	  un('echo Current Path: $PWD')
	  un('viale=$(python3 password.py)')
	  un('useradd -m -p $arg store')
	  un('echo Created user with $arg password')
	  un('cp -r -a $PWD/home/store. /home/store')
	  un('echo Install done.')
	  av(0)
	elif ar==4: #Mode 4 Identifier Software Check
	  ap("The more bits, the more secure it is!")
	  ap("Availale bit sizes: 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192")
	  w=eval(input("Enter the bitsize you want:"))
	  x=d.getrandbits(w)
	  ap(x)
	  av(0)
	elif ar==5: #Mode 5 Identifier Software Check
	  f=open('id.txt', z)
	  ar_contents=f.read()
	  ap(ar_contents)
	  f.close()
	  av(0)
	elif ar==6: #Mode 6 Identifier Software Check
	  ar=open('tables.txt')
	  aq=ar.readlines()
	  ap((aq[al]))
	  av(0)
	elif ar==7: #Mode 7 Identifier Software Check
	  ap(path) #aps Current Path
	  av(0)
	elif ar==8: #Mode 8 Identifier Software Check
	  an=au(range(2, 100)) # Returns Preset Line Number Range
	  ao=au(an) #Outputs the Preset Line Number Range to a list
	  am=open(an, y)
	  for line in ao:
	    am.write(line)
	    am.write(aw)
	  am.close()
	  a0="sentry_url"
	  a1="apful_key"
	  a2="production"
	  a3="send_stats"
	  a4="datadog_api_key"
	  a5="datadog_app_key"
	  a6="phparname"
	  a7="php_logger_path"
	  a8="php_logger_method"
	  a9="send_php_logs"
	  b0="api_key"
	  b1="orders"
	  b2="app_key"
	  b3="offset"
	  b4="limit"
	  b5="code"
	  b6="result"
	  b7="https://api.theapful.com/"
	  b8="apful API Python Library 1.2"
	  b9="Authorization"
	  c0="User-Agent"
	  c1="Content-Type"
	  c2="application/json"
	  c3="paging"
	  c4="total"
	  c5="VERBOSE"
	  c6="INFO"
	  c7="WARNING"
	  c8="CRITICAL"
	  d6="./readtables.sh"
	  e2="utf-8"
	  e3="https://api.theapful.com/"
	  e4="apful API Python Library 1.0"
	  e5="User-Agent"
	  e6="Content-Type"
	  e7="application/json"
	  e8="Server"
	  e9="avs"
	  f0="auth"
	  f2="/"
	  f3="fixtures"
	  f5=au(ba(0, 1))
	  f7="API response was not valid JSON."
	  f8="GET"
	  f9="POST"
	  g0="PUT"
	  g1="DELETE"
	  g2="API response did not contain paginated results."
	  g3=">B"
	  g4=">H"
	  g5=">I"
	  g6="<I"
	  g7=">b"
	  g8=">h"
	  g9=">i"
	  h0="0"
	  h1="255"
	  h3="65535"
	  h5="4294967295"
	  h7="4294967295"
	  h8="-128"
	  h9="127"
	  i0="-32768"
	  i1="32767"
	  i2="-2147483648"
	  i3="2147483647"
	  i4=au(ba(1, 2))
	  j0="200"
	  j1="301"
	  j2="ascii"
	  j3="256"
	  j4="128"
	  j5="512"
	  j6=au(ba(3, 4))
	  l0=[a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
	  l1=[b0, b1, b2, b3, b4, b5, b6, b7, b8, b9]
	  l2=[c0, c1, c2, c3, c4, c5, c6, c7, c8, c6]
	  l3=[c9, c9, c9, c9, c9, c9, d6, d6, d6, c3]
	  l4=[d9, c4, e2, e3, e4, e5, e6, e7, e8, e9]
	  l5=[f0, e9, g2, f3, e2, f5, f7, f8, f9, g0]
	  l6=[g1, g2, g3, g4, g5, g6, g7, g8, g9, h0]
	  l7=[h1, h0, h3, h0, h5, h0, h7, h8, h9, i0]
	  l8=[i1, i2, i3, i4, i4, i4, j0, j1, j2, j3] 
	  l9=[l0, l1, l2, l3, l4, l5, l6, l7, l8, j4, j5, j6, j7]
	  al=open(ao, y)
	  for line in l9:
	    al.write(line)
	    al.write(aw)
	  al.close()
	  av(0)
	elif ar==9: #Mode 9 Identifier Software Check
	  ap(w)
	  ap("My Aquarium Custom Attachment Generator\n")
	  ap("By John Pansera / Version 1.0\n")
	  ap("Randomization Mod by 6100m, porting concepts by TMinusBlastedRocket, zero casting work of butch@stackoverflow\n")
	  ab=aa.randint
	  cb=ab(0, 2) #My Aquarium Tank Size Offset
	  cd=ab(0, 5) #My Aquarium Glass Size Offset
	  ce=ab(0, 4) #My Aquarium Floor Type Offset
	  cf=ab(0, 4) #My Aquarium Background Type Offset
	  cg=ab(0, 6) #My Aquarium Light Type Offset
	  ch=ab(1, 12) #My Aquarium Special Date 1 Month Offset
	  ci=ab(1, 31) #My Aquarium Special Date 1 Day Offset
	  cj=ab(1, 12) #My Aquarium Special Date 2 Month Offset
	  ck=ab(1, 31) #My Aquarium Special Date 2 Day Offset
	  cl=ab(1, 12) #My Aquarium Special Date 3 Month Offset
	  cm=ab(1, 31) #My Aquarium Special Date 3 Day Offset
	  cn=ab(1, 101) #My Aquarium Add Fish Decisional Offset
	  co=ab(1, 15) #My Aquarium Maximum Fish Offset
	  ay=ag(cn) #Obsufcates variable to be shorter via aliasing
	  az=ag(co) #Converts the My Aquarium Maximum Fish Offset to a ageger
	  bb=au(ab(1, 40))
	  av=h.OrderedDict()
	  av["unknown"]=j(0)  # Version?
	  av["cb"]=j(ag(cb))
	  av["cd"]=j(ag(cd))
	  av["ce"]=j(ag(ce))
	  av["cf"]=j(ag(cf))
	  av["cg"]=j(ag(cg))
	  av["cq"]=q(0)
	  av["cr"]=l(0)
	  av["cs"]=l(0)
	  av["ct"]=j(0)
	  av["cu"]=j(ag(ch))
	  av["cv"]=j(ag(ci))
	  av["ct_1"]=j(0)
	  av["cw"]=j(0)
	  av["cx"]=j(ag(cj))
	  av["cy"]=j(ag(ck))
	  av["cw_2"]=j(0)
	  av["cz"]=j(0)
	  av["da"]=j(ag(cl))
	  av["dc"]=j(ag(cm))
	  av["cz_1"]=j(0)
	  data=utilsnotbyme.check(ay)
	  if data=="even":
	    if az <= 15:
	        for i in range(az):
	            sel=rn.choice(bb)
	            if sel < 40:
	                av["dd_%s" % i]=j(1)
	                av["de_%s" % i]=j(sel)
	                av["df_%s" % i]=q(0)
	                av["dg_%s" % i]=q(0)
	                av["dh_%s" % i]=q(1)
	                av["di_%s" % i]=l(1)  # Birthday is day 1
	                av["dj_%s" % i]=l(1)  # Current day set to 1
	                av["dk"]=m(240 - (az * 16))
	                av["dl"]=m(160)  # TODO: Add in object tables
	                ap("Processing ...")
	                f=e.BytesIO()
	                for k, v in au(av.items()): f.write(v)
	                f.flush()
	                f.seek(0)
	                copy=f.read()
	                crc32=format(g.crc32(copy) & 0xFFFFFFFF, '08x')
	                f.close()
	                ar=open('a0014682.dat', 'wb')  # Not sure how the name is generated yet
	                ar.write(g.unhexlify('08051400'))  # Magic Value
	                ar.write(g.unhexlify(crc32))  # CRC32
	                ar.write(copy)  # Rest of ar
	                ar.flush()
	                ar.close()
	                bb="a0014682.dat"
	                bc=r["nwcs_path_data"]
	                bd=str(path) + "/" + str(bb)
	                ac.rename(bd, bc)
	                ap(aw)
	                ap("Completed Successfully")
	                av(0)
	            else:
	                raise Exception("Error Code 1 Occured.")
	                o("Error: Invalid selection: %s" % at, "WARNING")
	    else:
	        raise Exception("Error Code 1 Occured.")
	        o("Error: Invalid amount, skipping: %s" % at, "WARNING")
	        az=0
	  else:
	    ap("Not doing fish....")
	    av["dk"]=m(240 - (az * 16))
	    av["dl"]=m(160) 
	    # TODO: Add in object tables
	    ap("Processing ...")
	    f=e.BytesIO()
	    for k, v in au(av.items()): f.write(v)
	    f.flush()
	    f.seek(0)
	    copy=f.read()
	    crc32=format(g.crc32(copy) & 0xFFFFFFFF, '08x')
	    f.close()
	    ar=open('a0014682.dat', 'wb')
	    # Not sure how the name is generated yet
	    ar.write(g.unhexlify('08051400'))  # Magic Value
	    ar.write(g.unhexlify(crc32))  # CRC32
	    ar.write(copy)  # Rest of ar
	    ar.flush()
	    ar.close()
	    bb="a0014682.dat"
	    bc=r["nwcs_path_data"]
	    bd=str(path) + "/" + str(bb)
	    ac.rename(bd, bc)
	    ap(aw)
	    ap("Completed Successfully")
	    av(0)
	else:
	  raise Exception("Exit code 127 Occured.")
	  o("You did not specify args: %s" % u, "WARNING")
	  av(127)
	raise Exception("Unknown Error Occured")
	o("Unknown Error Occured: %s" % au, "WARNING")
	av(1)
