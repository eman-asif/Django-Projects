import requests
import json

url = "http://127.0.0.1:8000/stuapi/"
data = {
    "name": "Eman Asif",
    "age": 21,
    "email": "eman@gmail.com"
}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
