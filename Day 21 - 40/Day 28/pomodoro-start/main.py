from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 
on = False
remaining_time = 0
def start():
    global on
    on = True
    timer()

def reset():
    global on
    global remaining_time
    on = False
    remaining_time = 0
    canvas.config(text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_work():
    count_down(WORK_MIN * 60)

def start_short_break():
    count_down(SHORT_BREAK_MIN * 60)

def start_long_break():
    count_down(LONG_BREAK_MIN * 60)
    reset()

def timer():
    while on:
        for _ in range(4):
            start_work()
            while True:
                if remaining_time <= 0:
                    break
            check_marks.config(text=check_marks.cget("text") + "✓")
            start_short_break()
        start_long_break()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def remaining_time_to_string(time):
    string = str(int(time/60))
    string += ":"
    string += str(time%60)
    return string

def count_down(count):
    canvas.config(text=remaining_time_to_string(remaining_time))
    remaining_time -= 1
    window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Program")
window.config(padx=100, pady=100, bg=YELLOW)

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 112, image=tomato_image)
canvas.create_text(100, 130, text=remaining_time_to_string(remaining_time), fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1, pady=20, padx=40)

timer = Label(text="Timer", fg="#000000", bg=YELLOW, font=(FONT_NAME, 48, "italic"))
timer.grid(column=1, row=0)

start_button = Button(text="start", fg="#000000", font=(FONT_NAME, 14, "italic"), command=reset, width=8, height=2, highlightthickness=2)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", fg="#000000", font=(FONT_NAME, 14, "italic"), command=reset, width=8, height=2, highlightthickness=2)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", font=(FONT_NAME, 60, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()
