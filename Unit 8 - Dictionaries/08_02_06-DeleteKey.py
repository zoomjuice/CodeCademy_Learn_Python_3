"""
When we get a ticket number, we want to return the prize and also remove that pair from the dictionary, since the prize
 has been given away. We can use .pop() to do this. Just like with .get(), we can provide a default value to return
 if the key does not exist in the dictionary:
"""

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25,
                   "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop('stamina grains', 0)
health_points += available_items.pop('power stew', 0)
health_points += available_items.pop('mystic bread', 0)

print(available_items)
print(health_points)
