from tkinter import *
import random
import os
import sys

FONT = "Inter"
BG_COLOR = "#313244"
LAYER_COLOR = "#45475a"
TEXT_COLOR = "#cdd6f4"

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_entry():
    pass

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Klokan Password Manager")
window.config(padx=20, pady=30, bg=BG_COLOR)

logo = PhotoImage(file=resource_path("pass_man_logo.png"))
canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BG_COLOR)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0, padx=100)

# ----- Labels ----- #
web_label = Label(text="Website:", font=(FONT, 14), bg=BG_COLOR, fg=TEXT_COLOR)
web_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:", font=(FONT, 14), bg=BG_COLOR, fg=TEXT_COLOR)
user_label.grid(column=0,row=2)

pass_label = Label(text="Password:", font=(FONT, 14), bg=BG_COLOR, fg=TEXT_COLOR)
pass_label.grid(column=0, row=3)

# ----- Entries ----- #
web_entry = Entry(width=36, font=(FONT, 12), bg=LAYER_COLOR, fg=TEXT_COLOR)
web_entry.grid(column=1, row=1, pady=4)

user_entry = Entry(width=36, font=(FONT, 12), bg=LAYER_COLOR, fg=TEXT_COLOR)
user_entry.grid(column=1, row=2, pady=4)

pass_entry = Entry(width=36, font=(FONT, 12), bg=LAYER_COLOR, fg=TEXT_COLOR)
pass_entry.grid(column=1, row=3, pady=4)

# ----- Buttons ----- #
add_button = Button(text="Add", font=(FONT, 12), command=add_entry, width=6, height=1, highlightthickness=1)
add_button.grid(column=0, row=4)

button_frame = Frame(window, highlightthickness=0, bg=BG_COLOR)
button_frame.grid(column=1, row=4, pady=8)

generate_short_button = Button(button_frame, text="Create Short Password", font=(FONT, 12), command=generate_password, width=14, height=1, highlightthickness=1)
generate_short_button.pack(side=LEFT, padx=2)

generate_long_button = Button(button_frame, text="Create Long Password", font=(FONT, 12), command=generate_password, width=14, height=1, highlightthickness=1)
generate_long_button.pack(side=LEFT, padx=2)

# ----- Search ----- #
search_frame = Frame(window, highlightthickness=0, bg=BG_COLOR)
search_frame.grid(column=2, row=1, rowspan=4)

search_label = Label(search_frame, text="Search Previous Entries", font=(FONT, 16), bg=BG_COLOR, fg=TEXT_COLOR)
search_label.pack(anchor=W)

search_entry = Entry(search_frame, width=24, font=(FONT, 12), bg=LAYER_COLOR, fg=TEXT_COLOR)
search_entry.pack(anchor=W, pady=8)

result_frame_user = Frame(search_frame, highlightthickness=0, bg=BG_COLOR)
result_frame_user.pack(anchor=W)

result_frame_pass = Frame(search_frame, highlightthickness=0, bg=BG_COLOR)
result_frame_pass.pack(anchor=W)

search_result_user = Label(result_frame_user, text="Email/Username:", font=(FONT, 10, "underline"), bg=BG_COLOR, fg=TEXT_COLOR)
search_result_user.pack(anchor=W)
search_result_user_text = Label(result_frame_user, text="searched email/username", font=(FONT, 12), bg=BG_COLOR, fg=TEXT_COLOR)
search_result_user_text.pack()

search_result_pass = Label(result_frame_pass, text="Password:", font=(FONT, 10, "underline"), bg=BG_COLOR, fg=TEXT_COLOR)
search_result_pass.pack(anchor=W)
search_result_pass_text = Label(result_frame_pass, text="searched pass", font=(FONT, 12), bg=BG_COLOR, fg=TEXT_COLOR)
search_result_pass_text.pack()


window.mainloop()
