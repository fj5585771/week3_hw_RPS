from app.models.player import *

class Game:

    def __init__(self):
        self.win_lookup = {
            "scissors": "paper",
            "rock" : "scissors",
            "paper" : "rock"
        }

    # Constructor not needed

    # write a function that takes in 2 players and compares their choices and returns the winning player.  if a draw the player should be None type

    def play_game(self, player_1, player_2):
        choice1 = player_1.choice.lower()
        choice2 = player_2.choice.lower()

        winner = None
        
        if self.win_lookup.get(choice1) == choice2:
            winner = player_1
        elif self.win_lookup.get(choice2) == choice1:
            winner = player_2

        return winner
