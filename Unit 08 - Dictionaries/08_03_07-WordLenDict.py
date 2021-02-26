"""
Write a function named word_length_dictionary that takes a list of strings named words. The function should return a
 dictionary of key/value pairs where every key is a word in words and every value is the length of that word.
"""

# Write your word_length_dictionary function here:


def word_length_dictionary(words):
    return {word: len(word) for word in words}


# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
