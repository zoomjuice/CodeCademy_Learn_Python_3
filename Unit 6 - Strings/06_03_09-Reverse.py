"""
Write a function named reverse_string that takes a string as a parameter. The function should return word in reverse.
"""

# Write your reverse_string function here:


def reverse_string(string):
    gnirts = ''
    for index in range(1, len(string) + 1):
        gnirts = gnirts + string[-index]
    return gnirts


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# Challenge: Try with list slicing
# Challenge: Try without slicing or range()
