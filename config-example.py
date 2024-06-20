# If you're adding a new config option, please update WiiLink24/production-deployment's
# copy of config.py to match the new options once committed to master.

# Primary config for room-server
db_url = "postgresql://username:password@localhost/database_name"

# Used as the base domain within first.bin.
# To resolve to 127.0.0.1, feel free to use "dev.wiilink24.com".
root_domain = "dev.wiilink24.com"
root_https_enabled = False
# If true, assumes url1, url2, url3 and shop subdomains (i.e. url1.dev.wiilink24.com).
# If false, assumes dev.wiilink24.com/url1. If you are not reverse proxying, keep this False.
root_separate_subdomain = False

# Used to secure the web panel.
secret_key = "please_change_thank_you"

# Sentry configuration for error logging.
use_sentry = False
sentry_dsn = "https://public@sentry.example.com/1"

use_s3 = False
r2_account_id = ""
r2_bucket_name = "room-server"
s3_connection_url = ""
s3_access_key_id = ""
s3_secret_access_key = ""

url1_cdn_url = "http://url1.videos.wiilink24.com"

ds_rsa_key_path = ""

# OpenID Connect configuration
client_secrets_path = "client_secrets.json"