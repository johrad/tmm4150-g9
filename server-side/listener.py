import json
from time import sleep

filepath = "/home/data/data.json"


while True:
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
        print(data, end='\r')
    
    except Exception as e: # ignore if no data file present
        print(e)
    
    pass
    

    sleep(0.2)