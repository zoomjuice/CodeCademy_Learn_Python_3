suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

# Use x:y to select a subset of elements from a list from index x to y-1
beginning = suitcase[0:4]

print(beginning)

# Will select elements of index 2 and 3
middle = suitcase[2:4]

print(middle)

# You can omit the 0 when selecting from the beginning or to the end of a list
first_three = suitcase[:3]
two_to_end = suitcase[2:]
last_two = suitcase[-2:]

print(first_three)
print(two_to_end)
print(last_two)
