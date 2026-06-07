from turtle import Turtle, Screen

klokan = Turtle()
screen = Screen()

def move_forward():
    klokan.forward(10)

def move_backward():
    klokan.backward(10)

def move_left():
    klokan.left(10)

def move_right():
    klokan.right(10)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=klokan.clear)

screen.exitonclick()