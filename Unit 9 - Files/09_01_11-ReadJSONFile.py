"""
Python has a built-in library to read and write JSON (JavaScript Object Notation) files. JSON is a file format inspired
by the programming language JavaScript.

JSON's format is similar to Python dictionary syntax, so JSON files might be easy to read from a Python developer
standpoint. Python comes with a json package that will help us parse JSON files into dictionaries. Suppose we have a
JSON file like the following:

purchase_14781239.json
{
  'user': 'ellen_greg',
  'action': 'purchase',
  'item_id': '14781239'
}

We would be able to read that in as a Python dictionary with the following code:

import json
with open('purchase_14781239.json') as purchase_json:
    purchase_data = json.load(purchase_json)

print(purchase_data['user']) # Prints 'ellen_greg'

First we import the json package, then open the file as 'purchase_json' in read mode (by default).

We continue by parsing purchase_json using json.load(), creating a Python dictionary out of the file so we can interact
with it. We print one of the values of the JSON file by keying into the purchase_data object.
"""

import json

with open('message.json') as message_json:
    message = json.load(message_json)

print(message)
print(message['text'])

"""
message.json

{
  "text": "Now that's JSON!",
  "secret text": "Now that's some _serious_ JSON!"
}
"""
