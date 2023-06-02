# py_client/basic.py

import requests, json

endpoint = "http://127.0.0.1:8000/songs/api/list_create/"


data = {'title': 'Malakia', 
        }

get_response = requests.post(endpoint, json=data)

print(get_response.status_code)

