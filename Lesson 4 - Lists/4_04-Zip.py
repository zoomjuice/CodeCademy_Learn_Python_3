names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

# Zip combines two lists into a a zip object
names_and_dogs_names = zip(names, dogs_names)

print(names_and_dogs_names)

# To create a list of TUPLES, you must run list() on the zip object
list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)

list_of_names_and_dogs_names[0].append('foo')
