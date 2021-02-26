"""
A file can be opened in append mode with the argument 'a'. Append mode will only write your data to the end of a file.
 If you want your file on a new line, you must specify a newline explicitly with '\n'.
"""

with open('cool_dogs.txt', 'a') as cool_dogs_file:
    cool_dogs_file.write('\nAir Buddy')

"""
cool_dogs.txt

Laika
Beethoven
Snoop Doggy
Clifford
Wishbone
"""
