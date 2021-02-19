# If you're adding a new config option, please update WiiLink24/production-deployment's
# copy of config.py to match the new options once committed to master.

# Primary config for room-server
db_url = "sqlite:///mnt/c/Users/zurgE/OneDrive/Documents/room-server-master/app.db"

# Configuration for Elasticsearch
elasticsearch_url = "localhost:9200"
elasticsearch_user = "admin"
elasticsearch_pass = "admin"

# Used as the base domain within first.bin.
# To resolve to 127.0.0.1, feel free to use "dev.wiilink24.com".
root_domain = "dev.wiilink24.com"
root_https_enabled = False
# If true, assumes url1, url2, url3 and shop subdomains (i.e. url1.dev.wiilink24.com).
# If false, assumes dev.wiilink24.com/url1. If you are not reverse proxying, keep this False.
root_separate_subdomain = False

# Used to secure the web panel.
secret_key = "please_change_thank_you"

# If using a setup with multiple versions of room-server, set this to False.
video_deletion_enabled = True

maxmind_account_id = 0
maxmind_license_id = ""

use_localized_time = True
