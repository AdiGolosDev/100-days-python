from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

directions = [0, 90, 180, 270]

klokan = Turtle()
klokan.shape("turtle")
klokan.width(3)

def draw_dashed_line():
    for i in range(4):
        klokan.right(90)
        for i in range(10):
            klokan.pendown()
            klokan.forward(10)
            klokan.penup()
            klokan.forward(10)

def change_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_gons():   #3 - 22 gons because everything ends on gon(pentagon, hexagon...)
    i = 3
    while i < 23:
        angle = 360 / i
        for _ in range(i):
            klokan.right(angle)
            klokan.forward(50)
        klokan.color(change_color())
        i += 1

def random_walk():
    for _ in range(200):
        klokan.color(change_color())
        klokan.forward(22)
        klokan.setheading(random.choice(directions))

def draw_spirograph(amount):
    for _ in range(amount):
        klokan.color(change_color())
        klokan.circle(100)
        klokan.setheading(klokan.heading() + 360 / amount)
        

klokan.speed(0)
draw_spirograph(100)

screen.exitonclick()
