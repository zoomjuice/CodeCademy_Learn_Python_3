"""
One of the first things we learn as programmers is how to print out information that we need for debugging.
Unfortunately, when we print out an object we get a default representation that seems fairly useless.

class Employee():
    pass

argus = Employee()
print(argus)
# prints "<__main__.Employee object at 0x104e88390>"

This default string representation gives some information, like where the class is defined and the memory address
where this object is stored, but is usually not useful information to have when we are trying to debug our code.

The dunder method __repr__() is a method we can use to tell Python what we want the string representation of the class
to be. __repr__() can only have one parameter, self, and must return a string.

In our Employee class below, we have an instance variable called name that should be unique enough to be useful when
we’re printing out an instance of the Employee class.

class Employee():
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name

argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"

We implemented the __repr__() method and had it return the .name attribute of the object. When we printed the object
out it simply printed the .name of the object! Cool!
"""


class Circle:

    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2

    def __repr__(self):
        return 'Circle with radius {}'.format(self.radius)

    def area(self):
        return self.pi * self.radius ** 2

    def circumference(self):
        return self.pi * 2 * self.radius


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)
