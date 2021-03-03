"""
What does a function return when it doesn’t return anything? This sounds like a riddle, but there is a correct
answer. A Python function that does not have any explicit return statement will return None after completing. This
means that all functions in Python return something, whether it’s explicit or not. For example:

def no_return():
  print("You've hit the point of no return")
  # notice no return statement

here_it_is = no_return()

print(here_it_is)
# Prints out "None"

Above we defined a function called no_return() and saved the result to a variable here_it_is. When we print() the
value of here_it_is we get None, referring to Python’s None. It’s possible to make this syntax even more explicit — a
return statement without any value returns None also.

def fifty_percent_off(item):
  # Check if item.cost exists
  if hasattr(item, 'cost'):
    return item.cost / 2

  # If not, return None
  return

sale_price = fifty_percent_off(product)

if sale_price is None:
  print("This product is not for sale!")

Here we have implemented a function that returns the cost of a product with “50% Off” (or “half price”). We check if
the item passed to our function has a cost attribute. If it exists, we return half the cost. If not,
we simply return, which returns None.

When we plug a product into this function, we can expect two possibilities: the first is that the item has a cost and
this function returns half of that. The other is that item does not have a listed cost and so the function returns
None. We can put error handling in the rest of our code, if we get None back from this function that means whatever
we’re looking at isn’t for sale!
"""

# store the result of this print() statement in the variable prints_return
prints_return = print("What does this print function return?")

# print out the value of prints_return

print(prints_return)

# call sort_this_list.sort() and save that in list_sort_return
sort_this_list = [14, 631, 4, 51358, 50000000]
list_sort_return = sort_this_list.sort()

# print out the value of list_sort_return

print(list_sort_return)

