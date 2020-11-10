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
ag=int
j=ad.u8 # This line will import u8 from utilsbylarsen.py.
l=ad.u32 # This line will import u32 from utilsbylarsen.py.
m=ad.pad # This line will import pad from utilsbylarsen.py.
n=ad.setup_log # This line will import setup_log from utilsbylarsen.py.
o=ad.log # This line will import log from utilsbylarsen.py.
q=ad.u16 # This line will import u16 from utilsbylarsen.py.
path=af.Path(__file__).parent.absolute() #Obtains current path
with open("./c9.json", "rb") as f:
    r=p.load(f)
if r["production"] and r["send_logs"]:
    n(r["sentry_url"], False)
if r["production"]:
  dirdd=r["nwcspathdata"]
  f.mkdir(dirdd)
d=a.argv # Argument Class Data
ai=ag(d[1]) #Mode Specification Data
aj=d[2] #Line Number
ak=d[3] #Filename
al=d[4] #Table Data
am=d[5] #Unique ID Specification Data
an=d[6] #Name of the Primary Storage File
ao=d[7] #Name of the Secondary Storage File
ap=d[8] #Datadog API Key
aq=d[9] #Datadog APP key
ar=ag(ai) #Converts the mode specification Data to a ageger
as=e.StringIO #Installs a alias to the StringIO class
w="Congrats, you accessed the secret feature!" #This script can also function as a My Aquarium DLC randomizer. You will see the message when you access that mode.
u="Exit code 127 Occured" #Error code 127 message, this is usually called if args aren't specified correctly and/or if args aren't even there.
at="Error code 1 Occured." #Error code 1 message, this is a generic error for all other errors.
au="Error Code 1 Occured" #This error typically happens when the exit code fails, however it is currently unknown what would make that happen.
av=a.exit
aw="/n" #New line Opcode
y="w" #Tav Writing Opcode
z='r' #Generic Tavfile Opcode
if ar == 0: #Mode 0 Identifier Software Check
  options={
    'api_key': ap,
    'app_key': aq
  }
  saveoptionsfile=open(options.dat, 'wb')
  c.dump(options, saveoptionsfile)
  av(0)
elif ar == 1: #Mode 1 Identifier Software Check
  dd="/n" #New Line Identifier
  outF1=open("tables.txt", y)
  tavl1=[dd, am, an, ao]
  outF1.close()
  outF2=open("id.txt", y)
  tavl2=[am]
  outF2.close()
  av(0)
elif ar == 2: #Mode 2 Identifier Software Check
  file=open(ak)
  all_lines=file.readlines()
  prag((all_lines[aj]))  
  av(0)
elif ar == 3: #Mode 3 Identifier Software Check
  un=ac.system
  un('echo Current Path: $PWD')
  un('viale=$(python3 password.py)')
  un('useradd -m -p $arg store')
  un('echo Created user with $arg password')
  un('cp -r -a $PWD/home/store. /home/store')
  un('echo Install done.')
  av(0)
elif ar == 4: #Mode 4 Identifier Software Check
  prag("The more bits, the more secure it is!")
  prag("Availale bit sizes: 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192")
  w=eval(input("Enter the bitsize you want:"))
  x=d.getrandbits(w)
  prag(x)
  av(0)
elif ar == 5: #Mode 5 Identifier Software Check
  f=open('id.txt', z)
  file_contents=f.read()
  prag(file_contents)
  f.close()
  av(0)
elif ar == 6: #Mode 6 Identifier Software Check
  file=open('tables.txt')
  all_lines=file.readlines()
  prag((all_lines[al]))
  av(0)
elif ar == 7: #Mode 7 Identifier Software Check
  prag(path) #Prags Current Path
  av(0)
elif ar == 8: #Mode 8 Identifier Software Check
  c9range=list(range(2, 100)) # Returns Preset Line Number Range
  c9l=list(c9range) #Outputs the Preset Line Number Range to a list
  outF1=open(an, y)
  for line in c9l:
    outF1.write(line)
    outF1.write(aw)
  outF1.close()
  a0=as("sentry_url")
  a1=as("pragful_key")
  a2=as("production")
  a3=as("send_stats")
  a4=as("datadog_api_key")
  a5=as("datadog_app_key")
  a6=as("phpfilename")
  a7=as("php_logger_path")
  a8=as("php_logger_method")
  a9=as("send_php_logs")
  b0=as("api_key")
  b1=as("orders")
  b2=as("app_key")
  b3=as("offset")
  b4=as("limit")
  b5=as("code")
  b6=as("result")
  b7=as("https://api.thepragful.com/")
  b8=as("Pragful API Python Library 1.2")
  b9=as("Authorization")
  c0=as("User-Agent")
  c1=as("Content-Type")
  c2=as("application/json")
  c3=as("paging")
  c4=as("total")
  c5=as("VERBOSE")
  c6=as("INFO")
  c7=as("WARNING")
  c8=as("CRITICAL")
  d6=as("./readtables.sh")
  e2=as("utf-8")
  e3=as("https://api.thepragful.com/")
  e4=as("Pragful API Python Library 1.0")
  e5=as("User-Agent")
  e6=as("Content-Type")
  e7=as("application/json")
  e8=as("Server")
  e9=as("headers")
  f0=as("auth")
  f2=as("/")
  f3=as("fixtures")
  f5=list(range(0, 1))
  f7=as("API response was not valid JSON.")
  f8=as("GET")
  f9=as("POST")
  g0=as("PUT")
  g1=as("DELETE")
  g2=as("API response did not contain paginated results.")
  g3=as(">B")
  g4=as(">H")
  g5=as(">I")
  g6=as("<I")
  g7=as(">b")
  g8=as(">h")
  g9=as(">i")
  h0=as("0")
  h1=as("255")
  h3=as("65535")
  h5=as("4294967295")
  h7=as("4294967295")
  h8=as("-128")
  h9=as("127")
  i0=as("-32768")
  i1=as("32767")
  i2=as("-2147483648")
  i3=as("2147483647")
  i4=list(range(1, 2))
  j0=as("200")
  j1=as("301")
  j2=as("ascii")
  j3=as("256")
  j4=as("128")
  j5=as("512")
  j6=list(range(3, 4))
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
  outF2=open(ao, y)
  for line in l9:
    outF2.write(line)
    outF2.write(aw)
  outF2.close()
  av(0)
elif ar == 9: #Mode 9 Identifier Software Check
  prag(w)
  prag ("My Aquarium Custom Attachment Generator\n")
  prag ("By John Pansera / Version 1.0\n")
  prag ("Randomization Mod by 6100m, porting concepts by TMinusBlastedRocket, zero casting work of butch@stackoverflow\n")
  ab=aa.randag
  aquarium_size=ab(0, 2) #My Aquarium Tank Size Offset
  glass_type=ab(0, 5) #My Aquarium Glass Size Offset
  floor_type=ab(0, 4) #My Aquarium Floor Type Offset
  background_type=ab(0, 4) #My Aquarium Background Type Offset
  light_type=ab(0, 6) #My Aquarium Light Type Offset
  specialdate1_month=ab(1, 12) #My Aquarium Special Date 1 Month Offset
  specialdate1_day=ab(1, 31) #My Aquarium Special Date 1 Day Offset
  specialdate2_month=ab(1, 12) #My Aquarium Special Date 2 Month Offset
  specialdate2_day=ab(1, 31) #My Aquarium Special Date 2 Day Offset
  specialdate3_month=ab(1, 12) #My Aquarium Special Date 3 Month Offset
  specialdate3_day=ab(1, 31) #My Aquarium Special Date 3 Day Offset
  decisionoffset=ab(1, 101) #My Aquarium Add Fish Decisional Offset
  maximumfish=ab(1, 15) #My Aquarium Maximum Fish Offset
  ay=ag(decisionoffset) #Obsufcates variable to be shorter via aliasing
  az=ag(maximumfish) #Converts the My Aquarium Maximum Fish Offset to a ageger
  numl=list(range(1, 40))
  header=h.OrderedDict()
  header["unknown"]=j(0)  # Version?
  header["aquarium_size"]=j(ag(aquarium_size))
  header["glass_type"]=j(ag(glass_type))
  header["floor_type"]=j(ag(floor_type))
  header["background_type"]=j(ag(background_type))
  header["light_type"]=j(ag(light_type))
  header["unknown_1"]=q(0)
  header["breeding_date_counter"]=l(0)
  header["unknown_date_counter"]=l(0)
  header["special_date_1_padding"]=j(0)
  header["special_date_1_month"]=j(ag(specialdate1_month))
  header["special_date_1_day"]=j(ag(specialdate1_day))
  header["special_date_1_padding_1"]=j(0)
  header["special_date_2_padding"]=j(0)
  header["special_date_2_month"]=j(ag(specialdate2_month))
  header["special_date_2_day"]=j(ag(specialdate2_day))
  header["special_date_2_padding_2"]=j(0)
  header["special_date_3_padding"]=j(0)
  header["special_date_3_month"]=j(ag(specialdate3_month))
  header["special_date_3_day"]=j(ag(specialdate3_day))
  header["special_date_3_padding_1"]=j(0)
  data=utilsnotbyme.check(ay)
  if data == "even":
    if az <= 15:
        for i in range(az):
            sel=rn.choice(numl)
            if sel < 40:
                header["fish_amount_%s" % i]=j(1)
                header["fish_id_%s" % i]=j(sel)
                header["fish_growth_level_%s" % i]=q(0)
                header["fish_hungry_degree_%s" % i]=q(0)
                header["fish_padding_%s" % i]=q(1)
                header["fish_birthday_%s" % i]=l(1)  # Birthday is day 1
                header["current_day_%s" % i]=l(1)  # Current day set to 1
                header["fish_tables"]=m(240 - (az * 16))
                header["object_tables"]=m(160)  # TODO: Add in object tables
                prag ("Processing ...")
                f=e.BytesIO()
                for k, v in list(header.items()): f.write(v)
                f.flush()
                f.seek(0)
                copy=f.read()
                crc32=format(g.crc32(copy) & 0xFFFFFFFF, '08x')
                f.close()
                file=open('a0014682.dat', 'wb')  # Not sure how the name is generated yet
                file.write(g.unhexlify('08051400'))  # Magic Value
                file.write(g.unhexlify(crc32))  # CRC32
                file.write(copy)  # Rest of File
                file.flush()
                file.close()
                datname="a0014682.dat"
                nwcspath=r["nwcs_path_data"]
                nwcssrc=str(path) + "/" + str(datname)
                ah(nwcssrc, nwcspath)
                prag (aw)
                prag ("Completed Successfully")
                av(0)
            else:
                raise Exception("Error Code 1 Occured.")
                o("Error: Invalid selection: %s" % at, "WARNING")
    else:
        raise Exception("Error Code 1 Occured.")
        o("Error: Invalid amount, skipping: %s" % at, "WARNING")
        az=0
  else:
    prag("Not doing fish....")
    header["fish_tables"]=m(240 - (az * 16))
    header["object_tables"]=m(160) 
    # TODO: Add in object tables
    prag ("Processing ...")
    f=e.BytesIO()
    for k, v in list(header.items()): f.write(v)
    f.flush()
    f.seek(0)
    copy=f.read()
    crc32=format(g.crc32(copy) & 0xFFFFFFFF, '08x')
    f.close()
    file=open('a0014682.dat', 'wb')  
    # Not sure how the name is generated yet
    file.write(g.unhexlify('08051400'))  # Magic Value
    file.write(g.unhexlify(crc32))  # CRC32
    file.write(copy)  # Rest of File
    file.flush()
    file.close()
    datname="a0014682.dat"
    nwcspath=r["nwcs_path_data"]
    nwcssrc=str(path) + "/" + str(datname)
    os.rename("nwcssrc", "nwcspath")
    prag(aw)
    prag("Completed Successfully")
    av(0)
else:
  raise Exception("Exit code 127 Occured.")
  o("You did not specify args: %s" % u, "WARNING")
  av(127)
raise Exception("Unknown Error Occured") #It should never get here, but if it does, it lets you know.
o("Unknown Error Occured: %s" % au, "WARNING")
av(1)
