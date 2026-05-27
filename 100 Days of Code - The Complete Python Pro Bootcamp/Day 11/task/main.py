import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_dict = {"Ace": 0, "Two": 1, "Three": 2, "Four": 3, "Five": 4, "Six": 5, "Seven": 6,
             "Eight": 7, "Nine": 8, "Ten": 9, "Jack": 10, "Queen": 11, "King": 12, "???": 13}
tokens = int(input(" * How many tokens will each player start with?\n"))
stay_list = []

class Player:
    def __init__(self, name, tokens, hand, bet):
        self.name = name
        self.tokens = tokens
        self.hand = hand
        self.bet = bet

    def draw(self):
        """Draws one card for the player"""
        self.hand.append(random.choice(list(card_dict.keys())))

    def play_round(self):
        """Plays a round of blackjack between the player and computer"""
        while input("Would you like to HIT or STAY? (hit / stay):\n").lower() == "hit":
            self.draw()
            print("Computer:")
            print_hand(players["computer"])
            print("\nYou:")
            print_hand(self)
            if get_player_total(self) > 21:
                print(f" * * * {self.name.title()} BUSTS * * *")
                players["computer"].tokens += self.bet
                self.bet = 0
                break
            elif get_player_total(self) == 21:
                print(f" * * * {self.name.title()} won 1.5 times their bet * * * ")
                self.tokens += int(2.5 * self.bet)
                players["computer"].tokens -= int(2.5 * self.bet) - self.bet
                self.bet = 0
                break
        if get_player_total(self) == 21:
            print(f" * * * {self.name.title()} won 1.5 times their bet * * * ")
            self.tokens += int(2.5 * self.bet)
            players["computer"].tokens -= int(2.5 * self.bet) - self.bet
            self.bet = 0
        elif get_player_total(self) < 21:
            print(f" * * * {self.name.title()} chose to stay at {get_player_total(self)} * * * ")
            stay_list.append(self.name)
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
        tokens_after_bet = tokens - bet
        players[current_name] = Player(current_name, tokens_after_bet, hand, bet)
    hand = []
    bet = 0
    tokens_after_bet = tokens * len(players)
    players["computer"] = Player("computer", tokens_after_bet, hand, bet)
    return players

def get_player_total(player):
    """Gets total of cards for player"""
    total = 0
    for card in player.hand:
        if card_dict[card] != 13:
            total += cards[card_dict[card]]
    return total

def print_hand(player):
    """Prints hand of player"""
    total = get_player_total(player)
    print("Hand:")
    for card in player.hand:
        print(f"* {card}")
    return total

def update_display():
    """Updates display"""
    print("\n")
    print(f" * Current player count: {get_player_count()}\n" + "-"*50)
    for player in players:
        print(f"Player: {players[player].name.title()}\nTokens: {players[player].tokens}\nBet: {players[player].bet}")
        print(f"Hand total: {print_hand(players[player])}")
        print("-" * 22)

def play_game():
    """Plays a game of blackjack"""
    print(art.logo + "\n\n")
    not_over = True
    while not_over:
        for player in players:
            players[player].draw()
            players[player].draw()
        players["computer"].hand.pop()
        players["computer"].hand.append(list(card_dict.keys())[13])
        update_display()

        for player in players:
            if players[player].name == "computer":
                break
            print(f"{players[player].name.title()}'s turn:")
            if get_player_total(players[player]) > 21:
                print(f" * * * {players[player].name.title()} BUSTS * * * ")
                players["computer"].tokens += players[player].bet
                players[player].bet = 0
            elif get_player_total(players[player]) == 21:
                print(f" * * * {players[player].name.title()} won 1.5 times their bet * * * ")
                players[player].tokens += int(2.5 * players[player].bet)
                players["computer"].tokens -= int(2.5 * players[player].bet) - players[player].bet
                players[player].bet = 0
            else:
                players[player].play_round()
            update_display()

        players["computer"].hand.pop()
        while get_player_total(players["computer"]) < 17:
            players["computer"].draw()
        update_display()

        computer_final_score = get_player_total(players["computer"])

        if computer_final_score > 21:
            print(f" * The Dealer BUSTS\nAll remaining players win twice their bet!\n")
            for name in stay_list:
                players[name].tokens += players[name].bet * 2
                players["computer"].tokens -= players[name].bet
                players[name].bet = 0
        elif computer_final_score <= 21:
            for name in stay_list:
                if get_player_total(players[name]) > computer_final_score:
                    print(f" * {name.title()} won against the dealer!\n They win twice their bet!")
                    players[name].tokens += players[name].bet * 2
                    players["computer"].tokens -= players[name].bet
                    players[name].bet = 0
                else:
                    print(f" # {name.title()} lost against the dealer!\n")
                    players["computer"].tokens += players[name].bet
                    players[name].bet = 0

        update_display()
        if input("Will the game continue? (y/n): ").lower() != "y":
            not_over = False
        for player in players:
            players[player].hand = []

players = initialize_players()
play_game()
