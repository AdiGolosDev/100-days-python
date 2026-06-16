from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color("white")
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score}", align="center", font=("Arial", 22, "normal"))

    def update_score(self):
        write = False
        with open("highscore.txt") as file:
            if int(file.read()) < self.high_score:
                write = True
        
        if write:
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))

        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 22, "normal"))

    def reset(self):
        with open("highscore.txt") as file:
            if self.score > int(file.read()):
                self.high_score = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Score: {self.score}\nYour python has stopped growing", align="center", font=("Arial", 22, "normal"))
