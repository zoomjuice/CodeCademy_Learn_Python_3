def first_three_multiples(num):
    print(num, num * 2, num * 3)
    return num * 3

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)  # should print 10, 20, 30, and return 30
first_three_multiples(0)  # should print 0, 0, 0, and return 0


def tip(bill, percentage):
    return bill * (percentage / 100)


# Uncomment these function calls to test your tip function:
print(tip(10, 25))  # should print 2.5
print(tip(0, 100))  # should print 0.0


def introduction(name_first, name_last):
    intro_string = name_last + ", " + name_first + " " + name_last
    return intro_string


# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))  # should print Bond, James Bond
print(introduction("Maya", "Angelou"))  # should print Angelou, Maya Angelou


def dog_years(name, age):
    return "{}, you are {} years old in dog years".format(name, age * 7)


# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))  # should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))  # should print "Baby, you are 0 years old in dog years"


def lots_of_math(a, b, c, d):
    print(a + b)
    print(c - d)
    print((a + b) * (c - d))
    return ((a + b) * (c - d)) % a


# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))  # should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))  # should print 2, 0, 0, 0
