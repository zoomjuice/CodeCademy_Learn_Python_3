names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

# Zip combines two lists into a a zip object
names_and_dogs_names = zip(names, dogs_names)

print(names_and_dogs_names)

# To create a list of TUPLES, you must run list() on the zip object
list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)

# Trying to modify a tuple throws an error
# list_of_names_and_dogs_names[0][1] = 'Spot'

# To modify an element in a zipped list, convert the tuples in it to lists
for i in range(len(list_of_names_and_dogs_names)):
    list_of_names_and_dogs_names[i] = list(list_of_names_and_dogs_names[i])

# After conversion, elements may be changed
list_of_names_and_dogs_names[0][1] = 'Spot'

print(list_of_names_and_dogs_names)
