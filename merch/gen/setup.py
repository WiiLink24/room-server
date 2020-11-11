import acwc24 as a
import calendar as b
import sys as e
import pathlib as g
import pyminizip as h
import pickle as i
import random as j
import requests as k
import subprocess as l
import time as k
from datetime import datetime
d=e.argv
m=print
n=l.run
c=e.exit
o=d[1] #Filename of Script that is being run
d1=int(d[2]) #Mode Identifier Data
path=g.Path(__file__).parent.absolute()
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
  t=k.localtime()
  current_time=k.strftime("%H:%M:%S", t)
  m(current_time)
  c(0)
elif d1==6:
  m(o)
  c(0)
elif d1==7:
  m(path)
  c(0)
elif d1==8:
  data=int(1)
  save=open('offset.dat', 'wb')
  load=open('password.dat', 'rb')
  ah=i.load(load_file)
  i.dump(textList, save)
  h.compress("offset.dat", path, "offset.enc", ah, int(compress_level))
  save.close()
  load.close()
  c(0)
elif d1==9:
  m("Congrats, you accessed the secret feature!\n")
  m("Code by Larsen, I take ZERO credit.\n")
  m("Credits also go to:\n")
  m("Aurum for making ACWC24. The BIN files were generated with ACDLC, also made by the same person.\n")
  m("Techincabor for helping me figure out the name of the DLC domain.\n")
  m("\n")
  m("so do not go saying I stole credit, as I take no credit and we will...\n")
  m("Just virtually ignore you if you say it.\n")
  ad=["anniversary_cake",
          "blue_Pikmin_hat",
          "bus_model",
          "Chihuahua_model",
          "dachshund_model",
          "dalmatian_model",
          "Dolphin_model",
          "Eiffel_tower",
          "fedora_chair",
          "flamenco_hat",
          "GameCube_dresser",
          "Gracie_dresser",
          "green_headgear",
          "guard_s_helmet",
          "hopscotch_floor",
          "Kapp_n_model",
          "Labrador_model",
          "ladder_shades",
          "Nintendo_DS_Lite",
          "Nintendo_DSi_B",
          "Nintendo_DSi_W",
          "Pave_clock",
          "red_Pikmin_hat",
          "shopping_cart",
          "tam_o_shanter",
          "Wii_locker",
          "wildflower_floor",
          "yellow_Pikmin_hat"]
  aa={}
  aa[1]=["snowman_head", "snowman_vanity"]
  aa[2]=["Cupid_bench"]
  aa[3]=["egg_TV", "shamrock_hat"]
  aa[4]=["egg_TV"]
  aa[5]=[]
  aa[6]=["banana_split_hat", "hot_dog_hat", "sand_castle"]
  aa[7]=["banana_split_hat", "hot_dog_hat", "sand_castle"]
  aa[8]=["banana_split_hat", "hot_dog_hat", "sand_castle"]
  aa[9]=["pile_of_leaves"]
  aa[10]=["pile_of_leaves"]
  aa[11]=["pile_of_leaves"]
  aa[12]=["snowman_head", "snowman_vanity", "Jingle_TV", "festive_wreath"]
  def picker():
      month=datetime.today().month
      ad_all=ad + aa[month]
      choice=j.choices(ad_all, weights=[1] * len(ad) + [2] * len(aa[month]), k=1)[0]
      return choice
  if os.path.exists("dlc.dat"):
      dlc_list=i.load(open("dlc.dat", "rb"))
      choice=list(dlc_list.values())[-1]
      while choice in list(dlc_list.values())[:len(ad)]:
          choice=picker()
      dlc_id=list(dlc_list.keys())[-1] + 1
  else:
      dlc_list={}
      choice=picker()
      dlc_id=1
  m("The next DLC item will be: " + choice + "!")
  dlc_list[dlc_id]=choice
  i.dump(dlc_list, open("dlc.dat", "wb"))
  a.create(choice, False, 8192 + dlc_id)
  region2={}
  region2["E"]="us"
  region2["P"]="eu"
  region2["J"]="jp"
  region2["K"]="kr"
  for region in ["E", "P", "J", "K"]:
      l.call(["mv", "build/" + choice + "_" + region + ".arc.wc24", "/var/www/wapp.wii.com/nwcs/public_html/ruu/rvforestdl_" + region2[region] + ".enc"])
  dlc_message="We are now distributing this item:\n\n" + choice + "\n\nEnjoy!"
  data={"username": "Animal Crossing DLC Bot", "content": dlc_message,
          "avatar_url": "http://rc24.xyz/images/logo-small.png", "attachments": [
              {"fallback": dlc_message, "color": "#549537", "author_name": "RiiConnect24 Animal Crossing DLC Script",
                  "author_icon": "https://rc24.xyz/images/ajs/animalcrossing/pete.png",
                  "text": dlc_message, "title": "Update!",
                  "fields": [{"title": "Script", "value": "Animal Crossing Wii", "short": "false"}],
                  "footer": "RiiConnect24 Script",
                  "footer_icon": "https://rc24.xyz/images/logo-small.png",
                  "ts": int(b.timegm(datetime.utcnow().timetuple()))}]}
  aj=open(discord.dat, 'rb')
  ai=i.load(aj)
  post_aj=k.post(ai.replace(b"\n", b""), json=data, allow_redirects=True)
  aj.close()
  c(0)
