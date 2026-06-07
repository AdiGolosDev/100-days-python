from turtle import Turtle, Screen
import random

screen = Screen()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

def draw_end_line():
    ref = Turtle(visible=False)
    ref.penup()
    ref.goto(x=225, y=175)
    ref.pendown()
    ref.width(5)
    ref.right(90)
    ref.forward(350)

draw_end_line()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle Racing, Make your bet", prompt="Which turtle will win?")
print(f"You have bet on {user_bet}")

ypos = 100

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-200, y=ypos)
    ypos -= 40
    turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 225:
            race_on = False
            winning_color = turtle.pencolor()

print(f"The winner is {winning_color} turtle!")

if winning_color == user_bet:
    print("Congratulations! You won the bet!")
else:    
    print("Sorry, you lost the bet. Better luck next time!")

screen.exitonclick()
