from turtle import Turtle, Screen
from score import Score
from paddle import Paddle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Python pong")

r_paddle = Paddle(350)
l_paddle = Paddle(-350)

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

score = Score()
score.update_score()

screen.exitonclick()
