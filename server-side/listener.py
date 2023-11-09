import json
from time import sleep

filepath = "/home/data/data.json"


while True:
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        print(data, end='\r')
    
    except FileNotFoundError: # ignore if no data file present
        pass
    except Exception as e:
        print("ERROR!!:" e)

    sleep(0.5)