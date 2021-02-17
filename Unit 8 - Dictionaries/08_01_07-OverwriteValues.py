"""
We know that we can add a key by using syntax like:

menu["avocado toast"] = 7

This will create a key "avocado toast" and set the value to 7. But what if we already have an 'avocado toast' entry in
 the menu dictionary?

In that case, our value assignment would overwrite the existing value attached to the key 'avocado toast'.

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)

This would yield:

{"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

Notice the value of "oatmeal" has now changed to 5.
"""

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone",
                 "Animated Feature": "Zootopia"}

oscar_winners.update({'Supporting Actress': 'Viola Davis'})
oscar_winners['Best Picture'] = 'Moonlight'
