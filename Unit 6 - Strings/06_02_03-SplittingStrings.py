"""
.split() is performed on a string, takes one argument, and returns a list of substrings found between the given
 argument (which in the case of .split() is known as the delimiter). The following syntax should be used:

string_name.split(delimiter)  # Note: $delimiter can be any string

If you do not provide an argument for .split() it will default to splitting at spaces.

For example, consider the following strings:

man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())
# => ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']

.split returned a list with each word in the string. Important to note: if we run .split() on a string with no spaces,
 we will get the same string in return.

When you split a string on a character that it ends with, you’ll end up with an empty string at the end of the list.

print(greatest_guitarist.split('a'))
# => ['s', 'nt', 'n', ' ']

We can also split strings using escape sequences like \n or \t.
"""

# 6.2.3

line_one = "The sky has given over"
line_one_words = line_one.split()
print(line_one_words)

# 6.2.4

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa" \
          ",Kamala Suraiyya,Langston Hughes,Edgar Allen Poe,Adrienne Rich,Nikki Giovanni,Samuel Taylor Coleridge"

author_names = authors.split(',')
print(author_names)

author_last_names = [name.split()[-1] for name in author_names]
print(author_last_names)

# 6.2.5

spring_storm_text = \
    """The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)
