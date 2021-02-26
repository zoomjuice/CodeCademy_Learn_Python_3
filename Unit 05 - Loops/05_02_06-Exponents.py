"""
Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list
 containing every number in bases raised to every number in powers.

For example, consider the following code.

exponents([2, 3, 4], [1, 2, 3])

the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the
 second. Then two to the third, and so on.
"""


def exponents(bases, powers):
    raised = []
    for base in bases:
        for power in powers:
            raised.append(base ** power)
    return raised


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

# Try a nested list comprehension


def expwnage(bases, powers):
    raised = [base ** power for base in bases for power in powers]  # oww oof my brain
    return raised


print(expwnage([2, 3, 4], [1, 2, 3]))
