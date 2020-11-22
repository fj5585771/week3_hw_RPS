from app.models.player import *

class Game():
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    # write a function that takes in 2 players and compares their choices and returns the winning player.  if a draw the player should be None type

    def play_game(self):
        if (self.player_1.choice == "rock" and self.player_2.choice == "paper") or (self.player_1.choice == "paper" and self.player_2.choice == "scissors") or (self.player_1.choice == "scissors" and self.player_2.choice == "rock"):
            return f"{self.player_2.name} wins!"

        elif self.player_1.choice == self.player_2.choice:
            draw = None
            return "Its a draw!"     

        else:
            return f"{self.player_1.name} wins!"
