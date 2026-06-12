from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.color("white")

    def update_score(self):
        self.clear()
        self.write(f"{self.left_score}          {self.right_score}", align="center", font=("Arial", 30, "normal"))