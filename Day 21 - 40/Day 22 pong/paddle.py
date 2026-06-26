from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.xpos = x_position
        self.penup()
        self.hideturtle() 
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.xpos, 0)
        self.showturtle()

    def up(self):
        if self.ycor() < 250:
            self.goto(self.xpos, self.ycor() + 20)

    def down(self):
        if self.ycor() > -250:
            self.goto(self.xpos, self.ycor() - 20)
