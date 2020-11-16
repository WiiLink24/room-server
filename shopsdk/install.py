import pickle as c
import random as aa
import io as e
import os
import binascii as g
import collections as h
import json as p
import utilsnotbyme as ad
import digitalcontentsender as zu
def run(ai, aj, ak, al, am, an, ao, ap, aq, ar):
	ag=int
	ap=print
	j=ad.u8
	l=ad.u32
	m=ad.pad
	n=ad.setup_log
	o=ad.log
	q=ad.u16
	with open("./config.json", "rb") as f:
	  r=p.load(f)
	if r["nwcs_production"] and r["nwcs_send_logs"]:
	  n(r["nwcs_sentry_url"], False)
	if r["nwcs_production"]:
	  dirdd=r["nwcs_path_data"]
	  os.mkdir(dirdd)
	ar=ag(ai) #Converts the mode specification Data to a integer
	w="Congrats, you accessed the secret feature!" #This script can also function as a My Aquarium DLC randomizer. You will see the message when you access that mode.
	u="Exit code 127 Occured" #Error code 127 message, this is usually called if args aren't specified correctly and/or if args aren't even there.
	at="Error code 1 Occured." #Error code 1 message, this is a generic error for all other errors.
	au="Error Code 1 Occured" #This error typically happens when the exit code fails, however it is currently unknown what would make that happen.
	av=zu.normalexit()
	aw="\n" #New line Opcode
	y="w" #Tav Writing Opcode
	z='r' #Generic File Writing Opcode
	if ar==0: #Mode 1 Identifier Software Check
	  options={
	    'api_key': ap,
	    'app_key': aq
	  }
	  ca=open(options.dat, 'wb')
	  c.dump(options, ca)
	  av()
	elif ar==9: #Mode 2 Identifier Software Check
	  ap(w)
	  ap("My Aquarium Custom Attachment Generator\n")
	  ap("By John Pansera / Version 1.0\n")
	  ap("Randomization Mod by 6100m, porting concepts by TMinusBlastedRocket\n")
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
	  az=ag(co) #Converts the My Aquarium Maximum Fish Offset to a integer
	  bb=list(range(1, 40))
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
	  data=ad.check(ay)
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
	          for k, v in list(av.items()):
                      f.write(ad.to_bytes(v))
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
	          bd=str(os.getcwd()) + "/" + str(bb)
	          os.rename(bd, bc)
	          ap(aw)
	          ap("Completed Successfully")
	          av()
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
	    for k, v in list(av.items()):
                f.write(ad.to_bytes(v))
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
	    bd=str(os.getcwd()) + "/" + str(bb)
	    os.rename(bd, bc)
	    ap(aw)
	    ap("Completed Successfully")
	    av()
	else:
	  raise Exception("Exit code 127 Occured.")
	  o("You did not specify args: %s" % u, "WARNING")
	  zu.invalidexit()
	raise Exception("Unknown Error Occured")
	o("Unknown Error Occured: %s" % au, "WARNING")
	zu.abnormalexit()
