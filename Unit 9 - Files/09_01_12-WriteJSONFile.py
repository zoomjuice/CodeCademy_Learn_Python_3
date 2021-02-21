"""
We can use the json library to translate Python objects to JSON as well. This is especially useful in instances where
you’re using a Python library to serve web pages, you would also be able to serve JSON. Let’s say we had a Python
dictionary we wanted to save as a JSON file:

turn_to_json = { 'eventId': 674189, 'dateTime': '2015-02-12T09:23:17.511Z', 'chocolate': 'Semi-sweet Dark',
                'isTomatoAFruit': True }

We’d be able to create a JSON file with that information by doing the following:

import json

with open('output.json', 'w') as json_file:
    json.dump(turn_to_json, json_file)

We import the json module, open up a write-mode file under the variable json_file, and then use the json.dump() method
to write to the file. json.dump() takes two arguments: first the data object, then the file object you want to save.
"""

import json

data_payload = {
    'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
    'follow up': 'But enough talk!'
}

with open('data.json', 'w') as data_json:
    json.dump(data_payload, data_json)

print(data_json)
