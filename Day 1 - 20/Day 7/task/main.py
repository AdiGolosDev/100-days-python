import random
import hangman_words
import hangman_art

print(f"Welcome to: \n {hangman_art.logo}\n")

chosen_word = random.choice(hangman_words.word_list)
word_guess = []
guessed_letters = []

for character in chosen_word:
    word_guess.append("_")

def fill(g):
    i = 0
    for char in chosen_word:
        if g == char:
            word_guess[i] = g
        i += 1

def print_progress():
    a = ""
    for char in word_guess:
        a += char
    return a

guess_count = 6

print("Your current progress is: " + print_progress())

while print_progress() != chosen_word and guess_count > 0:
    print(f"Attempts remaining: {guess_count}\n")
    print(f"Hangman: \n{hangman_art.stages[guess_count]}\n")
    guess = input("Please guess a letter! ").lower()
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue
    else:
        guessed_letters.append(guess)
        if guess in chosen_word:
            print("Right, this letter is in the chosen word!")
            fill(guess)
        else:
            print("Wrong, this letter is not in the chosen word!")
            guess_count -= 1

        print("Your current guess progress is: " + print_progress())

if guess_count < 1 and print_progress() != chosen_word:
    print(f"You lose!\n\n {hangman_art.stages[guess_count]}\n")
    print(f"The word was: {chosen_word}")
else:
    print("You win!\n")
