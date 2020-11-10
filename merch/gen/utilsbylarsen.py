import logging as f
import requests as g
import sentry_sdk as e
import struct as a
from sentry_sdk.integrations.logging import LoggingIntegration
g.packages.urllib3.disable_warnings()  # This is so we don't get some warning about SSL.
production = False
p_errors = False
def setup_log(sentry_url, print_errors):
    global logger, production
    sentry_logging = LoggingIntegration(
        level=f.INFO,
        event_level=f.INFO
    )
    e.init(dsn=sentry_url, integrations=[sentry_logging])
    logger = logging.getLogger(__name__)
    p_errors = print_errors
    production = True
def log(msg, level):  
    # TODO: Use number levels, strings are annoying
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
def u8(b):
    if not 0 <= b <= 255:
        log("u8 out of range: %s" % b, "INFO")
        b = 0
    return a.pack(">B", b)
def u16(b):
    if not 0 <= b <= 65535:
        log("u16 out of range: %s" % b, "INFO")
        b = 0
    return a.pack(">H", b)
def u32(b):
    if not 0 <= b <= 4294967295:
        log("u32 out of range: %s" % b, "INFO")
        b = 0
    return a.pack(">I", b)
def pad(c):
    d = ""
    for _ in range(c): d += "\0"
    return d
