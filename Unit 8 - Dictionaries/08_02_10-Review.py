from random import randint

tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant",
         6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice",
         12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star",
         18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

times = ['past', 'present', 'future']
cards = [randint(1, 22) for i in range(3)]

while len(cards) != len(set(cards)):
    cards = [randint(1, 22) for i in range(3)]

spread = {time: tarot[card] for time, card in zip(times, cards)}

# spread.update({'past': tarot.pop(13), 'present': tarot.pop(22), 'future': tarot.pop(10)})

for key, val in spread.items():
    print('Your {key} is the {value} card.'.format(key=key, value=val))
