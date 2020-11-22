from flask import render_template
from app import app
from app.models.player import Player
from app.models.game import Game

@app.route('/')
def index():
    return render_template ('index.html', title ='Home')

@app.route('/<choice1>/<choice2>')
def game(choice1, choice2):
    player_1 = Player ("fraser", choice1)
    player_2 = Player ("eric", choice2)
    only_game = Game(player_1, player_2)
    result = only_game.play_game()
    return render_template("result.html", result = result, choice1 = choice1, choice2 = choice2)

# @app.route(‘/<move1>/<move2>’)
# def play_a_game(move1, move2):
#     player_1 = Player( "Player 1”, move1 )
#     player_2 = Player( "Player 2", move2 )
#     game = Game( player_1, player_2 )
#     winner = game.play_game( player_1, player_2 )
#     return (render_template(“winner.html”, winner = winner, move1=move1, move2=move2))
