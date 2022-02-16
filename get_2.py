import requests

# we will use JSONPlaceholder to test our API, its a free service which provides fake API endpoint
API_ENDPOINT = "https://jsonplaceholder.typicode.com/todos/1"

## GET

response = requests.get(API_ENDPOINT)
print(response.json())
print(response.status_code)
print(response.headers['content-type'])

## POST

API_ENDPOINT = "https://jsonplaceholder.typicode.com/todos"

todo = {
    "userId": 1,
    "title": "Updated Title",
    "completed": True
}

# method 1
response = requests.post(API_ENDPOINT, json=todo)
print(response.json())
print(response.status_code)

# method 2 - using headers
import json
headers = {'Content-type': 'application/json'}
response = requests.post(API_ENDPOINT, data=json.dumps(todo), headers=headers)
print(response.json())
print(response.status_code)

## PUT

# we will specify a particular entry to be updated
API_ENDPOINT = "https://jsonplaceholder.typicode.com/todos/5"

todo_updated = {
    "userId": 1,
    "title": "Updated Title 2.0",
    "completed": True
}

response = requests.put(API_ENDPOINT, json=todo_updated)
print(response.json())
print(response.status_code)

## PATCH

