import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_dict = {"Ace": 0, "Two": 1, "Three": 2, "Four": 3, "Five": 4, "Six": 5, "Seven": 6,
             "Eight": 7, "Nine": 8, "Ten": 9, "Jack": 10, "Queen": 11, "King": 12}
tokens = int(input(" * How many tokens will each player start with?\n"))

class Player:
    def __init__(self, name, tokens, hand, bet):
        self.name = name
        self.tokens = tokens
        self.hand = hand
        self.bet = bet

    def draw(self):
        self.hand.append(random.choice(list(card_dict.keys())))

    def play_round(self):
        while input("Would you like to HIT or STAY? (hit / stay):\n").lower() == "hit":
            self.draw()
            print_hand(players["computer"])
            print_hand(self)
            if get_player_total(self) > 21:
                print(f" * * * {self.name.title()} BUSTS * * *")
                break
            elif get_player_total(self) == 21:
                print(f" * * * {self.name.title()} WINS * * * ")
                break
        if get_player_total(self) == 21:
            print(f" * * * {self.name.title()} won 1.5 times their bet * * * ")
        elif get_player_total(self) < 21:
            print(f" * * * {self.name.title()} chose to stay at {get_player_total(self)} * * * ")
        else:
            return


def initialize_player_count():
    """Gets player count which can only be between 1 and 3 inclusive"""
    player_count = 1
    player_count = int(input(" * Please enter how many players will be participating besides the computer: (max: 3)\n"))
    if  player_count < 0 or player_count > 3:
        print(" * Invalid input, please enter again:")
        initialize_player_count()
    return player_count

def get_player_count():
    """Gets player count"""
    return len(players)

def initialize_players():
    """Initializes player objects and returns a dictionary of players"""
    players = {}
    player_count = initialize_player_count()
    for i in range(player_count):
        hand = []
        current_name = input(f" * Player {i + 1} * Please enter your name:\n")
        bet = int(input(f" * Player {i + 1} * How much would you like to bet?\n"))
        players[current_name] = Player(current_name, tokens, hand, bet)
    hand = []
    bet = 0
    players["computer"] = Player("computer", tokens, hand, bet)
    return players

def print_hand(player):
    """Prints hand of player"""
    total = 0
    print("Hand:")
    for card in player.hand:
        print(f"* {card}")
        total += cards[card_dict[card]]

    return total

def get_player_total(player):
    """Gets total of cards for player"""
    total = 0
    for card in player.hand:
        total += cards[card_dict[card]]
    return total

def update_display():
    """Updates display"""
    print("\n" * 20)
    print(f"\n{art.logo}\n * Current player count: {get_player_count()}\n")
    for player in players:
        print(f"Player: {players[player].name.title()}\nTokens: {players[player].tokens}")
        print(f"Hand total: {print_hand(players[player])}")
        print("-" * 22)

def play_game():
    """Plays a game of blackjack"""
    not_over = True
    while not_over:
        for player in players:
            players[player].hand.append(random.choice(list(card_dict.keys())))
            players[player].hand.append(random.choice(list(card_dict.keys())))

        update_display()

        for player in players:
            if players[player].name == "computer":
                break

            print(f"{players[player].name.title()}'s turn:")
            if get_player_total(players[player]) > 21:
                print(f" * * * {players[player].name.title()} BUSTS * * * ")
            elif get_player_total(players[player]) == 21:
                print(f" * * * {players[player].name.title()} won 1.5 times their bet * * * ")
            else:
                players[player].play_round()

            update_display()


        not_over = False

players = initialize_players()
play_game()
