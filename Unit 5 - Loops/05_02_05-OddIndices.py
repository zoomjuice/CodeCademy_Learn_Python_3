"""
Create a function named odd_indices() that has one parameter named lst.

The function should create a new empty list and add every element from lst that has an odd index. The function should
 then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].
"""


def odd_indices(lst):
    new_list = []
    i = 0
    while i < len(lst):
        if i % 2 == 0:
            i += 1
            continue
        else:
            new_list.append(lst[i])
            i += 1
    return new_list


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

# Try solving with range()
# Maybe a list comprehension?


def odder_indices(lst):
    odd_list = [lst[i] for i in range(len(lst)) if i % 2 == 1]
    return odd_list


print(odder_indices([4, 3, 7, 10, 11, -2]))

# Now try it without a conditional


def oddest_indices(lst):
    odd_list = [lst[i] for i in range(1, len(lst), 2)]
    return odd_list


print(oddest_indices([4, 3, 7, 10, 11, -2]))
