"""
Not only can we accept arbitrarily many parameters to a function in our definition, but Python also supports a
syntax that makes deconstructing any data that you have on hand to feed into a function that accepts these kinds of
unpacked arguments. The syntax is very similar, but is used when a function is called, not when it’s defined.

def takes_many_args(*args):
  print(','.join(args))

long_list_of_args = [145, "Mexico City", 10.9, "85C"]

# We can use the asterisk "*" to deconstruct the container.
# This makes it so that instead of a list, a series of four different
# positional arguments are passed to the function
takes_many_args(*long_list_of_args)
# Prints "145,Mexico City,10.9,85C"

We can use the * when calling the function that takes a series of positional parameters to unwrap a list or a tuple.
This makes it easy to provide a sequence of arguments to a function even if that function doesn’t take a list as an
argument. Similarly we can use ** to destructure a dictionary.

def pour_from_sink(temperature="Warm", flow="Medium")
  set_temperature(temperature)
  set_flow(flow)
  open_sink()

# Our function takes two keyword arguments
# If we make a dictionary with their parameter names...
sink_open_kwargs = {
  'temperature': 'Hot',
  'flow': "Slight",
}

# We can destructure them an pass to the function
pour_from_sink(**sink_open_kwargs)
# Equivalent to the following:
# pour_from_sink(temperature="Hot", flow="Slight")

So we can also use dictionaries and pass them into functions as keyword arguments with that syntax. Notice that our
pour_from_sink() function doesn’t even accept arbitrary **kwargs. We can use this destructuring syntax even when the
function has a specific number of keyword or positional arguments it accepts. We just need to be careful that the
object we’re destructuring matches the length (and names, if a dictionary) of the signature of the function we’re
passing it into.
"""

from products import create_product


def create_products(**products_dict):
    for name, price in products_dict.items():
        create_product(name, price)


new_product_dict = {'Apple': 1, 'Ice Cream': 3, 'Chocolate': 5}

create_products(**new_product_dict)
