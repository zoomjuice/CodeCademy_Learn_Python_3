"""
Notice that when we want to invoke the randint() function we call random.randint(). This is default behavior where
 Python offers a namespace for the module. A namespace isolates the functions, classes, and variables defined in the
  module from the code in the file doing the importing. Your local namespace, meanwhile, is where your code is run.

Python defaults to naming the namespace after the module being imported, but sometimes this name could be ambiguous or
 lengthy. Sometimes, the module’s name could also conflict with an object you have defined within your local namespace.

Fortunately, this name can be altered by aliasing using the as keyword:

import module_name as name_you_pick_for_the_module

You might also occasionally encounter import *. The * is known as a “wildcard” and matches anything and everything.
 This syntax is considered dangerous because it could pollute our local namespace. Pollution occurs when the same name
 could apply to two possible things. For example, if you happen to have a function floor() focused on floor tiles,
 using from math import * would also import a function floor() that rounds down floats.
"""

import random
from matplotlib import pyplot as plt

numbers_a = range(1, 13)
numbers_b = [random.randint(0, 1000) for i in range(12)]

plt.plot(numbers_a, numbers_b)
plt.show()
