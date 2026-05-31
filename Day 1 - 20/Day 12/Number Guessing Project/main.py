import random
import art

EASY = 10
HARD = 5

player_choice = ""

print(art.logo + "\n")

def choose_difficulty():
    global player_choice
    player_choice = input(f"Would you like to play easy mode, or hard mode?\n"
                          f"Enter \"easy\" for 10 guesses.\n"
                          f"Enter \"hard\" for 5 guesses.\n")

def play_round(difficulty):
    global player_choice
    attempts_remaining = difficulty
    number = random.randint(1, 100)
    print(f"I am thinking of a number between 1 and 100\n Try to guess what it is!\nAttempts remaining: {attempts_remaining}\n")
    while player_choice != number:
        if attempts_remaining == 0:
            print(f"You didn't manage to guess it within {difficulty} tries...\nYou lose...\n"
                  f"The number was {number}")
            break
        player_choice = int(input("What is your guess? "))
        attempts_remaining -= 1
        if player_choice == number:
            print(f"You guessed correctly! My number was: {number}")
        elif player_choice > number:
            print(f"You guessed too high!")
        elif player_choice < number:
            print(f"You guessed too low!")
        print(f"Attempts remaining: {attempts_remaining}\n")

def play_game():
    global player_choice
    not_over = True

    while not_over:
        choose_difficulty()
        if player_choice == "easy":
            play_round(EASY)
        elif player_choice == "hard":
            play_round(HARD)
        else:
            print("You did not chose a difficulty level. ( bad input )\n")
            continue

        player_choice = input("Would you like to play another round? (yes/no)\n")
        if player_choice != "yes":
            not_over = False
        print("\n" * 5)

play_game()
