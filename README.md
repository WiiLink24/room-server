# room-server
[![Build](https://github.com/WiiLink24/room-server/actions/workflows/push_docker_image.yml/badge.svg)](https://github.com/WiiLink24/room-server/actions/workflows/push_docker_image.yml)
## What is this?
room-server provides a server usable with [Wii no Ma](https://en.wikipedia.org/wiki/Wii_no_Ma).

## Running
**Note**: As of `2b40385e69b40e9c85b26bed2c96006438c80644`, Python <=3.9 is needed. If you need to use 3.8 or lower, you can use the `Pre-Python-3.9-Requirement` tag, however, do note that this version is **not** maintained and that further commits may be based off of Python 3.9 features and syntax.

You'll most likely want to [create a virtualenv](https://docs.python.org/3/library/venv.html) to install things. For example:
```
python3 -m venv virtualenv
```
Ensure you active the environment.

Regardless of the above, ensure you have installed requirements:
```
pip3 install -r requirements.txt
# Useful for reading .flaskenv.
pip3 install python-dotenv
```

You'll then need to install PostgreSQL or a similar database among others. Copy `config-example.py` to `config.py` and update this config.

Next, read `conf/README.md` for instructions of static files you should provide.

Finally, run in development mode, and enjoy!
```
flask run
```

In order for search to be usable, you will need to install Elasticsearch. We recommend using [Open Distro for Elasticsearch](https://opendistro.github.io/for-elasticsearch/).
