import json
from time import sleep

filepath = "/home/data/data.json"


while True:
    with open(filepath, "r") as f:
        data = json.load(f)

    print(data)
    sleep(0.2)