"""
If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}  # sensors object from previous exercise

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})  # Add 3 new rooms

This would add all three items to the sensors dictionary, so sensors now looks like this:

{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}
"""

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({'theLooper': 138475, 'stringQueen': 85739})

print(user_ids)
