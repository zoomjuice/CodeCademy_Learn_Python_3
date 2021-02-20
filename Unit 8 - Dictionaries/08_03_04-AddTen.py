"""
Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The
 function should add 10 to every value in my_dictionary and return my_dictionary
"""

# Write your add_ten function here:


def add_ten(my_dict):
    return {key: value + 10 for key, value in my_dict.items()}


# Uncomment these function calls to test your  function:
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}
