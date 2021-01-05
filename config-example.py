# If you're adding a new config option, please update WiiLink24/production-deployment's
# copy of config.py to match the new options once committed to master.

# Primary config for room-server
db_url = "postgresql://username:password@localhost/database_name"
elasticsearch_url = "localhost:9200"

# Used as the base domain within first.bin.
# To resolve to 127.0.0.1, feel free to use "dev.wiilink24.com".
root_domain = "dev.wiilink24.com"
root_https_enabled = False
# If true, assumes url1, url2, url3 and shop subdomains (i.e. url1.dev.wiilink24.com).
# If false, assumes dev.wiilink24.com/url1. If you are not reverse proxying, keep this False.
root_separate_subdomain = False

# Used to secure the web panel.
underground_enabled = False
secret_key = "please_change_thank_you"

# If using a setup with multiple versions os room-server, set this to False.
video_deletion_enabled = True
