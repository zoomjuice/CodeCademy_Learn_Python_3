"""
There's an even easier way than iterating through the entire string to determine if a character is in a string. We can
 do this type of check more efficiently using in. in checks if one string is part of another string.

Here is what the syntax of in looks like:

letter in word

Here, letter in word is a boolean expression that is True if the string letter is in the string word.

Here are some examples:

print("e" in "blueberry")
# => True
print("blue" in "blueberry")
# => True
print("a" in "blueberry")
# => False
"""


def contains(big_str, small_str):
    return small_str in big_str


print(contains("watermelon", "melon"))  # True
print(contains("watermelon", "berry"))  # False


def common_letters(str_one, str_two):
    common = []
    for letter in str_one:
        if letter in str_two and letter not in common:
            common.append(letter)
    return common


print(common_letters('manhattan', 'san francisco'))


# def same_letters(str_one, str_two):
#     return [letter for letter in str_one if letter in str_two and letter not in locals()['_[1]'].__self__]


# print(same_letters('manhattan', 'san francisco'))
