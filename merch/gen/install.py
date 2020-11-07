import sys as a
import pathlib as main
import pickle as c
import random as rn
import io as e
import os as ff
import binascii as g
import collections as h
import utilsbylarsen as nw
import json as p
import shutil as othr #Imports the base class of shutil
import time as misc
u1 = int
secn = othr.copyfile #Selectively imports copyfile from the base class of shutil.
j = nw.u8 # This line will import u8 from utilsbylarsen.py.
l = nw.u32 # This line will import u32 from utilsbylarsen.py.
m = nw.pad # This line will import pad from utilsbylarsen.py.
n = nw.setup_log # This line will import setup_log from utilsbylarsen.py.
o = nw.log # This line will import log from utilsbylarsen.py.
q = nw.u16 # This line will import u16 from utilsbylarsen.py.
path = main.Path(__file__).parent.absolute() #Obtains current path
with open("./nwcs.json", "rb") as f:
    r = p.load(f)
if r["production"] and r["send_logs"]:
    n(r["sentry_url"], False)
if r["production"]:
  dirdd = r["nwcspathdata"]
  f.mkdir(dirdd)
d = a.argv # Argument Class Data
dd1 = u1(d[1]) #Mode Specification Data
dd2 = d[2] #Line Number
dd3 = d[3] #Filename
dd4 = d[4] #Table Data
dd5 = d[5] #Unique ID Specification Data
dd6 = d[6] #Name of the Primary Storage File
dd7 = d[7] #Name of the Secondary Storage File
dd8 = d[8] #Datadog API Key
dd9 = d[9] #Datadog APP key
dd0 = u1(dd1) #Converts the mode specification Data to a integer
stg = e.StringIO #Installs a alias to the StringIO class
w = "Congrats, you accessed the secret feature!" #This script can also function as a My Aquarium DLC randomizer. You will see the message when you access that mode.
u = "Exit code 127 Occured" #Error code 127 message, this is usually called if args aren't specified correctly and/or if args aren't even there.
vv = "Error code 1 Occured." #Error code 1 message, this is a generic error for all other errors.
unknownerrormsg = "Error Code 1 Occured" #This error typically happens when the exit code fails, however it is currently unknown what would make that happen.
ext = ff._exit
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
  ext(0)
elif dd0 == 1: #Mode 1 Identifier Software Check
  dd = "/n" #New Line Identifier
  outF1 = open("tables.txt", y)
  textl1 = [dd, dd5, dd6, dd7]
  outF1.close()
  outF2 = open("id.txt", y)
  textl2 = [dd5]
  outF2.close()
  ext(0)
elif dd0 == 2: #Mode 2 Identifier Software Check
  file = open(dd3)
  all_lines = file.readlines()
  print((all_lines[dd2]))  
  ext(0)
elif dd0 == 3: #Mode 3 Identifier Software Check
  un = f.system
  un('echo Current Path: $PWD')
  un('viale=$(python3 password.py)')
  un('useradd -m -p $arg store')
  un('echo Created user with $arg password')
  un('cp -r -a $PWD/home/store. /home/store')
  un('echo Install done.')
  ext(0)
elif dd0 == 4: #Mode 4 Identifier Software Check
  print("The more bits, the more secure it is!")
  print("Availale bit sizes: 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192")
  w = eval(input("Enter the bitsize you want:"))
  x = d.getrandbits(w)
  print(x)
  ext(0)
elif dd0 == 5: #Mode 5 Identifier Software Check
  f = open('id.txt', z)
  file_contents = f.read()
  print(file_contents)
  f.close()
  ext(0)
elif dd0 == 6: #Mode 6 Identifier Software Check
  file = open('tables.txt')
  all_lines = file.readlines()
  print((all_lines[dd4]))
  ext(0)
elif dd0 == 7: #Mode 7 Identifier Software Check
  print(path) #Prints Current Path
  ext(0)
elif dd0 == 8: #Mode 8 Identifier Software Check
  configrange = list(range(2, 100)) # Returns Preset Line Number Range
  configl = list(configrange) #Outputs the Preset Line Number Range to a list
  outF1 = open(dd6, y)
  for line in configl:
    outF1.write(line)
    outF1.write(nl)
  outF1.close()
  v00 = stg("sentry_url")
  v01 = stg("printful_key")
  v02 = stg("production")
  v03 = stg("send_stats")
  v04 = stg("datadog_api_key")
  v05 = stg("datadog_app_key")
  v06 = stg("phpfilename")
  v07 = stg("php_logger_path")
  v08 = stg("php_logger_method")
  v09 = stg("send_php_logs")
  v10 = stg("api_key")
  v11 = stg("orders")
  v12 = stg("app_key")
  v13 = stg("offset")
  v14 = stg("limit")
  v15 = stg("code")
  v16 = stg("result")
  v17 = stg("https://api.theprintful.com/")
  v18 = stg("Printful API Python Library 1.2")
  v19 = stg("Authorization")
  v20 = stg("User-Agent")
  v21 = stg("Content-Type")
  v22 = stg("application/json")
  v23 = stg("paging")
  v24 = stg("total")
  v25 = stg("VERBOSE")
  v26 = stg("INFO")
  v27 = stg("WARNING")
  v28 = stg("CRITICAL")
  v36 = stg("./readtables.sh")
  v42 = stg("utf-8")
  v43 = stg("https://api.theprintful.com/")
  v44 = stg("Printful API Python Library 1.0")
  v45 = stg("User-Agent")
  v46 = stg("Content-Type")
  v47 = stg("application/json")
  v48 = stg("Server")
  v49 = stg("headers")
  v50 = stg("auth")
  v52 = stg("/")
  v53 = stg("fixtures")
  v55 = list(range(0, 1))
  v57 = stg("API response was not valid JSON.")
  v58 = stg("GET")
  v59 = stg("POST")
  v60 = stg("PUT")
  v61 = stg("DELETE")
  v62 = stg("API response did not contain paginated results.")
  v63 = stg(">B")
  v64 = stg(">H")
  v65 = stg(">I")
  v66 = stg("<I")
  v67 = stg(">b")
  v68 = stg(">h")
  v69 = stg(">i")
  v70 = stg("0")
  v71 = stg("255")
  v73 = stg("65535")
  v75 = stg("4294967295")
  v77 = stg("4294967295")
  v78 = stg("-128")
  v79 = stg("127")
  v80 = stg("-32768")
  v81 = stg("32767")
  v82 = stg("-2147483648")
  v83 = stg("2147483647")
  v84 = list(range(1, 2))
  v90 = stg("200")
  v91 = stg("301")
  v92 = stg("ascii")
  v93 = stg("256")
  v94 = stg("128")
  v95 = stg("512")
  v96 = list(range(3, 4))
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
  ext(0)
elif dd0 == 9: #Mode 9 Identifier Software Check
  print(w)
  print ("My Aquarium Custom Attachment Generator\n")
  print ("By John Pansera / Version 1.0\n")
  print ("Randomization Mod by 6100m, porting concepts by TMinusBlastedRocket, zero casting work of butch@stackoverflow\n")
  rr = rn.randint
  aquarium_size = rr(0, 3) #My Aquarium Tank Size Offset
  glass_type = rr(0, 6) #My Aquarium Glass Size Offset
  floor_type = rr(0, 5) #My Aquarium Floor Type Offset
  background_type = rr(0, 5) #My Aquarium Background Type Offset
  light_type = rr(0, 7) #My Aquarium Light Type Offset
  specialdate1_month = rr(1, 13) #My Aquarium Special Date 1 Month Offset
  specialdate1_day = rr(1, 32) #My Aquarium Special Date 1 Day Offset
  specialdate2_month = rr(1, 13) #My Aquarium Special Date 2 Month Offset
  specialdate2_day = rr(1, 32) #My Aquarium Special Date 2 Day Offset
  specialdate3_month = rr(1, 13) #My Aquarium Special Date 3 Month Offset
  specialdate3_day = rr(1, 32) #My Aquarium Special Date 3 Day Offset
  decisionoffset = rr(1, 25) #My Aquarium Add Fish Decisional Offset
  maximumfish = rr(1, 16) #My Aquarium Maximum Fish Offset
  df = u1(decisionoffset) #Obsufcates variable to be shorter via aliasing
  amnt = u1(maximumfish) #Converts the My Aquarium Maximum Fish Offset to a integer
  numl = list(range(1, 40))
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
  header["special_date_1_padding"] = j(0)
  header["special_date_1_month"] = j(int(specialdate1_month))
  header["special_date_1_day"] = j(int(specialdate1_day))
  header["special_date_1_padding_1"] = j(0)
  header["special_date_2_padding"] = j(0)
  header["special_date_2_month"] = j(int(specialdate2_month))
  header["special_date_2_day"] = j(int(specialdate2_day))
  header["special_date_2_padding_2"] = j(0)
  header["special_date_3_padding"] = j(0)
  header["special_date_3_month"] = j(int(specialdate3_month))
  header["special_date_3_day"] = j(int(specialdate3_day))
  header["special_date_3_padding_1"] = j(0)
  if df == 1 or df == 3 or df == 5 or df == 7 or df == 9 or df == 11 or df == 13 or df == 15 or df == 17 or df == 19 or df == 21 or df == 23:
    if amnt <= 15:
        for i in range(amnt):
            sel = rn.choice(numl)
            if sel < 40:
                header["fish_amount_%s" % i] = j(1)
                header["fish_id_%s" % i] = j(sel)
                header["fish_growth_level_%s" % i] = q(0)
                header["fish_hungry_degree_%s" % i] = q(0)
                header["fish_padding_%s" % i] = q(1)
                header["fish_birthday_%s" % i] = l(1)  # Birthday is day 1
                header["current_day_%s" % i] = l(1)  # Current day set to 1
                header["fish_tables"] = m(240 - (amnt * 16))
                header["object_tables"] = m(160)  # TODO: Add in object tables
                print ("Processing ...")
                f = e.BytesIO()
                for k, v in list(header.items()): f.write(v)
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
                datname = "a0014682.dat"
                nwcspath = r["nwcspathdata"]
                nwcssrc = str(path) + "/" + str(datname)
                secn(nwcssrc, nwcspath)
                print (nl)
                print ("Completed Successfully")
                a.exit(0)
            else:
                raise Exception("Error Code 1 Occured.")
                o("Error: Invalid selection: %s" % vv, "WARNING")
    else:
        raise Exception("Error Code 1 Occured.")
        o("Error: Invalid amount, skipping: %s" % vv, "WARNING")
        amnt = 0
  else:
    print("Not doing fish....")
    header["fish_tables"] = m(240 - (amnt * 16))
    header["object_tables"] = m(160) 
    # TODO: Add in object tables
    print ("Processing ...")
    f = e.BytesIO()
    for k, v in list(header.items()): f.write(v)
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
    datname = "a0014682.dat"
    nwcspath = r["nwcspathdata"]
    nwcssrc = str(path) + "/" + str(datname)
    secn(nwcssrc, nwcspath)
    print (nl)
    print ("Completed Successfully")
    a.exit(0)
else:
  raise Exception("Exit code 127 Occured.")
  o("You did not specify args: %s" % u, "WARNING")
  ext(127)
raise Exception("Unknown Error Occured") #It should never get here, but if it does, it lets you know.
o("Unknown Error Occured: %s" % unknownerrormsg, "WARNING")
ext(1)
