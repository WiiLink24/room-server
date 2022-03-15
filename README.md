# room-server
[![Build](https://github.com/WiiLink24/room-server/actions/workflows/push_docker_image.yml/badge.svg)](https://github.com/WiiLink24/room-server/actions/workflows/push_docker_image.yml)
## What is this?
room-server provides a server usable with [Wii no Ma](https://en.wikipedia.org/wiki/Wii_no_Ma).

## Running
1. You'll most likely want to [create a virtualenv](https://docs.python.org/3/library/venv.html) to install things. For example:
```
python3 -m venv virtualenv
```
Ensure you active the environment.

2. Regardless of the above, ensure you have installed requirements:
```
pip3 install -r requirements.txt
# Useful for reading .flaskenv.
pip3 install python-dotenv
```

3. You'll then need to install PostgreSQL. Copy `config-example.py` to `config.py` and update this config.
4. Read `conf/README.md` for instructions of static files you should provide.
5. Finally, start the server:
```
flask run
```
6. You will now be able to visit The Underground (http://root_domain/theunderground). The default username is `admin`, and password `admin`.
It's highly advised to change it as soon as possible.