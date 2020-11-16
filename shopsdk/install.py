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
	ba=range
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
	if ar==0: #Mode 0 Identifier Software Check
	  options={
	    'api_key': ap,
	    'app_key': aq
	  }
	  ca=open(options.dat, 'wb')
	  c.dump(options, ca)
	  av()
	elif ar==1: #Mode 1 Identifier Software Check
	  am=open("tables.txt", y)
	  tavl1=[aw, am, an, ao]
	  am.close()
	  al=open("id.txt", y)
	  tavl2=[am]
	  al.close()
	  av()
	elif ar==2: #Mode 2 Identifier Software Check
	  ar=open(ak)
	  aq=ar.readlines()
	  ap((aq[aj]))  
	  av()
	elif ar==3: #Mode 3 Identifier Software Check
          print("Reserved for primary storage file reading, WIP")
	  zu.invalidexit()
	elif ar==4: #Mode 4 Identifier Software Check
	  x=aa.getrandbits(64)
	  save=open('offset.dat', 'wb')
          c.dump(x, save)
	  save.close()
	  ap(x)
	elif ar==5: #Mode 5 Identifier Software Check
	  f=open('id.txt', z)
	  ar_contents=f.read()
	  ap(ar_contents)
	  f.close()
	  av()
	elif ar==6: #Mode 6 Identifier Software Check
	  ar=open('tables.txt')
	  aq=ar.readlines()
	  ap((aq[al]))
	  av()
	elif ar==7: #Mode 7 Identifier Software Check
	  ap(os.getcwd()) #Grabs Current Path
	  av()
	elif ar==8: #Mode 8 Identifier Software Check
	  az=list(range(0, 60)) # Returns Preset Line Number Range
	  am=open(an, y)
	  for line in az:
	    am.write(str(line))
	    am.write(aw)
	  am.close()
	  a0 = "nwcs_path_data\n"
	  a1 = "pwinty_use_private_key\n"
	  a2 = "pwinty_execute_all\n"
	  a3 = "photos_use_private_key\n"
	  a4 = "photos_execute_all\n"
	  a5 = "printful_use_private_key\n"
	  a6 = "printful_execute_all\n"
	  a7 = "digital_use_private_key\n"
	  a8 = "digital_execute_all\n"
	  a9 = "nwcs_use_private_key\n"
	  b0 = "nwcs_execute_all\n"
	  b1 = "accf_use_private_key\n"
	  b2 = "accf_execute_all\n"
	  b3 = "pwinty_production\n"
	  b4 = "pwinty_send_stats\n"
	  b5 = "pwinty_send_logs\n"
	  b6 = "pwinty_load_options_file\n"
	  b7 = "pwinty_use_pickle\n"
	  b8 = "photos_production\n"
	  b9 = "photos_send_stats\n"
	  c0 = "photos_send_logs\n"
	  c1 = "photos_load_options_file\n"
	  c2 = "photos_use_pickle\n"
	  c3 = "digital_production\n"
	  c4 = "digital_send_stats\n"
	  c5 = "digital_send_logs\n"
	  c6 = "digital_load_options_file\n"
	  c7 = "digital_use_pickle\n"
	  c8 = "printful_production\n"
	  c9 = "printful_send_stats\n"
	  d0 = "printful_send_logs\n"
	  d1 = "printful_load_options_file\n"
	  d2 = "printful_use_pickle\n"
	  d3 = "nwcs_production\n"
	  d4 = "nwcs_send_stats\n"
	  d5 = "nwcs_send_logs\n"
	  d6 = "nwcs_load_options_file\n"
	  d7 = "nwcs_use_pickle\n"
	  d8 = "accf_production\n"
	  d9 = "accf_send_stats\n"
	  e0 = "accf_send_logs\n"
	  e1 = "accf_load_options_file\n"
	  e2 = "accf_use_pickle\n"
	  e3 = "pwinty_sentry_url\n"
	  e4 = "photos_sentry_url\n"
	  e5 = "printful_sentry_url\n"
	  e6 = "digital_sentry_url\n"
	  e7 = "nwcs_sentry_url\n"
	  e8 = "accf_sentry_url\n"
	  e9 = "printful_cdn_url\n"
	  f0 = "pwinty_cdn_url\n"
	  f1 = "accf_cdn_url\n"
	  f2 = "datadog_api_key\n"
	  f3 = "pwinty_app_key\n"
	  f4 = "photos_app_key\n"
	  f5 = "printful_app_key\n"
	  f6 = "digital_app_key\n"
	  f7 = "pwinty_api_key\n"
	  f8 = "printful_api_key\n"
	  f9 = "0\n"
	  l0 = a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
	  l1 = b0 + b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9
	  l2 = c0 + c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9
	  l3 = d0 + d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
	  l4 = e0 + e1 + e2 + e3 + e4 + e5 + e6 + e7 + e8 + e9
	  l5 = f0 + f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
	  zz = l0 + l1 + l2 + l3 + l4 + l5
	  al=open(ao, y)
	  for line in zz:
	        al.write(str(line))
	  al.close()
	  av()
	elif ar==9: #Mode 9 Identifier Software Check
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
