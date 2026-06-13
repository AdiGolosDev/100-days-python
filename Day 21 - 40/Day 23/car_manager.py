import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
SPAWN_CHANCE_PER_FRAME = 0.3

class Car(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(250, random.randint(-180, 180))

    def move_car(self, move_distance):
        self.goto(self.xcor() - move_distance, self.ycor())


class CarManager:
    
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def start_level(self, level=1):
        self.speed += (level - 1) * MOVE_INCREMENT

    def spawn_car(self):
        if random.random() < SPAWN_CHANCE_PER_FRAME:
            self.cars.append(Car())

    def move_cars(self):
        for car in self.cars:
            car.move_car(self.speed)

            if car.xcor() < -250:
                car.hideturtle()
