from turtle import Screen, Turtle
import time

EAST = 0
SOUTH = 270
WEST = 180
NORTH = 90

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("The Python Grows!!!")
screen.tracer(0)

snake_blocks = []
starting_position = [(0, 0), (-20, 0), (-40, 0)]

screen.update()

for pos in starting_position:
    snake_body = Turtle("square")
    snake_body.color("black")
    snake_body.penup()
    snake_body.goto(pos)
    snake_blocks.insert(0, snake_body)
    screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    for block in snake_blocks:
        if block != snake_blocks[len(snake_blocks) - 1]:
            block.goto(snake_blocks[snake_blocks.index(block) + 1].position())
        else:
            block.forward(20)
            block.left(90)




screen.exitonclick()