from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=500, height=300)
window.config(padx=120, pady=120)

km = 0
def button_clicked():
    miles = int(input.get())
    km = miles * 1.6
    output_text.config(text=km)

input = Entry(text="0", width=5)
input.grid(column=1, row=0)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)

is_equal_text = Label(text="is equal to")
is_equal_text.grid(column=0, row=1)

output_text = Label(text=km)
output_text.grid(column=1, row=1)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
