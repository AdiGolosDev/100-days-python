from tkinter import *
import random
import os
import sys

BACKGROUND_COLOR = "#B1DDC6"

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

window = Tk()
window.title("Klokan's Anki Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back = PhotoImage(file=resource_path("images/card_back.png"))
card_front = PhotoImage(file=resource_path("images/card_front.png"))
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=1, row=0)

a = input("please say y if you would like to switch the card: ")

if a == "y":
    canvas.itemconfig(canvas_image, image=card_back)


window.mainloop()
