import sys as a
import pathlib as af
import pickle as c
import random as as aa
import io as e
import os as ac
import binascii as g
import collections as h
import utilsbylarsen as ad
import json as p
import shutil as ae #Imports the base class of shutil
import utilsnotbyme
ag=int
ah=ae.copyfile #Selectively imports copyfile from the base class of shutil.
j=ad.u8 # This line will import u8 from utilsbylarsen.py.
l=ad.u32 # This line will import u32 from utilsbylarsen.py.
m=ad.pad # This line will import pad from utilsbylarsen.py.
n=ad.setup_log # This line will import setup_log from utilsbylarsen.py.
o=ad.log # This line will import log from utilsbylarsen.py.
q=ad.u16 # This line will import u16 from utilsbylarsen.py.
path=af.Path(__file__).parent.absolute() #Obtains current path
with open("./config.json", "rb") as f:
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
ar=ag(ai) #Converts the mode specification Data to a integer
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
  print((all_lines[aj]))  
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
  print("The more bits, the more secure it is!")
  print("Availale bit sizes: 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192")
  w=eval(input("Enter the bitsize you want:"))
  x=d.getrandbits(w)
  print(x)
  av(0)
elif ar == 5: #Mode 5 Identifier Software Check
  f=open('id.txt', z)
  file_contents=f.read()
  print(file_contents)
  f.close()
  av(0)
elif ar == 6: #Mode 6 Identifier Software Check
  file=open('tables.txt')
  all_lines=file.readlines()
  print((all_lines[al]))
  av(0)
elif ar == 7: #Mode 7 Identifier Software Check
  print(path) #Prints Current Path
  av(0)
elif ar == 8: #Mode 8 Identifier Software Check
  configrange=list(range(2, 100)) # Returns Preset Line Number Range
  configl=list(configrange) #Outputs the Preset Line Number Range to a list
  outF1=open(an, y)
  for line in configl:
    outF1.write(line)
    outF1.write(aw)
  outF1.close()
  v00=as("sentry_url")
  v01=as("printful_key")
  v02=as("production")
  v03=as("send_stats")
  v04=as("datadog_api_key")
  v05=as("datadog_app_key")
  v06=as("phpfilename")
  v07=as("php_logger_path")
  v08=as("php_logger_method")
  v09=as("send_php_logs")
  v10=as("api_key")
  v11=as("orders")
  v12=as("app_key")
  v13=as("offset")
  v14=as("limit")
  v15=as("code")
  v16=as("result")
  v17=as("https://api.theprintful.com/")
  v18=as("Printful API Python Library 1.2")
  v19=as("Authorization")
  v20=as("User-Agent")
  v21=as("Content-Type")
  v22=as("application/json")
  v23=as("paging")
  v24=as("total")
  v25=as("VERBOSE")
  v26=as("INFO")
  v27=as("WARNING")
  v28=as("CRITICAL")
  v36=as("./readtables.sh")
  v42=as("utf-8")
  v43=as("https://api.theprintful.com/")
  v44=as("Printful API Python Library 1.0")
  v45=as("User-Agent")
  v46=as("Content-Type")
  v47=as("application/json")
  v48=as("Server")
  v49=as("headers")
  v50=as("auth")
  v52=as("/")
  v53=as("fixtures")
  v55=list(range(0, 1))
  v57=as("API response was not valid JSON.")
  v58=as("GET")
  v59=as("POST")
  v60=as("PUT")
  v61=as("DELETE")
  v62=as("API response did not contain paginated results.")
  v63=as(">B")
  v64=as(">H")
  v65=as(">I")
  v66=as("<I")
  v67=as(">b")
  v68=as(">h")
  v69=as(">i")
  v70=as("0")
  v71=as("255")
  v73=as("65535")
  v75=as("4294967295")
  v77=as("4294967295")
  v78=as("-128")
  v79=as("127")
  v80=as("-32768")
  v81=as("32767")
  v82=as("-2147483648")
  v83=as("2147483647")
  v84=list(range(1, 2))
  v90=as("200")
  v91=as("301")
  v92=as("ascii")
  v93=as("256")
  v94=as("128")
  v95=as("512")
  v96=list(range(3, 4))
  l0=[v00, v01, v02, v03, v04, v05, v06, v07, v08, v09]
  l1=[v10, v11, v12, v13, v14, v15, v16, v17, v18, v19]
  l2=[v20, v21, v22, v23, v24, v25, v26, v27, v28, v26]
  l3=[v29, v29, v29, v29, v29, v29, v36, v36, v36, v23]
  l4=[v39, v24, v42, v43, v44, v45, v46, v47, v48, v49]
  l5=[v50, v49, v62, v53, v42, v55, v57, v58, v59, v60]
  l6=[v61, v62, v63, v64, v65, v66, v67, v68, v69, v70]
  l7=[v71, v70, v73, v70, v75, v70, v77, v78, v79, v80]
  l8=[v81, v82, v83, v84, v84, v84, v90, v91, v92, v93] 
  l9=[l0, l1, l2, l3, l4, l5, l6, l7, l8, v94, v95, v96, v97]
  outF2=open(ao, y)
  for line in l9:
    outF2.write(line)
    outF2.write(aw)
  outF2.close()
  av(0)
elif ar == 9: #Mode 9 Identifier Software Check
  print(w)
  print ("My Aquarium Custom Attachment Generator\n")
  print ("By John Pansera / Version 1.0\n")
  print ("Randomization Mod by 6100m, porting concepts by TMinusBlastedRocket, zero casting work of butch@stackoverflow\n")
  ab=aa.randint
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
  az=ag(maximumfish) #Converts the My Aquarium Maximum Fish Offset to a integer
  numl=list(range(1, 40))
  header=h.OrderedDict()
  header["unknown"]=j(0)  # Version?
  header["aquarium_size"]=j(int(aquarium_size))
  header["glass_type"]=j(int(glass_type))
  header["floor_type"]=j(int(floor_type))
  header["background_type"]=j(int(background_type))
  header["light_type"]=j(int(light_type))
  header["unknown_1"]=q(0)
  header["breeding_date_counter"]=l(0)
  header["unknown_date_counter"]=l(0)
  header["special_date_1_padding"]=j(0)
  header["special_date_1_month"]=j(int(specialdate1_month))
  header["special_date_1_day"]=j(int(specialdate1_day))
  header["special_date_1_padding_1"]=j(0)
  header["special_date_2_padding"]=j(0)
  header["special_date_2_month"]=j(int(specialdate2_month))
  header["special_date_2_day"]=j(int(specialdate2_day))
  header["special_date_2_padding_2"]=j(0)
  header["special_date_3_padding"]=j(0)
  header["special_date_3_month"]=j(int(specialdate3_month))
  header["special_date_3_day"]=j(int(specialdate3_day))
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
                print ("Processing ...")
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
                print (aw)
                print ("Completed Successfully")
                av(0)
            else:
                raise Exception("Error Code 1 Occured.")
                o("Error: Invalid selection: %s" % at, "WARNING")
    else:
        raise Exception("Error Code 1 Occured.")
        o("Error: Invalid amount, skipping: %s" % at, "WARNING")
        az=0
  else:
    print("Not doing fish....")
    header["fish_tables"]=m(240 - (az * 16))
    header["object_tables"]=m(160) 
    # TODO: Add in object tables
    print ("Processing ...")
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
    ah(nwcssrc, nwcspath)
    print (aw)
    print ("Completed Successfully")
    av(0)
else:
  raise Exception("Exit code 127 Occured.")
  o("You did not specify args: %s" % u, "WARNING")
  av(127)
raise Exception("Unknown Error Occured") #It should never get here, but if it does, it lets you know.
o("Unknown Error Occured: %s" % au, "WARNING")
av(1)
