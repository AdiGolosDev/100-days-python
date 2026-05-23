import random

word_list = ["aardvark", "baboon", "camel", "omnipotent", "mystery", "puzzle", "hangman"]

chosen_word = random.choice(word_list)
word_guess = []

for character in chosen_word:
    word_guess.append("_")

def fill(g):
    i = 0
    for char in chosen_word:
        if g == char:
            word_guess[i] = g
            i += 1
        else:
            i += 1

def print_progress():
    a = ""
    for char in word_guess:
        a += char
    return a
guess_count = int(input("How many guesses would you like to allow yourself? \nThe minimum number of guesses is 5"))
if guess_count < 5:
    guess_count = 5
    print("Minimum number of guesses will be applied...")

print("Your current progress is: " + print_progress())
while print_progress() != chosen_word and guess_count > 0:
    print(f"Attempts remaining: {guess_count}")
    guess = input("Please guess a letter! ").lower()
    if guess in word_guess:
        print("You already guessed this letter!")
    else:
        guess_count -= 1

    if guess in chosen_word:
        print("Right, this letter is in the chosen word!")
        fill(guess)
    else:
        print("Wrong, this letter is not in the chosen word!")

    print("Your current guess progress is: " + print_progress())

if guess_count < 1 and print_progress() != chosen_word:
    print("You lose!")
else:
    print("You win!")
