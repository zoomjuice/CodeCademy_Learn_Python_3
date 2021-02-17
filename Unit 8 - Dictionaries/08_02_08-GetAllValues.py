"""
Dictionaries have a .values() method that returns a dict_values object (just like a dict_keys object but for values!)
 with all of the values in the dictionary. It can be used in the place of a list for iteration:

There is no built-in function to get all of the values as a list, but if you really want to, you can use:

list(test_scores.values())

However, for most purposes, the dict_list object will act the way you want a list to act.
"""

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18,
                 "dictionaries": 18}

total_exercises = 0

for value in num_exercises.values():
    total_exercises += value

print(total_exercises)
