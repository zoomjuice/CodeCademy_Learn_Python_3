"""
So if we can’t use a list as a default argument for a function, what can we use? If we want an empty list,
we can use None as a special value to indicate we did not receive anything. After we check whether an argument was
provided we can instantiate a new list if it wasn’t.

def add_author(authors_books, current_books=None):
  if current_books is None:
    current_books = []

  current_books.extend(authors_books)
  return current_books

In the above function, we accept current_books a value expected to be a list. But we don’t require it. If someone
calls add_author() without giving an argument for current_books, we supply an empty list. This way multiple calls to
add_author won’t include data from previous calls to add_author.
"""


def update_order(new_item, current_order=None):
    if current_order is None:
        current_order = []
    current_order.append(new_item)
    return current_order


# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2)
