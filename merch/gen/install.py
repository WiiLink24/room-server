import sys as a
import pathlib as main
import pickle as c
import random as d
import io as e
import os as f
import binascii as g
import collections as h
import utilsbylarsen as nwcsutils
import json as p
import shutil as othr #Imports the base class of shutil
import time as misc
secn = othr.copyfile #Selectively imports copyfile from the base class of shutil.
j = nwcsutils.u8 # This line will import u8 from utilsbylarsen.py.
l = nwcsutils.u32 # This line will import u32 from utilsbylarsen.py.
m = nwcsutils.pad # This line will import pad from utilsbylarsen.py.
n = nwcsutils.setup_log # This line will import setup_log from utilsbylarsen.py.
o = nwcsutils.log # This line will import log from utilsbylarsen.py.
q = nwcsutils.u16 # This line will import u16 from utilsbylarsen.py.
currentpath = main.Path(__file__).parent.absolute() #Obtains current path
b = "rb" #Generic JSON Opcode
generic = "production" #Production Mode Parent Data
with open("./nwcs.json", b) as f:
    r = p.load(f)
if r[generic] and r["send_logs"]:
    n(r["sentry_url"], False)
if r[generic]:
  directorycreationdata = r["nwcspathdata"]
  f.mkdir(directorycreationdata)
argdata0 = a.argv[0] #Python Filename
argdata1 = a.argv[1] #Mode Specification Data
argdata2 = a.argv[2] #Line Number
argdata3 = a.argv[3] #Filename
argdata4 = a.argv[4] #Table Data
argdata5 = a.argv[5] #Unique ID Specification Data
argdata6 = a.argv[6] #Name of the Primary Storage File
argdata7 = a.argv[7] #Name of the Secondary Storage File
argdata8 = a.argv[8] #Datadog API Key
argdata9 = a.argv[9] #Datadog APP key
w = e.StringIO("Congrats, you accessed the secret feature!") #This script can also function as a My Aquarium DLC randomizer. You will see the message when you access that mode.
u = e.StringIO("Exit code 127 Occured") #Error code 127 message, this is usually called if args aren't specified correctly and/or if args aren't even there.
v = e.StringIO("Error code 1 Occured.") #Error code 1 message, this is a generic error for all other errors.
y = "w" #Text Writing Opcode
z = 'r' #Generic Textfile Opcode
if argdata1 == 0: #Mode 0 Identifier Software Check
  options = {
    'api_key': argdata8,
    'app_key': argdata9
  }
  saveoptionsfile = open(options.dat, 'wb')
  c.dump(options, saveoptionsfile)
  f._exit(0)
elif argdata1 == 1: #Mode 1 Identifier Software Check
  data = "/n" #New Line Identifier
  outF1 = open("tables.txt", y)
  textList1 = [data, argdata5, argdata6, argdata7]
  outF1.close()
  outF2 = open("id.txt", y)
  textList2 = [argdata5]
  outF2.close()
  f._exit(0)
elif argdata1 == 2: #Mode 2 Identifier Software Check
  file = open(argdata3)
  all_lines = file.readlines()
  print(all_lines[argdata2])  
  f._exit(0)
elif argdata1 == 3: #Mode 3 Identifier Software Check
  f.system('echo Current Path: $PWD')
  f.system('variable=$(python3 password.py)')
  f.system('useradd -m -p $arg store')
  f.system('echo Created user with $arg password')
  f.system('cp -r -a $PWD/home/store. /home/store')
  f.system('echo Install done.')
  print("Exiting in 11...")
  misc.sleep(1)
  print("Exiting in 10...")
  misc.sleep(1)
  print("Exiting in 9...")
  misc.sleep(1)
  print("Exiting in 8...")
  misc.sleep(1)
  print("Exiting in 7...")
  misc.sleep(1)
  print("Exiting in 6...")
  misc.sleep(1)
  print("Exiting in 5...")
  misc.sleep(1)
  print("Exiting in 4...")
  misc.sleep(1)
  print("Exiting in 3...")
  misc.sleep(1)
  print("Exiting in 2...")
  misc.sleep(1)
  print("Exiting in 1...")
  misc.sleep(1)
  normal = 0 #Success Notification Data
  f._exit(normal)
elif argdata1 == 4: #Mode 4 Identifier Software Check
  print("The more bits, the more secure it is!")
  print("Available bit sizes: 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192")
  w = input("Enter the bitsize you want:")
  x = d.getrandbits(w)
  print(x)
  f._exit(0)
elif argdata1 == 5: #Mode 5 Identifier Software Check
  f = open('id.txt', z)
  file_contents = f.read()
  print(file_contents)
  f.close()
  f._exit(0)
elif argdata1 == 6: #Mode 6 Identifier Software Check
  file = open('tables.txt')
  all_lines = file.readlines()
  print(all_lines[argdata4])
  f._exit(0)
elif argdata1 == 7: #Mode 7 Identifier Software Check
  print(currentpath) #Prints Current Path
  f._exit(0)
elif argdata1 == 8: #Mode 8 Identifier Software Check
  configrange = range(2, 100) # Returns Preset Line Number Range
  configlist = list(configrange) #Outputs the Preset Line Number Range to a list
  outF1 = open(argdata6, y)
  for line in configlist:
    # write line data to primary storage file
    outF1.write(line)
    outF1.write("\n")
  outF1.close()
  variablelist = []
  s = variablelist.append
  var00 = e.StringIO("sentry_url")
  var01 = e.StringIO("printful_key")
  var02 = e.StringIO("production")
  var03 = e.StringIO("send_stats")
  var04 = e.StringIO("datadog_api_key")
  var05 = e.StringIO("datadog_app_key")
  var06 = e.StringIO("phpfilename")
  var07 = e.StringIO("php_logger_path")
  var08 = e.StringIO("php_logger_method")
  var09 = e.StringIO("send_php_logs")
  var10 = e.StringIO("api_key")
  var11 = e.StringIO("orders")
  var12 = e.StringIO("app_key")
  var13 = e.StringIO("offset")
  var14 = e.StringIO("limit")
  var15 = e.StringIO("code")
  var16 = e.StringIO("result")
  var17 = e.StringIO("https://api.theprintful.com/")
  var18 = e.StringIO("Printful API Python Library 1.2")
  var19 = e.StringIO("Authorization")
  var20 = e.StringIO("User-Agent")
  var21 = e.StringIO("Content-Type")
  var22 = e.StringIO("application/json")
  var23 = e.StringIO("paging")
  var24 = e.StringIO("total")
  var25 = e.StringIO("VERBOSE")
  var26 = e.StringIO("INFO")
  var27 = e.StringIO("WARNING")
  var28 = e.StringIO("CRITICAL")
  var29 = e.StringIO("INFO")
  var30 = e.StringIO("INFO")
  var31 = e.StringIO("INFO")
  var32 = e.StringIO("INFO")
  var33 = e.StringIO("INFO")
  var34 = e.StringIO("INFO")
  var35 = e.StringIO("INFO")
  var36 = e.StringIO("./readtables.sh")
  var37 = e.StringIO("./readtables.sh")
  var38 = e.StringIO("./readtables.sh")
  var39 = e.StringIO("paging")
  var40 = e.StringIO("paging")
  var41 = e.StringIO("total")
  var42 = e.StringIO("utf-8")
  var43 = e.StringIO("https://api.theprintful.com/")
  var44 = e.StringIO("Printful API Python Library 1.0")
  var45 = e.StringIO("User-Agent")
  var46 = e.StringIO("Content-Type")
  var47 = e.StringIO("application/json")
  var48 = e.StringIO("Server")
  var49 = e.StringIO("headers")
  var50 = e.StringIO("auth")
  var51 = e.StringIO("headers")
  var52 = e.StringIO("/")
  var53 = e.StringIO("fixtures")
  var54 = e.StringIO("utf-8")
  var55 = e.StringIO("0")
  var56 = e.StringIO("1")
  var57 = e.StringIO("API response was not valid JSON.")
  var58 = e.StringIO("GET")
  var59 = e.StringIO("POST")
  var60 = e.StringIO("PUT")
  var61 = e.StringIO("DELETE")
  var62 = e.StringIO("API response did not contain paginated results.")
  var63 = e.StringIO(">B")
  var64 = e.StringIO(">H")
  var65 = e.StringIO(">I")
  var66 = e.StringIO("<I")
  var67 = e.StringIO(">b")
  var68 = e.StringIO(">h")
  var69 = e.StringIO(">i")
  var70 = e.StringIO("0")
  var71 = e.StringIO("255")
  var72 = e.StringIO("0")
  var73 = e.StringIO("65535")
  var74 = e.StringIO("0")
  var75 = e.StringIO("4294967295")
  var76 = e.StringIO("0")
  var77 = e.StringIO("4294967295")
  var78 = e.StringIO("-128")
  var79 = e.StringIO("127")
  var80 = e.StringIO("-32768")
  var81 = e.StringIO("32767")
  var82 = e.StringIO("-2147483648")
  var83 = e.StringIO("2147483647")
  var84 = e.StringIO("1")
  var85 = e.StringIO("2")
  var86 = e.StringIO("1")
  var87 = e.StringIO("2")
  var88 = e.StringIO("1")
  var89 = e.StringIO("2")
  var90 = e.StringIO("200")
  var91 = e.StringIO("301")
  var92 = e.StringIO("ascii")
  var93 = e.StringIO("256")
  var94 = e.StringIO("128")
  var95 = e.StringIO("512")
  var96 = e.StringIO("3")
  var97 = e.StringIO("4")
  s(var00)
  s(var01)
  s(var02)
  s(var03)
  s(var04)
  s(var05)
  s(var06)
  s(var07)
  s(var08)
  s(var09)
  s(var10)
  s(var11)
  s(var12)
  s(var13)
  s(var14)
  s(var15)
  s(var16)
  s(var17)
  s(var18)
  s(var19)
  s(var20)
  s(var21)
  s(var22)
  s(var23)
  s(var24)
  s(var25)
  s(var26)
  s(var27)
  s(var28)
  s(var29)
  s(var30)
  s(var31)
  s(var32)
  s(var33)
  s(var34)
  s(var35)
  s(var36)
  s(var37)
  s(var38)
  s(var39)
  s(var40)
  s(var41)
  s(var42)
  s(var43)
  s(var44)
  s(var45)
  s(var46)
  s(var47)
  s(var48)
  s(var49)
  s(var50)
  s(var51)
  s(var52)
  s(var53)
  s(var54)
  s(var55)
  s(var56)
  s(var57)
  s(var58)
  s(var59)
  s(var60)
  s(var61)
  s(var62)
  s(var63)
  s(var64)
  s(var65)
  s(var66)
  s(var67)
  s(var68)
  s(var69)
  s(var70)
  s(var71)
  s(var72)
  s(var73)
  s(var74)
  s(var75)
  s(var76)
  s(var77)
  s(var78)
  s(var79)
  s(var80)
  s(var81)
  s(var82)
  s(var83)
  s(var84)
  s(var85)
  s(var86)
  s(var87)
  s(var88)
  s(var89)
  s(var90)
  s(var91)
  s(var92)
  s(var93)
  s(var94)
  s(var95)
  s(var96)
  s(var97)
  outF2 = open(argdata7, y)
  for line in variablelist:
    # write variable data to secondary storage file
    outF2.write(line)
    outF2.write("\n")
  outF2.close()
  f._exit(0)
elif argdata1 == 9: #Mode 9 Identifier Software Check
  print(w)
  print ("My Aquarium Custom Attachment Generator")
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
  idmain0 = "{0:0>2}"
  formatjob = idmain0.format
  idmain1 = formatjob(1)
  idmain2 = formatjob(2)
  idmain3 = formatjob(3)
  idmain4 = formatjob(4)
  idmain5 = formatjob(5)
  idmain6 = formatjob(6)
  idmain7 = formatjob(7)
  idmain8 = formatjob(8)
  idmain9 = formatjob(9)
  idsecn0 = 10
  idsecn1 = 11
  idsecn2 = 12
  idsecn3 = 13
  idsecn4 = 14
  idsecn5 = 15
  idsecn6 = 16
  idsecn7 = 17
  idsecn8 = 18
  idsecn9 = 19
  idothr0 = 20
  idothr1 = 21
  idothr2 = 22
  idothr3 = 23
  idothr4 = 24
  idothr5 = 25
  idothr6 = 26
  idothr7 = 27
  idothr8 = 28
  idothr9 = 29
  idmisc0 = 30
  idmisc1 = 31
  idmisc2 = 32
  idmisc3 = 33
  idmisc4 = 34
  idmisc5 = 35
  idmisc6 = 36
  idmisc7 = 37
  idmisc8 = 38
  idmisc9 = 39
  fishidlist = []
  t = fishidlist.append
  t(idmain1)
  t(idmain2)
  t(idmain3)
  t(idmain4)
  t(idmain5)
  t(idmain6)
  t(idmain7)
  t(idmain8)
  t(idmain9)
  t(idsecn0)
  t(idsecn1)
  t(idsecn2)
  t(idsecn3)
  t(idsecn4)
  t(idsecn5)
  t(idsecn6)
  t(idsecn7)
  t(idsecn8)
  t(idsecn9)
  t(idothr0)
  t(idothr1)
  t(idothr2)
  t(idothr3)
  t(idothr4)
  t(idothr5)
  t(idothr6)
  t(idothr7)
  t(idothr8)
  t(idothr9)
  t(idmisc0)
  t(idmisc1)
  t(idmisc2)
  t(idmisc3)
  t(idmisc4)
  t(idmisc5)
  t(idmisc6)
  t(idmisc7)
  t(idmisc8)
  t(idmisc9)
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
            sel = d.choice(fishidlist)
            if sel < 40:
                header["fish_amount_%s" % i] = j(1)
                header["fish_id_%s" % i] = j(sel)
                header["fish_growth_level_%s" % i] = q(0)
                header["fish_hungry_degree_%s" % i] = q(0)
                header["fish_mding_%s" % i] = q(1)
                header["fish_birthday_%s" % i] = l(1)  # Birthday is day 1
                header["current_day_%s" % i] = l(1)  # Current day set to 1
                header["fish_tables"] = m(240 - (amnt * 16))
                header["object_tables"] = m(160)  # TODO: Add in object tables
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
                datfilename = e.StringIO("a0014682.dat")
                nwcspathvariable = r["nwcspathdata"]
                nwcssrcvariable = currentpath + "/" + datfilename
                secn(nwcssrcvariable, nwcspathvariable)
                print ("\n")
                print ("Completed Successfully")
            else:
                raise Exception("Error code 1 Occured.")
                print ("Error: Invalid selection")
                o("Error: Invalid selection: %s" % v, "WARNING")
    else:
        print ("Error: Invalid amount, skipping")
        o("Error: Invalid amount, skipping: %s" % v, "WARNING")
        amnt = 0
  else:
    print("Not doing fish....")
    header["fish_tables"] = m(240 - (amnt * 16))
    header["object_tables"] = m(160)  # TODO: Add in object tables
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
    datfilename = e.StringIO("a0014682.dat")
    nwcspathvariable = r["nwcspathdata"]
    nwcssrcvariable = currentpath + "/" + datfilename
    secn(nwcssrcvariable, nwcspathvariable)
    print ("\n")
    print ("Completed Successfully")
else:
  raise Exception("Exit code 127 Occured.")
  o("You did not specify args: %s" % u, "WARNING")
  f._exit(127)
raise Exception("Unknown Error Occured") #It should never get here, but if it does, it lets you know.
unknownerrorcode = 1
unknownerrormsg = e.StringIO("Error Code 1 Occured")
o("Unknown Error Occured: %s" % unknownerrormsg, "WARNING")
f._exit(unknownerrorcode)
