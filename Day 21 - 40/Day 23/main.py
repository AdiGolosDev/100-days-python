import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cm = CarManager()
level = 1
cm.start_level(level)
scoreboard.update_scoreboard(False)

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cm.spawn_car()
    cm.move_cars()
    screen.update()
    for car in cm.cars:
        if player.distance(car) < 10:
            game_is_on = False
            scoreboard.lose_game()

    screen.update()
    if player.check_win():
        level += 1
        scoreboard.update_scoreboard(True)
        cm.start_level(level)


screen.exitonclick()
