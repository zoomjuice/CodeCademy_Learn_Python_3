"""
Python equips us with many different ways to store data. A float is a different kind of number from an int, and we store
different data in a list than we do in a dict. These are known as different types. We can check the type of a Python
variable using the type() function.

a_string = "Cool String"
an_int = 12
print(type(a_string))  # prints "<class 'str'>"
print(type(an_int))  # prints "<class 'int'>"

Above, we defined two variables, and checked the type of these two variables. A variable's type determines what you
can do with it and how you can use it. You can't .get() something from an integer, just as you can't add two
dictionaries together using +. This is because those operations are defined at the type level.
"""

my_dict = {}
my_list = []

print(type(5))
print(type(my_dict))
print(type(my_list))
