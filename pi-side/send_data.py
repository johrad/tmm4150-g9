import requests
from config import serverAddress

localhost = 'http://localhost:8044'

def send(data):      
    
    try:
        response = requests.post(url=f'{serverAddress}/upload', json=data)
        response.raise_for_status()  # Raises HTTPError for bad responses
        print(response)
    except requests.exceptions.RequestException as e:
        print(f"Error sending data: {e}")





