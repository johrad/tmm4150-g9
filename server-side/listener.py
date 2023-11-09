import json
from time import sleep

filepath = "/home/data/data.json"


while True:
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
    except Exception as e:
        print(e)
    pass
    print(data, end='\r')
    sleep(0.2)