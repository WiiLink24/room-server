from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

import config
from helpers import xml_node_name, current_date_and_time
from room import app

# As sourced from the app's main arc in secure/{key,iv}.bin.
FIRST_BIN_KEY = b"\x94\x3B\x13\xDD\x87\x46\x8B\xA5\xD9\xB7\xA8\xB8\x99\xF9\x18\x03"
FIRST_BIN_IV = b"\x66\xB3\x3F\xC1\x37\x3F\xE5\x06\xEC\x2B\x59\xFB\x6B\x97\x7C\x82"

# Determine at import time what protocol to use as sourced from the config.
if config.root_https_enabled:
    root_protocol = "https"
else:
    root_protocol = "http"


def get_config_url(service_type: str) -> str:
    if config.root_separate_subdomain:
        # https://url1.dev.wiilink24.com/
        return f"{root_protocol}://{service_type}.{config.root_domain}/"
    else:
        # https://dev.wiilink24.com/url1/
        return f"{root_protocol}://{config.root_domain}/{service_type}/"


@xml_node_name("Config")
def conf_first_bin_xml():
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
    returned_xml = conf_first_bin_xml()

    # Then, we encrypt.
    cipher = AES.new(FIRST_BIN_KEY, AES.MODE_CBC, iv=FIRST_BIN_IV)
    encrypted_xml = cipher.encrypt(pad(returned_xml, AES.block_size))

    return encrypted_xml


class ABC:
    def __init__(self, text: str):
        self.text = text

    def print_func(self):
        print(self.text)


class DEF(ABC):
    def __init__(self):
        lol = super("lmfao")
        lol.print_func()
