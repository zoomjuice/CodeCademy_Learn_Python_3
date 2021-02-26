"""
Dictionary values can be accessed by using the key like a list index. e.g.

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599}

print(building_heights["Burj Khalifa"]) returns 828
print(building_heights["Ping An"]) returns 599
"""

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"],
                   "earth": ["Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements['fire'])  # Prints ['Aries', 'Leo', 'Sagittarius']
