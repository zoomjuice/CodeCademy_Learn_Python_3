# Append list size to end of list
def append_size(lst):
    lst.append(len(lst))
    return lst


# Add last two elements of list and append the value; repeat three times (Fibonacci!)
def append_sum(lst):
    for i in range(3):
        lst.append(lst[-2] + lst[-1])
    return lst


# Return the last element of the larger list, or the last element of the first list if list length is equal
def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    elif len(lst1) < len(lst2):
        return lst2[-1]
    else:
        return "ERROR"


# Return True if $item occurs in $list more than $n times
def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    elif lst.count(item) <= n:
        return False
    else:
        return "ERROR"


# Combine two lists and sort the resulting list
def combine_sort(lst1, lst2):
    combined_list = lst1 + lst2
    combined_list.sort()
    return combined_list
