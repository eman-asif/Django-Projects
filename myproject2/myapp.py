import requests
import json
url = "http://127.0.0.1:8000/stuapi/"

def get_data(id=None):
    params = {}
    if id is not None:
        params = {"id": id}
    response = requests.get(url, params=params)  # Correct way to pass query params
    try:
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not valid JSON:")
        print(response.text)

# get_data()
data = {
    "name": "Emann",
    "age": 21,
    "email": "shifazahid@gmail.com"
}
def post_data(data):


    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

post_data(data)
data = {"id":1, "name": "Shifa Zahid",
    "age": 21}
def update_data(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, data=json.dumps(data), headers=headers)
    try:
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())

    except:
        print(response.text)
# update_data(data) 
data = {"id":2}
def delete_data(data):
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(url, data=json.dumps(data), headers=headers)
    try:
        print("Status Code:", response.status_code)
        print("Response JSON:", response.json())

    except:
        print(response.text)
# delete_data(data)