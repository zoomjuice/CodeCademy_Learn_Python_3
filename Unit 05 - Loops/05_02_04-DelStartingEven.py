"""
Write a function called delete_starting_evens() that has a parameter named lst.

The function should remove elements from the front of lst until the front of the list is not even. The function should
 then return lst.

For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!
"""


def delete_starting_evens(lst):  # This version keeps deleting the first element until the first is odd
    while len(lst) != 0 and lst[0] % 2 == 0:
        lst = lst[1:]
    return lst


# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


def del_starting_evens(lst):  # This version looks for the first odd element and makes a new list that starts there
    i = 0
    while i <= len(lst):
        if i == len(lst):
            return []
        elif lst[i] % 2 == 1:
            i += 1
            break
        else:
            i += 1
            continue
    new_list = lst[i-1:]
    return new_list


# Uncomment the lines below when your function is done
print(del_starting_evens([4, 8, 10, 11, 12, 15]))
print(del_starting_evens([4, 8, 10]))
