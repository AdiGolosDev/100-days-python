from turtle import Screen, Turtle
import time
from snake import Snake

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("The Python Grows!!!")
screen.tracer(0)

screen.update()

gp = Snake()

screen.listen()
screen.onkey(gp.up, "Up")
screen.onkey(gp.down, "Down")
screen.onkey(gp.left, "Left")
screen.onkey(gp.right, "Right")

screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    gp.move()

screen.exitonclick()
