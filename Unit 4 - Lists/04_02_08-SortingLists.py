# Exercise 1 & 2
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace',
             '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
addresses.sort()

print(addresses)

# Exercise 3
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']

# sort(names) doesn't work because sort() does not return anything
names.sort()

# Exercise 4
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

# sorted_cities will be none because .sort() doesn't return anything, cities will, however, be sorted
sorted_cities = cities.sort()

print(sorted_cities)
print(cities)

#

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

# The sorted() function returns a sorted list while leaving the original list intact
games_sorted = sorted(games)

print(games)
print(games_sorted)
