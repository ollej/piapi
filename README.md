# piapi
REST API wrapper for the Raspberry Pi scrollphat API.


Installation
------------

```
$ virtualenv -p python3 .venv
$ pip3 install -r requirements.txt
$ source .venv/bin/activate
```

### Setup database

```
$ python3
> from piqueue import piqueue
> piqueue.create_database()
```
