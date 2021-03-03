"""
When writing a function with default arguments, it can be tempting to include an empty list as a default argument
to that function. Let’s say you have a function called populate_list that has two required arguments, but it’s easy
to see that we might want to give it some default arguments in case we don’t have either list_to_populate or length
every time. So we’d give it these defaults:

def populate_list(list_to_populate=[], length=1):
  for num in range(length):
    list_to_populate.append(num)
  return list_to_populate

It’s reasonable to believe that list_to_populate will be given an empty list every time it’s called. This isn’t the
case! list_to_populate will be given a new list once, in its definition, and all subsequent function calls will
modify the same list. This will happen:

returned_list = populate_list(length=4)
print(returned_list)
# Prints [0, 1, 2, 3] -- this is expected

returned_list = populate_list(length=6)
print(returned_list)
# Prints [0, 1, 2, 3, 0, 1, 2, 3, 4, 5] -- this is a surprise!

When we call populate_list a second time we’d expect the list [0, 1, 2, 3, 4, 5]. But the same list is used both
times the function is called, causing some side-effects from the first function call to creep into the second. This
is because a list is a mutable object.

A mutable object refers to various data structures in Python that are intended to be mutated, or changed. A list has
append and remove operations that change the nature of a list. Sets and dictionaries are two other mutable objects in
Python.

It might be helpful to note some of the objects in Python that are not mutable (and therefore OK to use as default
arguments). int, float, and other numbers can’t be mutated (arithmetic operations will return a new number). tuples
are a kind of immutable list. Strings are also immutable — operations that update a string will all return a
completely new string.
"""


def update_order(new_item, current_order=[]):
    current_order.append(new_item)
    return current_order


# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2)
