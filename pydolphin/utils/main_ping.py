import requests
from .get_host import _host


def ping():
    try:
        with requests.get(_host()) as r:
            if r.status_code == 200:
                print("online")
            else:
                print("offline", r.status)
    except Exception as e:
         print("Connection failed.", e)
