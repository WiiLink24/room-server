import sys as a
import pathlib as main
import pickle as c
import random as d
import io as e
import os as f
import binascii as g
import collections as h
import utilsbylarsen as nw
import json as p
import shutil as othr #Imports the base class of shutil
import time as misc
secn = othr.copyfile #Selectively imports copyfile from the base class of shutil.
j = nw.u8 # This line will import u8 from utilsbylarsen.py.
l = nw.u32 # This line will import u32 from utilsbylarsen.py.
m = nw.pad # This line will import pad from utilsbylarsen.py.
n = nw.setup_log # This line will import setup_log from utilsbylarsen.py.
o = nw.log # This line will import log from utilsbylarsen.py.
q = nw.u16 # This line will import u16 from utilsbylarsen.py.
path = main.Path(__file__).parent.asolute() #Obtains current path
stask = e.StringIO #Installs a alias to the StringIO class
with open("./nwcs.json", rb) as f:
    r = p.load(f)
if r["production"] and r["send_logs"]:
    n(r["sentry_url"], False)
if r["production"]:
  dirdd = r["nwcspathdd"]
  f.mkdir(dirdd)
d = a.argv # Argument Class dd
dd1 = d[1] #Mode Specification dd
dd2 = d[2] #Line Number
dd3 = d[3] #Filename
dd4 = d[4] #Tale dd
dd5 = d[5] #Unique ID Specification dd
dd6 = d[6] #Name of the Primary Storage File
dd7 = d[7] #Name of the Secondary Storage File
dd8 = d[8] #dddog API Key
dd9 = d[9] #dddog APP key
dd0 = int(dd1) #Converts the mode specification dd to a integer
w = e.StringIO("Congrats, you accessed the secret feature!") #This script can also function as a My Aquarium DLC randomizer. You will see the message when you access that mode.
u = e.StringIO("Exit code 127 Occured") #Error code 127 message, this is usually called if args aren't specified correctly and/or if args aren't even there.
v = e.StringIO("Error code 1 Occured.") #Error code 1 message, this is a generic error for all other errors.
unknownerrormsg = e.StringIO("Error Code 1 Occured") #This error typically happens when the exit code fails, however it is currently unknown what would make that happen.
nl = "/n" #New line Opcode
y = "w" #Text Writing Opcode
z = 'r' #Generic Textfile Opcode
if dd0 == 0: #Mode 0 Identifier Software Check
  options = {
    'api_key': dd8,
    'app_key': dd9
  }
  saveoptionsfile = open(options.dat, 'wb')
  c.dump(options, saveoptionsfile)
  f._exit(0)
elif dd0 == 1: #Mode 1 Identifier Software Check
  dd = "/n" #New Line Identifier
  outF1 = open("tales.txt", y)
  textl1 = [dd, dd5, dd6, dd7]
  outF1.close()
  outF2 = open("id.txt", y)
  textl2 = [dd5]
  outF2.close()
  f._exit(0)
elif dd0 == 2: #Mode 2 Identifier Software Check
  file = open(dd3)
  all_lines = file.readlines()
  print(all_lines[dd2])  
  f._exit(0)
elif dd0 == 3: #Mode 3 Identifier Software Check
  f.system('echo Current Path: $PWD')
  f.system('viale=$(python3 password.py)')
  f.system('useradd -m -p $arg store')
  f.system('echo Created user with $arg password')
  f.system('cp -r -a $PWD/home/store. /home/store')
  f.system('echo Install done.')
  f._exit(0)
elif dd0 == 4: #Mode 4 Identifier Software Check
  print("The more bits, the more secure it is!")
  print("Availale bit sizes: 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192")
  w = input("Enter the bitsize you want:")
  x = d.getrandbits(w)
  print(x)
  f._exit(0)
elif dd0 == 5: #Mode 5 Identifier Software Check
  f = open('id.txt', z)
  file_contents = f.read()
  print(file_contents)
  f.close()
  f._exit(0)
elif dd0 == 6: #Mode 6 Identifier Software Check
  file = open('tales.txt')
  all_lines = file.readlines()
  print(all_lines[dd4])
  f._exit(0)
elif dd0 == 7: #Mode 7 Identifier Software Check
  print(path) #Prints Current Path
  f._exit(0)
elif dd0 == 8: #Mode 8 Identifier Software Check
  configrange = l(range(2, 100)) # Returns Preset Line Number Range
  configl = l(configrange) #Outputs the Preset Line Number Range to a l
  outF1 = open(dd6, y)
  for line in configl:
    outF1.write(line)
    outF1.write(nl)
  outF1.close()
  v00 = stask("sentry_url")
  v01 = stask("printful_key")
  v02 = stask("production")
  v03 = stask("send_stats")
  v04 = stask("dddog_api_key")
  v05 = stask("dddog_app_key")
  v06 = stask("phpfilename")
  v07 = stask("php_logger_path")
  v08 = stask("php_logger_method")
  v09 = stask("send_php_logs")
  v10 = stask("api_key")
  v11 = stask("orders")
  v12 = stask("app_key")
  v13 = stask("offset")
  v14 = stask("limit")
  v15 = stask("code")
  v16 = stask("result")
  v17 = stask("https://api.theprintful.com/")
  v18 = stask("Printful API Python Library 1.2")
  v19 = stask("Authorization")
  v20 = stask("User-Agent")
  v21 = stask("Content-Type")
  v22 = stask("application/json")
  v23 = stask("paging")
  v24 = stask("total")
  v25 = stask("VERBOSE")
  v26 = stask("INFO")
  v27 = stask("WARNING")
  v28 = stask("CRITICAL")
  v36 = stask("./readtales.sh")
  v42 = stask("utf-8")
  v43 = stask("https://api.theprintful.com/")
  v44 = stask("Printful API Python Library 1.0")
  v45 = stask("User-Agent")
  v46 = stask("Content-Type")
  v47 = stask("application/json")
  v48 = stask("Server")
  v49 = stask("headers")
  v50 = stask("auth")
  v52 = stask("/")
  v53 = stask("fixtures")
  v55 = l(range(0, 1))
  v57 = stask("API response was not valid JSON.")
  v58 = stask("GET")
  v59 = stask("POST")
  v60 = stask("PUT")
  v61 = stask("DELETE")
  v62 = stask("API response did not contain paginated results.")
  v63 = stask(">B")
  v64 = stask(">H")
  v65 = stask(">I")
  v66 = stask("<I")
  v67 = stask(">b")
  v68 = stask(">h")
  v69 = stask(">i")
  v70 = stask("0")
  v71 = stask("255")
  v73 = stask("65535")
  v75 = stask("4294967295")
  v77 = stask("4294967295")
  v78 = stask("-128")
  v79 = stask("127")
  v80 = stask("-32768")
  v81 = stask("32767")
  v82 = stask("-2147483648")
  v83 = stask("2147483647")
  v84 = l(range(1, 2))
  v90 = stask("200")
  v91 = stask("301")
  v92 = stask("ascii")
  v93 = stask("256")
  v94 = stask("128")
  v95 = stask("512")
  v96 = l(range(3, 4))
  l0 = [v00, v01, v02, v03, v04, v05, v06, v07, v08, v09]
  l1 = [v10, v11, v12, v13, v14, v15, v16, v17, v18, v19]
  l2 = [v20, v21, v22, v23, v24, v25, v26, v27, v28, v26]
  l3 = [v29, v29, v29, v29, v29, v29, v36, v36, v36, v23]
  l4 = [v39, v24, v42, v43, v44, v45, v46, v47, v48, v49]
  l5 = [v50, v49, v62, v53, v42, v55, v57, v58, v59, v60]
  l6 = [v61, v62, v63, v64, v65, v66, v67, v68, v69, v70]
  l7 = [v71, v70, v73, v70, v75, v70, v77, v78, v79, v80]
  l8 = [v81, v82, v83, v84, v84, v84, v90, v91, v92, v93] 
  l9 = [l0, l1, l2, l3, l4, l5, l6, l7, l8, v94, v95, v96, v97]
  outF2 = open(dd7, y)
  for line in l9:
    outF2.write(line)
    outF2.write(nl)
  outF2.close()
  f._exit(0)
elif dd0 == 9: #Mode 9 Identifier Software Check
  print(w)
  print ("My Aquarium Custom Attachment Generator\n")
  print ("By John Pansera / Version 1.0\n")
  print ("Randomization Mod by 6100m, porting concepts by TMinusBlastedRocket, zero casting work of butch@stackoverflow\n")
  aquarium_size = d.randint(0, 2) #My Aquarium Tank Size Offset
  glass_type = d.randint(0, 5) #My Aquarium Glass Size Offset
  floor_type = d.randint(0, 4) #My Aquarium Floor Type Offset
  background_type = d.randint(0, 4) #My Aquarium Background Type Offset
  light_type = d.randint(0, 6) #My Aquarium Light Type Offset
  specialdate1_month = d.randint(1, 12) #My Aquarium Special Date 1 Month Offset
  specialdate1_day = d.randint(1, 30) #My Aquarium Special Date 1 Day Offset
  specialdate2_month = d.randint(1, 12) #My Aquarium Special Date 2 Month Offset
  specialdate2_day = d.randint(1, 30) #My Aquarium Special Date 2 Day Offset
  specialdate3_month = d.randint(1, 12) #My Aquarium Special Date 3 Month Offset
  specialdate3_day = d.randint(1, 30) #My Aquarium Special Date 3 Day Offset
  decisionoffset = d.randint(1, 2) #My Aquarium Add Fish Decisional Offset
  maximumfish = d.randint(1, 15) #My Aquarium Maximum Fish Offset
  amnt = int(maximumfish) #Converts the My Aquarium Maximum Fish Offset to a integer
  a0 = "{0:0>2}"
  aa = a0.format
  a1 = aa(1)
  a2 = aa(2)
  a3 = aa(3)
  a4 = aa(4)
  a5 = aa(5)
  a6 = aa(6)
  a7 = aa(7)
  a8 = aa(8)
  a9 = aa(9)
  numl = l(range(10, 40))
  test_l1 = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9]
  fishidl = test_l1 + numl
  header = h.OrderedDict()
  header["unknown"] = j(0)  # Version?
  header["aquarium_size"] = j(int(aquarium_size))
  header["glass_type"] = j(int(glass_type))
  header["floor_type"] = j(int(floor_type))
  header["background_type"] = j(int(background_type))
  header["light_type"] = j(int(light_type))
  header["unknown_1"] = q(0)
  header["breeding_date_counter"] = l(0)
  header["unknown_date_counter"] = l(0)
  header["special_date_1_mding"] = j(0)
  header["special_date_1_month"] = j(int(specialdate1_month))
  header["special_date_1_day"] = j(int(specialdate1_day))
  header["special_date_1_mding_1"] = j(0)
  header["special_date_2_mding"] = j(0)
  header["special_date_2_month"] = j(int(specialdate2_month))
  header["special_date_2_day"] = j(int(specialdate2_day))
  header["special_date_2_mding_2"] = j(0)
  header["special_date_3_mding"] = j(0)
  header["special_date_3_month"] = j(int(specialdate3_month))
  header["special_date_3_day"] = j(int(specialdate3_day))
  header["special_date_3_mding_1"] = j(0)
  if decisionoffset == 1:
    if amnt <= 15:
        for i in range(amnt):
            sel = d.choice(fishidl)
            if sel < 40:
                header["fish_amount_%s" % i] = j(1)
                header["fish_id_%s" % i] = j(sel)
                header["fish_growth_level_%s" % i] = q(0)
                header["fish_hungry_degree_%s" % i] = q(0)
                header["fish_mding_%s" % i] = q(1)
                header["fish_birthday_%s" % i] = l(1)  # Birthday is day 1
                header["current_day_%s" % i] = l(1)  # Current day set to 1
                header["fish_tales"] = m(240 - (amnt * 16))
                header["object_tales"] = m(160)  # TODO: Add in object tales
                print ("Processing ...")
                f = e.BytesIO()
                for k, v in header.items(): f.write(v)
                f.flush()
                f.seek(0)
                copy = f.read()
                crc32 = format(g.crc32(copy) & 0xFFFFFFFF, '08x')
                f.close()
                file = open('a0014682.dat', 'wb')  # Not sure how the name is generated yet
                file.write(g.unhexlify('08051400'))  # Magic Value
                file.write(g.unhexlify(crc32))  # CRC32
                file.write(copy)  # Rest of File
                file.flush()
                file.close()
                datname = e.StringIO("a0014682.dat")
                nwcspath = r["nwcspathdd"]
                nwcssrc = path + "/" + datname
                secn(nwcssrc, nwcspath)
                print (nl)
                print ("Completed Successfully")
            else:
                raise Exception("Error Code 1 Occured.")
                o("Error: Invalid selection: %s" % v, "WARNING")
    else:
        raise Exception("Error Code 1 Occured.")
        o("Error: Invalid amount, skipping: %s" % v, "WARNING")
        amnt = 0
  else:
    print("Not doing fish....")
    header["fish_tales"] = m(240 - (amnt * 16))
    header["object_tales"] = m(160) 
    # TODO: Add in object tales
    print ("Processing ...")
    f = e.BytesIO()
    for k, v in header.items(): f.write(v)
    f.flush()
    f.seek(0)
    copy = f.read()
    crc32 = format(g.crc32(copy) & 0xFFFFFFFF, '08x')
    f.close()
    file = open('a0014682.dat', 'wb')  
    # Not sure how the name is generated yet
    file.write(g.unhexlify('08051400'))  # Magic Value
    file.write(g.unhexlify(crc32))  # CRC32
    file.write(copy)  # Rest of File
    file.flush()
    file.close()
    datname = e.StringIO("a0014682.dat")
    nwcspath = r["nwcspathdd"]
    nwcssrc = path + "/" + datname
    secn(nwcssrc, nwcspath)
    print (nl)
    print ("Completed Successfully")
else:
  raise Exception("Exit code 127 Occured.")
  o("You did not specify args: %s" % u, "WARNING")
  f._exit(127)
raise Exception("Unknown Error Occured") #It should never get here, but if it does, it lets you know.
o("Unknown Error Occured: %s" % unknownerrormsg, "WARNING")
f._exit(1)
