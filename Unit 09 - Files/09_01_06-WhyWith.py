"""
The "with" keyword invokes something called a context manager for the file that we're calling open() on. This context
manager takes care of opening the file when we call open() and then closing the file after we leave the indented block.

Since your files exist outside your Python script, we need to tell Python when we're done with them so that it can
close the connection to that file. Leaving a file connection open unnecessarily can impact other programs on your
computer that might be trying to access that file.

The with syntax replaces older ways to access files where you need to call .close() on the file object manually. We can
still open a file with the old syntax, as long as we remember to close the file connection afterwards.

fun_cities_file = open('fun_cities.txt', 'a') # We can now append a line to "fun_cities".
fun_cities_file.write("Montréal") # But we need to remember to close the file fun_cities_file.close()

In the above script we added “Montréal” as a new line in our file fun_cities.txt. However, with the older-style
syntax, we had to close the file afterwards. Since this is more verbose (requires at least one more line of code)
without being any more expressive, using with is preferred.
"""

close_this_file = open('fun_file.txt')

setup = close_this_file.readline()
punchline = close_this_file.readline()

close_this_file.close()

print(setup)
print(punchline)
