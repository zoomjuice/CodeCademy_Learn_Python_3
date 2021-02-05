# Raise number to the tenth power
def tenth_power(number):
    return number ** 10


# Calculate square root of number
def square_root(number):
    return number ** .5


# Calculate percentage of games won
def win_percentage(wins, losses):
    total_games = wins + losses
    return round((wins / total_games) * 100, 2)


# Calculate average of two numbers
def average(num1, num2):
    return (num1 + num2) / 2


# Calculate modulo of twice the numerator and half the denominator
def remainder(numerator, denominator):
    return (numerator * 2) % (denominator / 2)


# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))  # 1 to the 10th power is 1
print(tenth_power(0))  # 0 to the 10th power is 0
print(tenth_power(2))  # 2 to the 10th power is 1024
print()

# Uncomment these function calls to test your square_root function:
print(square_root(16))  # should print 4
print(square_root(100))  # should print 10
print()

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))  # should print 50
print(win_percentage(10, 0))  # should print 100
print()

# Uncomment these function calls to test your average function:
print(average(1, 100))  # The average of 1 and 100 is 50.5
print(average(1, -1))  # The average of 1 and -1 is 0
print()

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))  # should print 2
print(remainder(9, 6))  # should print 0
print()
