songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key: value for key, value in zip(songs, playcounts)}
plays.update({'Purple Haze': 1})  # Add a new value

plays['Respect'] = 94  # Update an existing value

library = {'The Best Songs': plays, 'Sunday Feelings': {}}

print(plays)
print(library)
