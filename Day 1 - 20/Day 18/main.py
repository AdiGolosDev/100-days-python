from turtle import Turtle, Screen

klokan = Turtle()
klokan.shape("turtle")
klokan.color("green")
for i in range(4):
    klokan.right(90)
    for i in range(10):
        klokan.pendown()
        klokan.forward(10)
        klokan.penup()
        klokan.forward(10)
        




screen = Screen()
screen.exitonclick()
