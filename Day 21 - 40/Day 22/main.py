from turtle import Turtle, Screen
from score import Score
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Python pong")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
score = Score()
score.update_score("")

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

net = Turtle()
net.penup()
net.hideturtle()
net.goto(0,-320)
net.left(90)
net.color("white")
while net.ycor() != 320:
    net.pendown()
    net.forward(20)
    net.penup()
    net.forward(20)

speed = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(speed)
    ball.move()

    if ball.distance(r_paddle) < 20 or ball.distance(l_paddle) < 20:
        ball.x_move *= -1
        speed *= 0.95
    
    if ball.xcor() > 370:
        score.update_score("left")
        ball.restart()
        speed = 0.9
        time.sleep(0.5)
    elif ball.xcor() < -370:
        score.update_score("right")
        ball.restart()
        speed = 0.1
        time.sleep(0.5)

screen.exitonclick()
