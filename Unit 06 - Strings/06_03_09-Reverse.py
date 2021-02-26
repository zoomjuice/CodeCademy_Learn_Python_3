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


def gnirts_esrever(string):
    return string[::-1]


# Uncomment these function calls to test your  function:
print(gnirts_esrever("Codecademy"))
# should print ymedacedoC
print(gnirts_esrever("Hello world!"))
# should print !dlrow olleH
print(gnirts_esrever(""))
# should print


# Challenge: Try without slicing or range()


def reverser(string):
    string_reversed = ''
    for letter in string:
        string_reversed = letter + string_reversed
    return string_reversed


# Uncomment these function calls to test your  function:
print(reverser("Codecademy"))
# should print ymedacedoC
print(reverser("Hello world!"))
# should print !dlrow olleH
print(reverser(""))
# should print
