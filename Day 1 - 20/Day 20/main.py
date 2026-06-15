from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("The Python Grows!!!")
screen.tracer(0)

gp = Snake() #stands for growing python
score = Score()
food = Food()

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

    if gp.out_of_bounds():
        score.reset()
        gp.reset()
    
    if gp.collides_with_self():
        score.reset()
        gp.reset()

    if gp.head.distance(food) < 15:
        food.move()
        gp.grow()
        score.increase_score()


screen.exitonclick()
