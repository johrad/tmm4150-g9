import requests

# Set the body of the POST request
data = {'attackBoolean': True, 'bms_voltage': 11.2, 'compressorState': False}

url1 = "http://199.247.7.163:8055/upload"
url2 = 'http://localhost:8044/upload'
# Send the POST request object and receive the response
response = requests.post(url=url1, json=data)
print(response)