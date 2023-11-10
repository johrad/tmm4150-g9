import requests

# Set the body of the POST request
data = {'attackBoolean': 1, 'battery_percentage': 11.2, 'compressorState': 0}

url1 = "http://199.247.7.163:8044/upload"
url2 = 'http://localhost:8044/upload'
# Send the POST request object and receive the response
response = requests.post(url=url1, json=data)
print(response) 