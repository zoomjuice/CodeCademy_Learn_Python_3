"""
Methods can also take more arguments than just self:

class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"

Above we defined a DistanceConverter class, instantiated it, and used it to convert 5 miles into kilometers. Notice
again that even though how_many_kms takes two arguments in its definition, we only pass miles, because self is
implicitly passed (and refers to the object converter).

Note: You still need to call a variable as class.variable even inside the class.
"""


class Circle:
    pi = 3.14

    def area(self, radius):
        return Circle.pi * radius ** 2


circle = Circle()

pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(11_460 / 2)

print(pizza_area)
print(teaching_table_area)
print(round_room_area)
