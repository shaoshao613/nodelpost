usage



 python api-server.py  -p --port-rpc 10332 --port-rest 9090

Example:

getLastBlogBySender


{
  "jsonrpc": "2.0",
  "method": "getLastBlogBySender",
  "params": ["AZCeVJgrLDsAUUtms9suq5KK9miNQo1Wd5"],
  "id": 1
}

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


getLastBlogByTag

{
  "jsonrpc": "2.0",
  "method": "getLastBlogByTag",
  "params": ["#BLOG#"],
  "id": 1
}


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

getLastBlog


{
  "jsonrpc": "2.0",
  "method": "getLastBlog",
  "params": [],
  "id": 1
}


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


demo 
www.sotapit.com/nodelpost


