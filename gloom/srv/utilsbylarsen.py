import sentry_sdk
import logging
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