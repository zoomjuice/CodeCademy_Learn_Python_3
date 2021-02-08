"""
Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function
 should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total
 sum of all the elements. If the list is empty, the function should return 0.

For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.
"""


def over_nine_thousand(lst):  # Uses while loop
    if sum(lst) < 9000:
        return sum(lst)
    else:
        lst_sum = 0
        i = 0
        while lst_sum < 9000:
            lst_sum += lst[i]
            i += 1
        return lst_sum


# Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([8000, 1000]))
print(over_nine_thousand([]))
print(over_nine_thousand([1]))


def over_9k(lst):  # Uses for loop
    if sum(lst) < 9000:
        return sum(lst)
    else:
        lst_sum = 0
        for value in lst:
            if lst_sum > 9000:
                break
            else:
                lst_sum += value
        return lst_sum


print(over_9k([8000, 900, 120, 5000]))
print(over_9k([8000, 1000]))
print(over_9k([]))
print(over_9k([1]))
