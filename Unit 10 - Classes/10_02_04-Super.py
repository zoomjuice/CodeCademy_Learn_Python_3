"""
Overriding methods is really useful in some cases but sometimes we want to add some extra logic to the existing
method. In order to do that we need a way to call the method from the parent class. Python gives us a way to do that
using super().

super() gives us a proxy object. With this proxy object, we can invoke the method of an object’s parent class (also
called its superclass). We call the required function as a method on super():

class Sink:
  def __init__(self, basin, nozzle):
    self.basin = basin
    self.nozzle = nozzle

class KitchenSink(Sink):
  def __init__(self, basin, nozzle, trash_compactor=None):
    super().__init__(basin, nozzle)
    if trash_compactor:
      self.trash_compactor = trash_compactor

Above we defined two classes. First, we defined a Sink class with a constructor that assigns a rinse basin and a sink
nozzle to a Sink instance. Afterwards, we defined a KitchenSink class that inherits from Sink. KitchenSink‘s
constructor takes an additional parameter, a trash_compactor. KitchenSink then calls the constructor for Sink with
the basin and nozzle it received using the super() function, with this line of code:

super().__init__(basin, nozzle)

This line says: “call the constructor (the function called __init__()) of the class that is this class’s parent
class.” In the example given, KitchenSink‘s constructor calls the constructor for Sink. In this way, we can override
a parent class’s method to add some new functionality (like adding a trash_compactor to a sink), while still
retaining the behavior of the original constructor (like setting the basin and nozzle as instance variables).
"""


class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions


class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions, raisins=40):
        super().__init__(potatoes, celery, onions)
        self.raisins = raisins
