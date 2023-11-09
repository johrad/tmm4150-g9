from time import sleep
import collectData
import send_data

jsonPath = "pi-side/data.json"


while True:
    collectData.collectData(filepath=jsonPath) # collects data and writes to .json
    send_data.send(filepath=jsonPath)

    sleep(2)