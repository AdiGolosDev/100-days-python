import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
tokens = int(input(" * How many tokens will each player start with?\n"))
players = []

class Player:
    def __init__(self, name, tokens):
        self.name = name
        self.tokens = tokens

def get_player_count():
    """Gets player count which can only be between 1 and 3 inclusive"""
    player_count = 1
    player_count = int(input(" * Please enter how many players will be participating besides the computer: (max: 3)\n"))
    if  player_count < 0 or player_count > 3:
        print(" * Invalid input, please enter again:")
        get_player_count()
    return player_count

def initialize_players():
    """Initializes player objects and list of players"""
    player_count = get_player_count()
    for i in range(player_count):
        current_name = input(f" * Player {i + 1} * Please enter your name:\n")
        player1 = Player(current_name, tokens)
        players.append(player1)

initialize_players()
print(players)