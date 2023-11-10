import requests

data = {
    'attackBoolean': 1,
    'battery_percentage': 90,
    'compressorBoolean': 0
}

response = requests.post('http://localhost:8044/upload', json=data)

if response.status_code == 200:
    print("Success! Received HTML response:")
else:
    print(f"HTTP request failed with status code {response.status_code}")