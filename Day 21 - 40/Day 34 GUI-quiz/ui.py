from tkinter import *
from quiz_brain import QuizBrain
import sys
import os

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Klok Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=FONT)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Questions will appear here :)", font=FONT, fill=THEME_COLOR, anchor="center")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        false_img = PhotoImage(file=self.resource_path("images/false.png"))
        true_img = PhotoImage(file=self.resource_path("images/true.png"))

        self.true_button = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def answer_true(self):
        self.quiz.check_answer("true")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()

    def answer_false(self):
        self.quiz.check_answer("false")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You got {self.quiz.score}/{self.quiz.question_amount} right!")

    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.dirname(__file__), relative_path)
