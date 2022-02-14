import json
import requests
import urllib.parse

# reading the JSON file
with open('volunteer_data.json', 'r') as text_file_input:
    data = text_file_input.read()

# load the file as a JSON object
obj = jsons.load(data)

API_ENDPOINT = 'https://registeredvolunteers.xyz.com/volunteer/{}/badge/{}' # some random endpoint

# we will pass on the required data (bolunteer id and badge id) to the API endpoint

for i in obj:
    r = requests.get(API_ENDPOINT.format(urllib.parse.quote(i['volunteerID']), i['badgeID']))

    print(r.text)

text_file_input.close()

r.json()
r.status_code
r.reason

