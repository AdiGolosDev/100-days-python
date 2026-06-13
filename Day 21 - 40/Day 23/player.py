from turtle import Turtle
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def check_win(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            time.sleep(1)
            return True
        else:
            return False
