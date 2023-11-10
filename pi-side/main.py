from time import sleep
import collectData
import send_data


while True:
    send_data.send(collectData.collectData()) # CollectData() returns data in json

    sleep(2)