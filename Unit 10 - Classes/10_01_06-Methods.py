"""
Methods are functions that are defined as part of a class. The first argument in a method is always the object
that is calling the method. Convention recommends that we name this first argument self. Methods always have at least
this one argument.

We define methods similarly to functions, except that they are indented to be part of the class.

class Dog:
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."

Above we created a Dog class with a time_explanation method that takes one argument, self, which refers to the object
calling the function. We created a Dog named pipi_pitbull and called the .time_explanation() method on our new object
for Pipi.

Notice we didn't pass any arguments when we called .time_explanation(), but were able to refer to self in the
function body. When you call a method it automatically passes the object calling the method as the first argument.

"""


class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."
