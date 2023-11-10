import requests
from config import serverAddress


def send(data):  
    data = {'attackBoolean': True, 'bms_voltage': 11.2, 'compressorState': False}

    serverAddress = "http://199.247.7.163:8055"
    localhost = 'http://localhost:8044'
    # Send the POST request object and receive the response
    response = requests.post(url=f'{serverAddress}/upload', json=data)
    print(response)   





