# If you're adding a new config option, please update WiiLink24/production-deployment's
# copy of config.py to match the new options once committed to master.

# Primary config for room-server
db_url = "postgresql://username:password@localhost/database_name"
secret_key = "please_change_thank_you"
underground_enabled = False
elasticsearch_url = "localhost:9200"
