# Thanks to using 

------

the project is to re-build the weibo / twitter platform with a delete forbirdden feature based on neo Blocking Chain.No one expecially the gov the can delete our post any more.


Coding based on 
https://github.com/CityOfZion/neo-python/


Here is some api for this system

> * getLastBlog
> * getLastBlogBySender
> * getLastBlogByTag

## Getting started

nodelpost has two System dependencies (everything else is covered with `pip`):

- [LevelDB](https://github.com/google/leveldb)
- [Python 3.6+](https://www.python.org/downloads/release/python-364/) (3.5 and below is not supported)

#### Centos/Redhat/Fedora

```
# Install Python 3.6:
yum install -y centos-release-scl
yum install -y rh-python36
scl enable rh-python36 bash

# Install dependencies:
yum install -y epel-release
yum install -y readline-devel leveldb-devel libffi-devel gcc-c++ redhat-rpm-config gcc python-devel openssl-devel
```


### Python 3.6

neo-python is compatible with **Python 3.6 and later**.

On *nix systems, install Python 3.6 via your package manager, or download an installation package
from the [official homepage](https://www.python.org/downloads/release/python-364/).

### Virtual Environment

It is recommended to put all project dependencies into its own virtual environment,
this way we don't pollute the global installation which could lead to version conflicts.

```
python3.6 -m venv venv
source venv/bin/activate
```

Now let's install neo-python's dependencies:

```
pip install -U setuptools pip wheel
pip install -e .
```


###Start API Server
```
python api-server.py  -p --port-rpc 10332 --port-rest 9090
```

-------------------


Example:

###getLastBlogBySender
Post Params
```
{
  "jsonrpc": "2.0",
  "method": "getLastBlogBySender",
  "params": ["AZCeVJgrLDsAUUtms9suq5KK9miNQo1Wd5"],
  "id": 1
}
```
----
Data Return
```
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "height": 1,
        "list": [
            {
                "sender": "AZCeVJgrLDsAUUtms9suq5KK9miNQo1Wd5",
                "type": {
                    "usage": 240,
                    "data": "23424c4f472349206c6f7665206e6f2064656c20706f7374"
                },
                "content": "#BLOG#I love no del post",
                "time": 1520693799
            }
        ]
    }
}
```


### getLastBlogByTag
Post Params
```
 {
  "jsonrpc": "2.0",
  "method": "getLastBlogByTag",
  "params": ["#BLOG#"],
  "id": 1
}
```
------
Data Return
```
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "height": 1,
        "list": [
            {
                "sender": "AZCeVJgrLDsAUUtms9suq5KK9miNQo1Wd5",
                "type": {
                    "usage": 240,
                    "data": "23424c4f472349206c6f7665206e6f2064656c20706f7374"
                },
                "content": "#BLOG#I love no del post",
                "time": 1520693799
            }
        ]
    }
}
```


###getLastBlog
Post Params
```
{
  "jsonrpc": "2.0",
  "method": "getLastBlog",
  "params": [],
  "id": 1
}
```
----
Data Return
```
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "height": 1,
        "list": [
            {
                "sender": "AZCeVJgrLDsAUUtms9suq5KK9miNQo1Wd5",
                "type": {
                    "usage": 240,
                    "data": "23424c4f472349206c6f7665206e6f2064656c20706f7374"
                },
                "content": "#BLOG#I love no del post",
                "time": 1520693799
            }
        ]
    }
}




