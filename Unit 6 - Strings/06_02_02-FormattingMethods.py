"""
There are three string methods that can change the casing of a string. These are .lower(), .upper(), and .title().

    .lower() returns the string with all lowercase characters.
    .upper() returns the string with all uppercase characters.
    .title() returns the string in title case, which means the first letter of each word is capitalized.

It's important to remember that string methods can only create new strings, they do not change the original string.
"""

poem_title = "spring storm"
poem_author = "William Carlos Williams"


def format_title(string):
    return string.title()


def format_author(string):
    return string.upper()


poem_title_fixed = format_title(poem_title)
poem_author_fixed = format_author(poem_author)

print(poem_title)
print(poem_title_fixed)
print(poem_author)
print(poem_author_fixed)
