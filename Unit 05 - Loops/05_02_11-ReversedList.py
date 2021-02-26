"""
Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.
"""


def reversed_list(lst1, lst2):
    lst1_reversed = []
    for i in range(len(lst1)):
        lst1_reversed.append(lst1.pop())
    return lst1_reversed == lst2


# Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

# Challenge: Try iterating over one of the lists backwards instead of creating a new list


def reverse_list(lst1, lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[len(lst1) - 1 - i]:
            return False
    return True


# Uncomment the lines below when your function is done
print(reverse_list([1, 2, 3], [3, 2, 1]))
print(reverse_list([1, 5, 3], [3, 2, 1]))
