# import tkinter better to use if you only use a few modules
from tkinter import *

window = Tk()
window.title("My first Tkinter GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # adding padding to all widgets

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()

# changing/updating properties
my_label["text"] = "New Text"
my_label.config(text="New Text Again")

my_label.config(padx=50, pady=50) # adding padding to specific widget

# Button
def button_clicked():
    text = input.get()
    my_label.config(text=text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click Me Instead", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)


# pack is bad for specific positioning
# place = precise positioning
# my_label.place(x=50, y=50)

# grid is relative to other components
my_label.grid(column=0, row=0) # start with thing you want on top left, then define other
                               # objects in regard to the starting object
# NOTE: cannot mix up grid and pack in same program



window.mainloop()
