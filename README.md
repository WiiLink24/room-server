# room-server
You'll most likely want to [create a virtualenv](https://docs.python.org/3/library/venv.html) to install things. For example:
```
python3 -m venv virtualenv
```
Ensure you active the environment.

From there, install requirements:
```
pip3 install -r requirements.txt
# Useful for reading .flaskenv.
pip3 install python-dotenv
```

You'll then need to install PostgreSQL. Copy `config-example.py` to `config.py` and update this config.

Finally, run in development mode.
```
flask run
```