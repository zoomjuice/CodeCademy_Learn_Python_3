"""
Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
"""


def same_values(lst1, lst2):
    indices_of_same_val = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i]:
            indices_of_same_val.append(i)
    return indices_of_same_val


# Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# Challenge: Try using a list comprehension
# Challenge: Rewrite function to work on lists of different lengths
