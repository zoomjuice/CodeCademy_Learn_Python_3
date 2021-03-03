from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:


def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
    from_lat = from_coords[0]
    to_lat = to_coords[0]
    from_long = from_coords[1]
    to_long = to_coords[1]
    shipping_rate = SHIPPING_PRICES.get(shipping_type)
    distance = get_distance(from_lat, from_long, to_lat, to_long)
    shipping_price = shipping_rate * distance
    return format_price(shipping_price)


# Test the function by calling
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here


def calculate_driver_cost(distance, *drivers):
    cheapest_driver = None
    cheapest_driver_price = None
    for driver in drivers:
        driver_time = driver.speed * distance
        price_for_driver = driver.salary * driver_time
        if cheapest_driver is None:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
        elif price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
    return cheapest_driver_price, cheapest_driver


# Test the function by calling
test_function(calculate_driver_cost)

# Define calculate_money_made() here


def calculate_money_made(**trips):
    total_revenue = 0
    for trip in trips.values():
        trip_revenue = trip.cost - trip.driver.cost
        total_revenue += trip_revenue
    return total_revenue


# Test the function by calling
test_function(calculate_money_made)

"""
nile.py

from math import sin, cos, atan2, sqrt


def get_distance(from_lat, from_long, to_lat, to_long):
    dlon = to_long - from_long
    dlat = from_lat - to_lat
    a = (sin(dlat / 2)) ** 2 + cos(from_lat) * cos(to_lat) * (sin(dlon / 2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = a * c
    return distance


SHIPPING_PRICES = {
    'Ground': 1,
    'Priority': 1.6,
    'Overnight': 2.3,
}


def format_price(price):
    return "${0:.2f}".format(price)
"""

"""
test.py

def test_function(fn):
    if fn.__name__ == "calculate_shipping_cost":
        test_shipping(fn)
    if fn.__name__ == "calculate_driver_cost":
        test_driver(fn)
    if fn.__name__ == "calculate_money_made":
        test_money(fn)


def test_shipping(f):
    try:
        costs = f((0, 0), (1, 1))
    except TypeError:
        print("calculate_shipping_cost() did not provide default argument for shipping_type")
        return
    if not type(costs) is str:
        print("calculate_shipping_cost() did not format the result in a string")
        return
    if costs != "$1.04":
        print("calculate_shipping_cost((0, 0), (1, 1)) returned {}. Expected result is {}".format(costs, "$1.04"))
        return
    print("OK! calculate_shipping_cost() passes tests")


class Driver:
    def __init__(self, speed, salary):
        self.speed = speed
        self.salary = salary

    def __repr__(self):
        return "Nile Driver speed {} salary {}".format(self.speed, self.salary)


driver1 = Driver(2, 10)
driver2 = Driver(7, 20)


def test_driver(f):
    try:
        price, driver = f(80, driver1, driver2)
    except TypeError:
        print("calculate_driver_cost() doesn't expect multiple driver arguments")
        return
    if type(driver) is not Driver:
        print("calculate_driver_cost() did not return driver")
        return
    if price != 1600:
        print("calculate_driver_cost() did not provide correct final price (expected {}, received {})".format(price, 1600))
        return
    if driver is not driver1:
        print("calculate_driver_cost() did not provide least expensive driver")
        return
    print("OK! calculate_driver_cost() passes tests")


class Trip:
    def __init__(self, cost, driver, driver_cost):
        self.cost = cost
        driver.cost = driver_cost
        self.driver = driver


trip1 = Trip(200, driver1, 15)
trip2 = Trip(300, driver2, 40)


def test_money(f):
    try:
        money = f(UEXODI=trip1, DEFZXIE=trip2)
    except TypeError:
        print("calculate_money_made() doesn't expect multiple trip keyword arguments")
        return
    if type(money) not in (int, float):
        print("calculate_driver_cost() did not return a number")
        return
    if money != 445:
        print(
            "calculate_driver_cost() did not provide correct final price (expected {}, received {})".format(money, 445))
        return
    print("OK! calculate_money_made() passes tests")
"""
