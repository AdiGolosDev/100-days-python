import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. State Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")
state_names = states.state.to_list()

def make_text_turtle(x, y, state):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.write(state, align='center', font=('Arial', 8, 'normal'))

correct = 0
game_on = True
while game_on:
    if correct == 50:
        winning_turtle = turtle.Turtle()
        winning_turtle.penup()
        winning_turtle.hideturtle()
        winning_turtle.goto(0, 250)
        winning_turtle.write("You Guessed Them All!\nCongratulations, You Win!!!", align='center', font=('Arial', 20, 'normal'))
        break

    user_input = screen.textinput(title=f"{correct}/50 - Guess the State", prompt="What other states do you know?")
    if user_input is None:
        continue
    elif user_input.lower() == "end":
        game_on = False
        continue
    answer = user_input.title()

    if answer in state_names:
        x = states.loc[states.state == answer, "x"].item()
        y = states.loc[states.state == answer, "y"].item()
        make_text_turtle(x, y, answer)
        state_names.remove(answer)
        correct += 1

            





screen.exitonclick()
