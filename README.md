# room-server
[![Build](https://github.com/WiiLink24/room-server/actions/workflows/push_docker_image.yml/badge.svg)](https://github.com/WiiLink24/room-server/actions/workflows/push_docker_image.yml)
## What is this?
room-server provides a server usable with [Wii no Ma](https://en.wikipedia.org/wiki/Wii_no_Ma).

## Running
1. You'll most likely want to [create a virtualenv](https://docs.python.org/3/library/venv.html) to install things. For example:
```
python3 -m venv virtualenv
```
Ensure you activate the environment.

2. Regardless of the above, ensure you have installed requirements:
```
pip3 install -r requirements.txt
# Useful for reading .flaskenv.
pip3 install python-dotenv
```
Note: If psycopg2 fails to install on a Debian based distro (i.e. Ubuntu or Linux Mint), install these packages and try again.
```
libpq-dev python3-dev
```
If you use an RHEL based distro (i.e. CentOS/Fedora), install these dependencies:
```
libpq-devel python3-devel
```
3. You'll then need to install [PostgreSQL](https://www.postgresql.org/download/). Refer to the database entry in the [room-server wiki](https://github.com/WiiLink24/room-server/wiki/Database-Setup) for more detailed download instructions.
4. Copy `config-example.py` to `config.py` and update this config.
5. Read `conf/README.md` for instructions of static files you should provide.
6. Finally, start the server:
```
flask run -h 0.0.0.0 -p 80
```
6. Before launching Wii no Ma, you will need to visit The Underground (http://root_domain/theunderground) to set up the database. 
The default username is `admin`, and password `admin`. It's highly advised to change it as soon as possible.

7. Refer to the [room-server wiki](https://github.com/WiiLink24/room-server/wiki) for further instructions on set up.
