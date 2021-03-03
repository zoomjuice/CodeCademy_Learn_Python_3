"""
When we call a function in Python, we need to list the arguments to that function to match the order of the
parameters in the function definition. We don’t necessarily need to do this if we pass keyword arguments.

We use keyword arguments by passing arguments to a function with a special syntax that uses the names of the
parameters. This is useful if the function has many optional default arguments or if the order of a function’s
parameters is hard to tell. Here’s an example of a function with a lot of optional arguments.

# Define a function with a bunch of default arguments
def log_message(logging_style="shout", message="", font="Times", date=None):
  if logging_style == 'shout':
    # capitalize the message
    message = message.upper()
  print(message, date)

# Now call the function with keyword arguments
log_message(message="Hello from the past", date="November 20, 1693")

Above we defined log_message(), which can take from 0 to 4 arguments. Since it’s not clear which order the four
arguments might be defined in, we can use the parameter names to call the function. Notice that in our function call
we use this syntax: message="Hello from the past". The key word message here needs to be the name of the parameter we
are trying to pass the argument to.
"""

import shapes


def draw_shape(shape_name="box", character="x", line_breaks=True):
    shape = shapes.draw_shape(shape_name, character)
    if not line_breaks:
        print(shape[1:-1])
    else:
        print(shape)


# call draw_shape() with keyword arguments here:

draw_shape(character='m', line_breaks=False)

"""
shapes.py

BOX_SHAPE = \"""
xxx
x x
xxx
\"""

TRIANGLE_SHAPE = \"""
  x 
 x x
xxxxx
\"""

QUESTION_SHAPE = \"""
  x
 x x
x   x
   x
  x
  x

  x
\"""

def draw_shape(name, char):
  if name == 'box':
    return BOX_SHAPE.replace('x', char)
  elif name == 'triangle':
    return TRIANGLE_SHAPE.replace('x', char)
  else:
    return QUESTION_SHAPE.replace('x', char)
"""
