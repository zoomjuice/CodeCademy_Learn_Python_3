"""
When working with strings from real data, the strings often aren’t clean. You’ll find lots of extra whitespace,
 unnecessary linebreaks, and rogue tabs.

Python provides a method for cleaning strings: .strip(). Stripping a string removes all whitespace characters from the
 beginning and end. Consider the following example:

featuring = "           rob thomas                 "
print(featuring.strip())
# => 'rob thomas'

You can also use .strip() with a character argument, which will strip that character from either end of the string.

featuring = "!!!rob thomas       !!!!!"
print(featuring.strip('!'))
# => 'rob thomas       '

By including the argument '!' we are able to strip all of the ! characters from either side of the string. Notice that
 now that we’ve included an argument we are no longer stripping whitespace, we are ONLY stripping the argument.
"""

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms',
                    '           like flowering mines    ', '\n', '   to conquer me home.    ']

love_maybe_lines_stripped = [line.strip() for line in love_maybe_lines]
print(love_maybe_lines_stripped)

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)
