toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

pizzas = list(zip(prices, toppings))
pizzas.sort()
num_pizzas = len(pizzas)
cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
num_2_dollar_slices = prices.count(2)

# Three cheapest pizzas... for the mice, of course
three_cheapest = pizzas[:3]

print("We sell {} different kinds of pizza!".format(num_pizzas))
print(pizzas)

print(three_cheapest)
