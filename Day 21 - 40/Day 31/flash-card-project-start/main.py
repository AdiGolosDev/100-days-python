from tkinter import *
import pandas
import random
import os
import sys

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Inter"
BACK_BG = "#91c2af"
FRONT_BG = "#ffffff"
side = "front"
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

flashcards = data.to_dict(orient="records") # orient="records" makes dict like this: 
# {"French": word, "English": word}
current = {}

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

def turn_to_front():
    global current
    canvas.itemconfig(canvas_image, image=card_front)
    language_label.config(text="French", bg=FRONT_BG, fg=BACK_BG)
    word_label.config(text=current["French"], bg=FRONT_BG, fg=BACK_BG)

def turn_to_back():
    global current
    canvas.itemconfig(canvas_image, image=card_back)
    language_label.config(text="English", bg=BACK_BG, fg=FRONT_BG)
    word_label.config(text=current["English"], bg=BACK_BG, fg=FRONT_BG)

def flip():
    global side
    
    if side == "front":
        side = "back"
        turn_to_back()
    elif side == "back":
        side = "front"
        turn_to_front()

def next_card():
    global side
    global current
    current = random.choice(flashcards)
    side = "front"
    turn_to_front()

def right():
    flashcards.remove(current)
    pandas.DataFrame(flashcards).to_csv("data/words_to_learn.csv", index=False)
    next_card()
    
def wrong():
    next_card()

window = Tk()
window.title("Klokan's Anki Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file=resource_path("images/card_back.png"))
card_front = PhotoImage(file=resource_path("images/card_front.png"))
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=1, row=0)

language_label = Label(text="Klokan's Flashcards", font=(FONT, 40, "italic"), bg=FRONT_BG, fg=BACK_BG)
language_label.place(x=50, y=50)

word_label = Label(text="Words that you have\n   to guess appear here!", font=(FONT, 60), bg=FRONT_BG, fg=BACK_BG)
word_label.place(x=50, y=200)

wrong_img = PhotoImage(file=resource_path("images/wrong.png"))
right_img = PhotoImage(file=resource_path("images/right.png"))
switch_img = PhotoImage(file=resource_path("images/switch.png"))

button_frame = Frame(window, highlightthickness=0, bg=BACKGROUND_COLOR)
button_frame.grid(column=1, row=1, pady=50)

wrong_button = Button(button_frame, image=wrong_img, width=100, height=100, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong)
wrong_button.pack(side=LEFT, padx=50)

switch_button = Button(button_frame, image=switch_img, width=100, height=100, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR, command=flip)
switch_button.pack(side=LEFT, padx=50)

right_button = Button(button_frame, image=right_img, width=100, height=100, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong)
right_button.pack(side=LEFT, padx=50)

window.mainloop()
