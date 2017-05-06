# piapi
REST API wrapper for the Raspberry Pi scrollphat API.


Installation
------------

```
$ virtualenv --system-site-packages -p python3 .venv
$ source .venv/bin/activate
$ pip3 install --upgrade -r requirements.txt
```

### Setup database

```
$ python3
> from piqueue import piqueue
> piqueue.create_database()
```

### Start piapi.py

```
$ FLASK_APP=piapi.py python3 -m flask run --host=0.0.0.0
```

### Default configuration

Create a file called `.env` with the following options:

```
MONIT_URL=https://mmonit.example.com
MONIT_USERNAME=username
MONIT_PASSWORD=password
MUSIC_PATH=/home/pi/music
MUSIC_EXTENSION=.mp3
```

Requirements
------------

Install requirements for jobs:

```
$ sudo apt-get install fortune mpg321
```
