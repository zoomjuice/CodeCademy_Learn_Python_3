"""
One way that we can introduce polymorphism to our class definitions is by using Python’s special dunder methods.
We’ve explored a few already, the constructor __init__() and the string representation method __repr__, but that’s
only scratching the tip of the iceberg.

Python gives us the power to define dunder methods that define a custom-made class to look and behave like a Python
builtin. What does that mean? Say we had a class that has an addition method:

class Color:
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue


  def __repr__(self):
    return "Color with RGB = ({red}, {green}, {blue})".format(red=self.red, green=self.green, blue=self.blue)

  def add(self, other):
    \"""
    Adds two RGB colors together
    Maximum value is 255
    \"""
    new_red = min(self.red + other.red, 255)
    new_green = min(self.green + other.green, 255)
    new_blue = min(self.blue + other.blue, 255)

    return Color(new_red, new_green, new_blue)

red = Color(255, 0, 0)
blue = Color(0, 0, 255)

magenta = red.add(blue)
print(magenta)
# Prints "Color with RGB = (255, 0, 255)"

In this code we defined a Color class that implements an addition function. Unfortunately, red.add(blue) is a little
verbose for something that we have an intuitive symbol for (i.e., the + symbol). Well, Python offers the dunder
method __add__ for this very reason! If we rename the add() method above to something that looks like this:

class Color:
  def __add__(self, other):
    \"""
    Adds two RGB colors together
    Maximum value is 255
    \"""
    new_red = min(self.red + other.red, 255)
    new_green = min(self.green + other.green, 255)
    new_blue = min(self.blue + other.blue, 255)

    return Color(new_red, new_green, new_blue)

Then, if we create the colors:

red = Color(255, 0, 0)
green = Color(0, 255, 0)
blue = Color(0, 0, 255)


We can add them together using the + operator!

# Color with RGB: (255, 0, 255)
magenta = red + blue

# Color with RGB: (0, 255, 255)
cyan = green + blue

# Color with RGB: (255, 255, 0)
yellow = red + green

# Color with RGB: (255, 255, 255)
white = red + green + blue

Since we defined an __add__ method for our Color class, we were able to add these objects together using the + operator.
"""


class Atom:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return self.label

    def __add__(self, other):
        return Molecule([self, other])


class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms

    def __repr__(self):
        atom_str = ''
        for atom in self.atoms:
            atom_str += atom.__repr__()
        return atom_str


sodium = Atom("Na")
chlorine = Atom("Cl")
# salt = Molecule([sodium, chlorine])
salt = sodium + chlorine

print(salt)
