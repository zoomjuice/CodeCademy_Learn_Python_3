"""
A Python function can return multiple things. This is especially useful in cases where bundling data into a different
structure (a dictionary or a list, for instance) would be excessive. In Python we can return multiple pieces of data
by separating each variable with a comma:

def multiple_returns(cool_num1, cool_num2):
  sum_nums = cool_num1 + cool_num2
  div_nums = cool_num1 / cool_num2
  return sum_nums, div_nums

Above we created a function that returns two results, sum_nums and div_nums. What happens when we call the function?

sum_and_div = multiple_returns(20, 10)

print(sum_and_div)
# Prints "(30, 2)"

print(sum_and_div[0])
# Prints "30"

So we get those two values back in what’s called a tuple, an immutable list-like object indicated by parentheses. We
can index into the tuple the same way as a list and so sum_and_div[0] will give us our sum_nums value and
sum_and_div[1] will produce our div_nums value.

What if we wanted to save these two results in separate variables? Well we can by unpacking the function return. We
can list our new variables, comma-separated, that correspond to the number of values returned:

sum, div = multiple_returns(18, 9)

print(sum)
# Prints "27"

print(div)
# Prints "2"

Above we were able to unpack the two values returned into separate variables.
"""


def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper


the_scream, the_whisper = scream_and_whisper('Foo')

print(the_scream, the_whisper)
