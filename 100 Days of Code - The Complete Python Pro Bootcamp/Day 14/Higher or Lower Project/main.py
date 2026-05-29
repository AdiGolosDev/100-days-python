import game_data
import art
import random

print(art.logo + "\n")

A = random.choice(game_data.data)
B = random.choice(game_data.data)

def initialize_AB():
    global A
    global B
    A = random.choice(game_data.data)
    B = random.choice(game_data.data)
    while True:
        if A == B:
            B = random.choice(game_data.data)
        else:
            break

def compare(A, B):
    if A['follower_count'] > B['follower_count']:
        return "A"
    else:
        return "B"

def play_game():
    global A
    global B
    finished = False
    score = 0
    while not finished:
        initialize_AB()
        answer = compare(A, B)
        print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.\n")
        print(art.vs + "\n")
        print(f"Compare B: {B['name']}, {B['description']}, from {B['country']}.\n")
        choice = input("Who do you think has more followers?\n Type \'A\' or \'B\': ").upper()
        if choice == answer:
            print("You got it right!")
            score += 1
        else:
            print("You got it wrong!")
            finished = True
        print(f"Current Score: {score}\n")

    print(f"Final Score: {score}\n")

play_game()
again = True
while again:
    P_input = input("Would you like to play again? (y / n): ").lower()
    if P_input != "y":
        again = False
