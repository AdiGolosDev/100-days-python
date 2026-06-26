import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index, row) in df.iterrows()}

on = True
while on:
    word = input("Please enter a word you would like translated into the nato phonetic alphabet: \n")
    if word == "/end":
        on = False
        break

    word_list = [letter.upper() for letter in word]
    try:
        word_nato_list = [f"{letter} = {dict[letter]}" for letter in word_list]
    except KeyError:
        print("Sorry, only use letters in the alphabet please.")
        continue

    for item in word_nato_list:
        print(item)
