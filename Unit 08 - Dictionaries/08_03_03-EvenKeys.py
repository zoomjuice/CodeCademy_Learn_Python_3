"""
Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values,
 as a parameter. This function should return the sum of the values of all even keys.
"""

# Write your sum_even_keys function here:


def sum_even_keys(my_dict):
    total = 0
    for key, value in my_dict.items():
        if key % 2 == 0:
            total += value
    return total


# Uncomment these function calls to test your  function:
print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6
