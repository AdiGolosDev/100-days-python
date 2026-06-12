from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.shape("circle")
        self.penup()
        self.color("white")

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

    def restart(self):
        self.goto(0,0)
        