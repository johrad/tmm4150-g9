import json
from time import sleep

import requests

filepath = "/home/data/data.json"


while True:
    try:
        with open(filepath, "r") as f:
            data = json.load(f)

        response = requests.post('http://localhost:8044/upload', json=data)

        if response.status_code == 200:
            print("Success! Received HTML response:")
        else:
            print(f"HTTP request failed with status code {response.status_code}")
        print(data, end='\r')
    
    except FileNotFoundError: # ignore if no data file present
        pass
    except Exception as e:
        print("ERROR!!:", e)

    sleep(0.5)


