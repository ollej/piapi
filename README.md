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
