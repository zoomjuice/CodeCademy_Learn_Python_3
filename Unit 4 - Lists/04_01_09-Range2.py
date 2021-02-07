# range() can be called with a different starting point
list1 = range(5, 15)  # Creates a range object from 5 to 14
print(list(list1))

# range() can also produce a range with different sized steps between each element
list2 = range(0, 40, 5)  # Creates a range object with 0, 5, 10, etc.
print(list(list2))
