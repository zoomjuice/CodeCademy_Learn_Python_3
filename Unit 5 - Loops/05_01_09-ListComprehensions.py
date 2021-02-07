heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

#      variable = [$return for $element in $list if $condition]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

# Comprehensions are also useful for making modified versions of lists
celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [temp * 9/5 + 32 for temp in celsius]

print(fahrenheit)
