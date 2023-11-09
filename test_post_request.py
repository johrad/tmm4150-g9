import requests

data = {
    'pressure': 0,
    'battery_percentage': 95,
    'attacks': 3
}

response = requests.post('http://localhost:8044/upload', json=data)

if response.status_code == 200:
    print("Success! Received HTML response:")
else:
    print(f"HTTP request failed with status code {response.status_code}")