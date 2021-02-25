"""
In this lesson, we learned more complicated relationships between classes. We learned:

    How to create a subclass of an existing class.
    How to redefine existing methods of a parent class in a subclass by overriding them.
    How to leverage a parent class’s methods in the body of a subclass method using the super() function.
    How to define a Python exception that inherits from Exception.
    How to write programs that are flexible using interfaces and polymorphism.
    How to write data types that look and feel like native data types with dunder methods.

These are really complicated concepts! It’s a long journey to get to the state of comfortably being able to build
class hierarchies that embody the concerns that your software will need to. Give yourself a pat on the back,
you earned it!
"""


class SortedList(list):
    def __init__(self):
        super().__init__()
        self.sort()

    def append(self, value):
        super().append(value)
        sorted_self = self.sort()
        return sorted_self
