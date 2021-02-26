"""
We saw that we can avoid KeyErrors by checking if a key is in a dictionary. Another method is a try/except:

key_to_check = "Landmark 81"
try:
  print(building_heights[key_to_check])
except KeyError:
  print("That key doesn't exist!")

If we try to access a nonexistent key, the program will go into the except block and print "That key doesn't exist!".
"""

caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
# caffeine_level.update({"matcha": 30})

try:
    print(caffeine_level['matcha'])
except:
    print('Unknown caffeine level')
