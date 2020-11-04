import errno
import logging
import os
import requests
import sentry_sdk
import struct
from sentry_sdk.integrations.logging import LoggingIntegration

"""Unification of utilities used by all scripts."""

requests.packages.urllib3.disable_warnings()  # This is so we don't get some warning about SSL.

production = False
p_errors = False

def setup_log(sentry_url, print_errors):
    global logger, production
    sentry_logging = LoggingIntegration(
        level=logging.INFO,
        event_level=logging.INFO
    )
    sentry_sdk.init(dsn=sentry_url, integrations=[sentry_logging])
    logger = logging.getLogger(__name__)
    p_errors = print_errors
    production = True

def log(msg, level):  # TODO: Use number levels, strings are annoying
    if p_errors:
        print(msg)

    if production:
        if level == "VERBOSE":
            logger.debug(msg)
        elif level == "INFO":
            logger.info(msg)
        elif level == "WARNING":
            logger.warning(msg)
        elif level == "CRITICAL":
            logger.critical(msg)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except:
        pass


"""Pack integers to specific type."""

# Unsigned integers

def u8(data):
    if not 0 <= data <= 255:
        log("u8 out of range: %s" % data, "INFO")
        data = 0
    return struct.pack(">B", data)


def u16(data):
    if not 0 <= data <= 65535:
        log("u16 out of range: %s" % data, "INFO")
        data = 0
    return struct.pack(">H", data)


def u32(data):
    if not 0 <= data <= 4294967295:
        log("u32 out of range: %s" % data, "INFO")
        data = 0
    return struct.pack(">I", data)


def u32_littleendian(data):
    if not 0 <= data <= 4294967295:
        log("u32 little endian out of range: %s" % data, "INFO")
        data = 0
    return struct.pack("<I", data)

# Signed integer

def s8(data):
    if not -128 <= data <= 127:
        log("s8 out of range: %s" % data, "INFO")
        data = 0
    return struct.pack(">b", data)


def s16(data):
    if not -32768 <= data <= 32767:
        log("s16 out of range: %s" % data, "INFO")
        data = 0
    return struct.pack(">h", data)


def s32(data):
    if not -2147483648 <= data <= 2147483647:
        log("s32 out of range: %s" % data, "INFO")
        data = 0
    return struct.pack(">i", data)

def pad(amnt):
    buffer = ""
    for _ in range(amnt): buffer += "\0"
    return buffer
