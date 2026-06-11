from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.score = 0
        self.write(f"Score: {self.score}", align="center", font=("Arial", 22, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 22, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Score: {self.score}\nYour python has stopped growing", align="center", font=("Arial", 22, "normal"))
