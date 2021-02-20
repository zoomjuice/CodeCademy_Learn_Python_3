"""
Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return
 the key associated with the largest value in the dictionary.
"""

# Write your max_key function here:


def max_key(my_dict):
    val_max = next(iter(my_dict.values()))
    key_max = next(iter(my_dict.keys()))
    for key, value in my_dict.items():
        if value > val_max:
            val_max = value
            key_max = key
    return key_max


# Uncomment these function calls to test your  function:
print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"
