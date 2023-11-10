import random as r
import requests




def collectData():

    ## add the collection stuff code and stuff stuff here.
    attackBoolean = True
    bms_voltage = r.randint(0,12)
    compressorState = False

    data = {'attackBoolean': True, 'bms_voltage': 11.2, 'compressorState': False}
    return data
