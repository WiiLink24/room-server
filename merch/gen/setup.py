import acwc24
import calendar
import os
import sys
import pathlib
import pyminizip
import pickle
import random
import requests
import subprocess
import time
from datetime import datetime
currentfile = d[1] #Filename of Script that is being run
d1 = d[2] #Mode Identifier Data
path = pathlib.Path(__file__).parent.absolute()
if d1 == 0:
  subprocess.run('python3 setup.py 1', shell=True)
  subprocess.run('python3 setup.py 2', shell=True)
  subprocess.run('python3 setup.py 3', shell=True)
  subprocess.run('python3 setup.py 4', shell=True)
if d1 == 1:
  subprocess.run('python3 install.py 1 0 0 0 1 primary.txt secondary.txt 0 0', shell=True)
if d1 == 2:
  subprocess.run('python3 install.py 3 0 0 0 0 0 0 0 0', shell=True)
if d1 == 3:
  subprocess.run('python3 install.py 4 0 0 0 0 0 0 0 0', shell=True)
if d1 == 4:
  subprocess.run('python3 install.py 8 0 0 0 0 primary.txt secondary.txt 0 0', shell=True)
if d1 == 5:
  t = time.localtime()
  current_time = time.strftime("%H:%M:%S", t)
  print(current_time)
if d1 == 6:
  print(currentfile)
if d1 == 7:
  print(path)
if d1 == 8:
  data = int(1)
  save = open('offset.dat', 'wb')
  load = open('password.dat', 'rb')
  loaded = pickle.load(load_file)
  pickle.dump(textList, save)
  pyminizip.compress("offset.dat", path, "offset.enc", loaded, int(compress_level))
  save.close()
  load.close()
if d1 == 9:
  print("Congrats, you accessed the secret feature!\n")
  print("Code by Larsen, I take ZERO credit.\n")
  print("so do not go saying I stole credit, as I take no credit and we will...\n")
  print("Just virtually ignore you if you say it.\n")
  items = ["anniversary_cake",
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
  items_seasonal = {}
  items_seasonal[1] = ["snowman_head", "snowman_vanity"]
  items_seasonal[2] = ["Cupid_bench"]
  items_seasonal[3] = ["egg_TV", "shamrock_hat"]
  items_seasonal[4] = ["egg_TV"]
  items_seasonal[5] = []
  items_seasonal[6] = ["banana_split_hat", "hot_dog_hat", "sand_castle"]
  items_seasonal[7] = ["banana_split_hat", "hot_dog_hat", "sand_castle"]
  items_seasonal[8] = ["banana_split_hat", "hot_dog_hat", "sand_castle"]
  items_seasonal[9] = ["pile_of_leaves"]
  items_seasonal[10] = ["pile_of_leaves"]
  items_seasonal[11] = ["pile_of_leaves"]
  items_seasonal[12] = ["snowman_head", "snowman_vanity", "Jingle_TV", "festive_wreath"]
  def picker():
      month = datetime.today().month
      items_all = items + items_seasonal[month]
      choice = random.choices(items_all, weights=[1] * len(items) + [2] * len(items_seasonal[month]), k=1)[0]
      return choice
  if os.path.exists("dlc.dat"):
      dlc_list = pickle.load(open("dlc.dat", "rb"))
      choice = list(dlc_list.values())[-1]
      while choice in list(dlc_list.values())[:len(items)]:
          choice = picker()
      dlc_id = list(dlc_list.keys())[-1] + 1
  else:
      dlc_list = {}
      choice = picker()
      dlc_id = 1
  print("The next DLC item will be: " + choice + "!")
  dlc_list[dlc_id] = choice
  pickle.dump(dlc_list, open("dlc.dat", "wb"))
  acwc24.create(choice, False, 8192 + dlc_id)
  region2 = {}
  region2["E"] = "us"
  region2["P"] = "eu"
  region2["J"] = "jp"
  region2["K"] = "kr"
  for region in ["E", "P", "J", "K"]:
      subprocess.call(["mv", "build/" + choice + "_" + region + ".arc.wc24", "/var/www/wapp.wii.com/nwcs/public_html/ruu/rvforestdl_" + region2[region] + ".enc"])
  dlc_message = "We are now distributing this item:\n\n" + choice + "\n\nEnjoy!"
  data = {"username": "Animal Crossing DLC Bot", "content": dlc_message,
          "avatar_url": "http://rc24.xyz/images/logo-small.png", "attachments": [
              {"fallback": dlc_message, "color": "#549537", "author_name": "RiiConnect24 Animal Crossing DLC Script",
                  "author_icon": "https://rc24.xyz/images/webhooks/animalcrossing/pete.png",
                  "text": dlc_message, "title": "Update!",
                  "fields": [{"title": "Script", "value": "Animal Crossing Wii", "short": "false"}],
                  "footer": "RiiConnect24 Script",
                  "footer_icon": "https://rc24.xyz/images/logo-small.png",
                  "ts": int(calendar.timegm(datetime.utcnow().timetuple()))}]}
  webhook = open(discord.dat, 'rb')
  webhook_url = pickle.load(webhook)
  post_webhook = requests.post(webhook_url.replace(b"\n", b""), json=data, allow_redirects=True)
