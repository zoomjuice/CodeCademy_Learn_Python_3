"""
Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums
"""


def max_num(lst):
    biggest = lst[0]
    for num in lst:
        if num > biggest:
            biggest = num
    return biggest


# Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))


def big_num(lst):
    return max(lst)  # Cheeky


print(big_num([50, -10, 0, 75, 20]))


def num_mais_grande(lst):
    lst.sort()
    return lst[-1]  # Less cheeky but still cheeky and wildly inefficient


print(num_mais_grande([50, -10, 0, 75, 20]))
