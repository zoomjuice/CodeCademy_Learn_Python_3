single_digits = list(range(10))
squares = []
cubes = [i**3 for i in single_digits]

for digit in single_digits:
  print(digit)
  squares.append(digit**2)

print(squares)
print(cubes)
