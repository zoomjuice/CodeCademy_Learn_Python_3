letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
           "V", "W", "X", "Y", "Z", " "]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letter_to_points = {letter: point for letter, point in zip(letters, points)}
player_to_words = {'player1': ['blue', 'tennis', 'exit'],
                   'wordNerd': ['earth', 'eyes', 'machine'],
                   'Lexi Con': ['eraser', 'belly', 'husky'],
                   'Prof Reader': ['zap', 'coma', 'period']}
player_to_points = {}


def score_word(word):
    score = 0
    for letter in word:
        score += letter_to_points[letter.upper()]
    return score


def play_word(player):
    if player not in player_to_words.keys():
        print('Player {player} doesn\'t exist. Are you sure you spelled it correctly?'.format(player=player))
        return 'ERROR'
    word = input('Please enter your word: ')
    if word.isalpha():
        player_to_words[player].append(word.lower())
        return
    else:
        print("{word} is not a valid word.".format(word=word))
        return 'ERROR'


def update_point_totals():
    global player_to_points
    player_to_points = {key: sum([score_word(element) for element in value]) for key, value in player_to_words.items()}
    return


# play_word('player1')

update_point_totals()

print(player_to_words)
print(player_to_points)
# print(score_word('brownie'))  # Should return 15
