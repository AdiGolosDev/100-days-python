import turtle
import pandas

# screen construction
screen = turtle.Screen()
screen.title("U.S. State Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# reads csv file using pandas; makes list for state names
states = pandas.read_csv("50_states.csv")
state_names = states.state.to_list()

# makes turtle for displaying text for correctly guessed state
def make_text_turtle(x, y, state):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.write(state, align='center', font=('Arial', 8, 'normal'))

# game on loop
correct = 0
game_on = True
while game_on:
    # once all 50 states are guessed, makes congratulations text
    if correct == 50:
        winning_turtle = turtle.Turtle()
        winning_turtle.penup()
        winning_turtle.hideturtle()
        winning_turtle.goto(0, 250)
        winning_turtle.write("You Guessed Them All!\nCongratulations, You Win!!!", align='center', font=('Arial', 20, 'normal'))
        break
    
    # gets user input and turns it into Title Case
    user_input = screen.textinput(title=f"{correct}/50 - Guess the State", prompt="What other states do you know?")
    if user_input is None:
        continue
    elif user_input.lower() == "end":
        game_on = False
        continue
    answer = user_input.title()

    # if not already guessed, makes turtle and increments correct score
    if answer in state_names:
        x = states.loc[states.state == answer, "x"].item()
        y = states.loc[states.state == answer, "y"].item()
        make_text_turtle(x, y, answer)
        state_names.remove(answer)
        correct += 1

screen.exitonclick()
