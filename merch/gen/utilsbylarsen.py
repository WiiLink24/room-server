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


def pad(amnt):
    buffer = ""
    for _ in range(amnt): buffer += "\0"
    return buffer
