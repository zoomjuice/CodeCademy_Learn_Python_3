"""
Classes are designed to allow for more code reuse, but what if we need a class that looks a lot like a class we
already have? If the bulk of a class’s definition is useful, but we have a new use case that is distinct from how the
original class was used, we can inherit from the original class. Think of inheritance as a remix — it sounds a lot
like the original, but there’s something… different about it.

class User:
  is_admin = False
  def __init__(self, username)
    self.username = username

class Admin(User):
  is_admin = True

Above we defined User as our base class. We want to create a new class that inherits from it, so we created the
subclass Admin. In the above example, Admin has the same constructor as User. Only the class variable is_admin is set
differently between the two.

Sometimes a base class is called a parent class. In these terms, the class inheriting from it, the subclass,
is also referred to as a child class.
"""


class Bin:
    pass


class RecyclingBin(Bin):
    pass
