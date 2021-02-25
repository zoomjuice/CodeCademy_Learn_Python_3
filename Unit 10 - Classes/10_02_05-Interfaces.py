"""
You may be wondering at this point why we would even want to have two different classes with two differently
implemented methods to use the same method name. This style is especially useful when we have an object for which it
might not matter which class the object is an instance of. Instead, we’re interested in whether that object can
perform a given task.

If we have the following code:

class Chess:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_chess_pieces()

  def play(self):
    print("Playing chess!")

class Checkers:
  def __init__(self):
    self.board = setup_board()
    self.pieces = add_checkers_pieces()

  def play(self):
    print("Playing checkers!")

In the code above we define two classes, Chess and Checkers. In Chess we define a constructor that sets up the board
and pieces, and a .play() method. Checkers also defines a .play() method. If we have a play_game() function that
takes an instance of Chess or Checkers, it could call the .play() method without having to check which class the
object is an instance of.

def play_game(chess_or_checkers):
  chess_or_checkers.play()

chess_game = Chess()
checkers_game = Checkers()
chess_game_2 = Chess()

for game in [chess_game, checkers_game, chess_game_2]:
  play_game(game)

Prints out the following:
Playing chess!
Playing checkers!
Playing chess!

In this code, we defined a play_game function that could take either a Chess object or a Checkers object. We
instantiate a few objects and then call play_game on each.

When two classes have the same method names and attributes, we say they implement the same interface. An interface in
Python usually refers to the names of the methods and the arguments they take. Other programming languages have more
rigid definitions of what an interface is, but it usually hinges on the fact that different objects from different
classes can perform the same operation (even if it is implemented differently for each class).
"""


class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def get_rate(self):
        return .001 * self.price_of_insured_item


class HomeInsurance(InsurancePolicy):
    def get_rate(self):
        return .00005 * self.price_of_insured_item
