"""
Write a function called unique_english_letters that takes the string word as a parameter. The function should return
 the total number of unique letters in the string. Treat uppercase and lowercase letters as different letters.

We've given you a list of every uppercase and lower case letter in the English alphabet. It will be helpful to include
 that list in your function.
"""

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Write your unique_english_letters function here:


def unique_english_letters(word):
    unique_lst = []
    for letter in word:
        if letter not in unique_lst and letter in letters:
            unique_lst.append(letter)
    return len(unique_lst)


# Uncomment these function calls to test your function:
print(unique_english_letters("misissippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
print(unique_english_letters("misSissIppi"))
# should print 6
print(unique_english_letters("1(Apple)!"))
# should print 4

# Better version - edit: not better


def uniq_letters(word):
    return len(set(word))


# Uncomment these function calls to test your function:
print(uniq_letters("misissippi"))
# should print 4
print(uniq_letters("Apple"))
# should print 4
print(uniq_letters("misSissIppi"))
# should print 6
print(uniq_letters("1(Apple)!"))
# should print 4
