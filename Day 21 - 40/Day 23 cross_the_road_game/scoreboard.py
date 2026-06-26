from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.color("black")
        self.level = 1

    def update_scoreboard(self, cleared_level=False):
        self.clear()
        if cleared_level:
            self.level += 1
        
        self.write(f"Level: {self.level}", font=FONT)
    
    def lose_game(self):
        self.clear()
        self.goto(0,0)
        self.write(f"You lost on level {self.level}",align="center", font=FONT)
