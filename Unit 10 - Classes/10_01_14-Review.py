"""
So far we’ve covered what a data type actually is in Python. We explored what the functionality of Python’s
built-in types (also called primitives) are. We learned how to create our own data types using the class keyword.

We explored the relationship between a class and an object — we create objects when we instantiate a class,
we find the class when we check the type() of an object. We learned the difference between class variables (the same
for all objects of a class) and instance variables (unique for each object).

We learned about how to define an object’s functionality with methods. We created multiple objects from the same
class, all with similar functionality, but with different internal data. They all had the same methods, but produced
different output because they were different instances.
"""


class Student:

    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}

    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) // len(self.grades)


class Grade:

    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def __add__(self, other):
        return self.score + other

    def __radd__(self, other):
        return other + self.score

    def __sub__(self, other):
        return self.score - other

    def __rsub__(self, other):
        return other - self.score

    def is_passing(self):
        return self.score >= self.minimum_passing


roger = Student('Roger van der Weyden', 'year 10')
sandro = Student('Sandro Botticelli', 'year 12')
pieter = Student('Pieter Bruegel the Elder', 'year 8')

grade_1 = Grade(100)
grade_2 = Grade(44)
grade_3 = Grade(70)

pieter.add_grade(grade_1)
pieter.add_grade(grade_2)
pieter.add_grade(grade_3)

print(pieter.get_average())
