"""
A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is
 made when someone says “Belly Jeans” instead of “Jelly Beans”.

Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding the first
 syllable of a word is a difficult task, so for our function, we’re going to switch the first letters of each word.
 Return the two new words as a single string separated by a space.
"""

# Write your make_spoonerism function here:


def make_spoonerism(word1, word2):
    return word2[0] + word1[1:] + ' ' + word1[0] + word2[1:]


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
