from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

import config
from helpers import xml_node_name, current_date_and_time, xml_node_name_update
from room import app
from flask import request

# As sourced from the app's main arc in secure/{key,iv}.bin.
FIRST_BIN_KEY = b"\x94\x3b\x13\xdd\x87\x46\x8b\xa5\xd9\xb7\xa8\xb8\x99\xf9\x18\x03"
FIRST_BIN_IV = b"\x66\xb3\x3f\xc1\x37\x3f\xe5\x06\xec\x2b\x59\xfb\x6b\x97\x7c\x82"

# Determine at import time what protocol to use as sourced from the config.
if config.root_https_enabled:
    root_protocol = "https"
else:
    root_protocol = "http"


def get_config_url(service_type: str) -> str:
    if service_type == "url1" and config.url1_cdn_url != "":
        return config.url1_cdn_url
    elif service_type == "url3" and config.url3_cdn_url != "":
        return config.url3_cdn_url

    if config.root_separate_subdomain:
        # https://url1.dev.wiilink24.com/
        return f"{root_protocol}://{service_type}.{config.root_domain}/"
    else:
        # https://dev.wiilink24.com/url1/
        return f"{root_protocol}://{config.root_domain}/{service_type}/"


@xml_node_name("Config")
def conf_first_bin_xml():
    data = {
        "maint": 0,
        "url1": get_config_url("url1"),
        "url2": get_config_url("url2"),
        "url3": get_config_url("url3"),
        "eulaver": 3,
        "shopurl": get_config_url("shop") + "index.esf",
        "shopkey": "7fce738e542f0a60fe5d8d8e1e8781af",
        "shopvalid": 1,
        "akahost": 5,
        "akaca": 1,
        "smpkey": "5ab362aa57dbb1dc16849e3e2d1cf2ff",
        "fmax": 30,
        "bmax": 10,
        "upddt": current_date_and_time(),
    }

    if "ptbr" in request.headers.get("User-Agent"):
        data["url1"] = "http://url1.ptbr.room.wiilink.ca/"
        data["url2"] = "http://url2.ptbr.room.wiilink.ca/"
        data["url3"] = "http://url3.ptbr.room.wiilink.ca/"
    elif "Du" in request.headers.get("User-Agent"):
        data["url1"] = "http://url1.ndl.room.wiilink.ca/"
        data["url2"] = "http://url2.ndl.room.wiilink.ca/"
        data["url3"] = "http://url3.ndl.room.wiilink.ca/"
    elif "It" in request.headers.get("User-Agent"):
        data["url1"] = "http://url1.it.room.wiilink.ca/"
        data["url2"] = "http://url2.it.room.wiilink.ca/"
        data["url3"] = "http://url3.it.room.wiilink.ca/"

    return data


@xml_node_name_update("Config")
def conf_first_bin_xml_update():
    return {
        "maint": 0,
        "url1": get_config_url("url1"),
        "url2": get_config_url("url2"),
        "url3": get_config_url("url3"),
        "eulaver": 3,
        "shopurl": get_config_url("shop") + "index.esf",
        "shopkey": "7fce738e542f0a60fe5d8d8e1e8781af",
        "shopvalid": 1,
        "akahost": 5,
        "akaca": 1,
        "smpkey": "5ab362aa57dbb1dc16849e3e2d1cf2ff",
        "fmax": 30,
        "bmax": 10,
        "upddt": current_date_and_time(),
    }


@app.route("/conf/first.bin")
def conf_first_bin():
    # first.bin is expected to be returned in an encrypted format.
    # First, we generate our response.
    ua = request.headers.get("User-Agent")
    if len(ua.split("/")) != 5:
        returned_xml = conf_first_bin_xml_update()
    else:
        returned_xml = conf_first_bin_xml()

    # Then, we encrypt.
    cipher = AES.new(FIRST_BIN_KEY, AES.MODE_CBC, iv=FIRST_BIN_IV)
    encrypted_xml = cipher.encrypt(pad(returned_xml, AES.block_size))

    return encrypted_xml
