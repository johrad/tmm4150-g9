import requests
from config import serverAddress


def send(data):      
    localhost = 'http://localhost:8044'

    
    # Send the POST request object and receive the response
    response = requests.post(url=f'{serverAddress}/upload', json=data)
    print(response)   





