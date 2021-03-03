"""
Python doesn’t stop at allowing us to accept unlimited positional parameters, it gives us the power to define
functions with unlimited keyword parameters too. The syntax is very similar, but uses two asterisks (**) instead of
one. Instead of args, we call this kwargs — as a shorthand for keyword arguments.

def arbitrary_keyword_args(**kwargs):
  print(type(kwargs))
  print(kwargs)
  # See if there's an "anything_goes" keyword arg
  # and print it
  print(kwargs.get('anything_goes'))

arbitrary_keyword_args(this_arg="wowzers", anything_goes=101)
# Prints "<class 'dict'>
# Prints "{'this_arg': 'wowzers', 'anything_goes': 101}"
# Prints "101"

As you can see, **kwargs gives us a dictionary with all the keyword arguments that were passed to
arbitrary_keyword_args. We can access these arguments using standard dictionary methods.

Since we’re not sure whether a keyword argument will exist, it’s probably best to use the dictionary’s .get() method
to safely retrieve the keyword argument. Do you remember what .get() returns if the key is not in the dictionary?
It’s None!
"""

# Checkpoint 1
print("My name is {name} and I'm feeling {feeling}.".format(name='Cat', feeling='fine, I guess'))

# Checkpoint 2
from products import create_product


# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict):
    for name, price in products_dict.items():
        create_product(name, price)


# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(Baseball='3', Shirt='14', Guitar='70')

"""
products.py

def create_product(name, price):
  print("{} created, being sold for ${}".format(name, price))
"""
