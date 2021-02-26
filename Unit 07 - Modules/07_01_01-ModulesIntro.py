"""
A module is a collection of Python declarations intended broadly to be used as a tool. Modules are also often referred
 to as “libraries” or “packages” — a package is really a directory that holds a collection of modules.

Often, a library will include a lot of code that you don't need that may slow down your program or conflict with
 existing code. Because of this, it makes sense to only import what you need.
"""

from datetime import datetime

current_time = datetime.now()

print(current_time)
