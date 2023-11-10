import random as r
import requests




def collectData():

    ## add the collection stuff code and stuff stuff here.
    attackBoolean = r.randint(0,1)
    battery_percentage = r.randint(0,12)
    compressorState = r.randint(0,1)

    data = {'attackBoolean': True, 'battery_percentage': battery_percentage, 'compressorState': False}
    return data
