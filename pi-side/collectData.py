import random as r
import json



def collectData(filepath):

    currentPressure = r.randint(0,200)
    currentBMSvoltage = r.randint(0,12)

    # put data into json file:
    data = { 
    "timestamp": "test data2",
    "pressure": currentPressure,
    "bms-voltage": currentBMSvoltage
    }

    with open(filepath, "w") as f:
        f.write(json.dumps(data))



