from flask import render_template
from app import app
from app.models.player import *
from app.models.game import *

@app.route('/')
def index():
    return render_template ('index.html', title ='Home')

@app.route('/<choice1>/<choice2>')
def game(choice1, choice2):
    player_1 = Player ("fraser", choice1)
    player_2 = Player ("eric", choice2)
    only_game = Game()
    winner = only_game.play_game(player_1, player_2)
    return render_template('result.html', winner=winner, only_game=only_game)
