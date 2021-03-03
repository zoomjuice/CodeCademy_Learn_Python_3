"""
Python’s functions offer us a very expressive syntax. We’re going to look into some of the finer details of how
functions in Python work and some techniques we can use to be more intuitive while writing and calling functions.

First, let’s consider some definitions:

    A parameter is a variable in the definition of a function.
    An argument is the value being passed into a function call.
    A function definition begins with def and contains the entire following indented block.
    And function calls are the places a function is invoked, with parentheses, after its definition

Let’s see this in a block of code:

# The "def" keyword is the start of a function definition
def function_name(parameter1, parameter2):
  # The placeholder variables used inside a function definition are called parameters
  print(parameter1)
  return parameter2
# The outdent signals the end of the function definition

# "Arguments" are the values passed into a function call
argument1 = "argument 1"
argument2 = "argument 2"

# A function call uses the functions name with a pair of parentheses
# and can return a value
return_val = function_name(argument1, argument2)

In the above code we defined the function function_name that takes two parameters, parameter1 and parameter2. We then
create two variables with the values "argument 1" and "argument 2" and proceed to call function_name with the two
arguments.

Some of this terminology can be used inconsistently between schools, people, and businesses. Some people don’t
differentiate between “parameter” and “argument” when speaking. It’s useful here because we’re going to be looking at
a lot of behavior that looks very similar in a function definition and a function call, but will be subtly different.
But the distinction is sometimes unnecessary, so don’t get too hung up if something is called a “parameter” that
should be an “argument” or vice versa.
"""

from record_library import place_record, rotate_record, drop_needle

def play_record(album):
  place_record(album)
  rotate_record(album)
  drop_needle(album)

next_album = "Blondie / Parallel Lines"

play_record(next_album)

"""
record_library.py

def place_record(album):
    return


def rotate_record(album):
    return


def drop_needle(album):
    print("Playing album {}".format(album))
"""