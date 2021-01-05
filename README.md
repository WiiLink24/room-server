# room-server
## What is this?
room-server provides a server usable with [Wii no Ma](https://en.wikipedia.org/wiki/Wii_no_Ma).

## Running
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