# py_client/basic.py

import requests, json

endpoint = "http://127.0.0.1:8000/songs/api/list_create/"


get_response = requests.get(endpoint)

print(get_response.status_code)
print(get_response.json())
