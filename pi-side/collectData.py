import random as r
import requests




def collectData():

    ## add the collection stuff code and stuff stuff here.
    attackBoolean = r.randint(0,1)
    bms_voltage = r.randint(0,12)
    compressorState = r.randint(0,1)

    data = {'attackBoolean': True, 'bms_voltage': 11.2, 'compressorState': False}
    return data
