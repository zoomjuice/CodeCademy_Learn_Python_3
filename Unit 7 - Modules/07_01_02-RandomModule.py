"""
One of the most commonly used modules is random, which allows you to generate numbers or select items at random.

With random, we'll be using more than one piece of the module's functionality, so the import syntax will look like:

import random
"""

# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)
