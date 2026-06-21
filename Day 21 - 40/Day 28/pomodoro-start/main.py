from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#268b3f"
DARK_GREEN = "#0a501c"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    reps += 1
    if reps >= 8:
        start_long_break()
    elif reps % 2 == 0:
        start_short_break()
    else:
        start_work()

def start_work():
    timer.config(text="Time to Get Shit Done!", fg=RED)
    count_down(WORK_MIN * 60)

def start_short_break():
    timer.config(text=" # Short Break Time # ", fg=GREEN)
    check_marks.config(text=check_marks.cget("text") + "✓")
    count_down(SHORT_BREAK_MIN * 60)

def start_long_break():
    check_marks.config(text=check_marks.cget("text") + "✓")
    timer.config(text="Congratulations!\nYou must've done\nsomething useful today!", fg=DARK_GREEN, font=(FONT_NAME, 28, "italic"))
    count_down(LONG_BREAK_MIN * 60)
    reset()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def remaining_time_to_string(time):
    colon = ":"
    if time % 2 == 1:
        colon = " "
    min = int(time/60)
    if min <= 9:
        string = "0" + str(min) + colon
    else:
        string = str(min) + colon
    
    sec = time % 60
    if sec <= 9:
        string += "0" + str(sec)
    else:
        string += str(sec)
    return string

def count_down(count):
    if count > 0:
        canvas.itemconfig(timer_text, text=remaining_time_to_string(count))
        window.after(1000, count_down, count - 1)
    elif count == 0:
        start()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Program")
window.config(padx=50, pady=100, bg=YELLOW, width=600, height=500)

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text=remaining_time_to_string(0), fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1, pady=20, padx=40)

timer = Label(text="         Timer        ", fg="#000000", bg=YELLOW, font=(FONT_NAME, 48, "italic"))
timer.grid(column=1, row=0)

start_button = Button(text="start", fg="#000000", font=(FONT_NAME, 14, "italic"), command=start, width=8, height=2, highlightthickness=2)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", fg="#000000", font=(FONT_NAME, 14, "italic"), command=reset, width=8, height=2, highlightthickness=2)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", font=(FONT_NAME, 60, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(column=1, row=3)

window.mainloop()
