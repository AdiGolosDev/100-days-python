from turtle import Turtle

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

starting_position = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self, current_heading=EAST):
        self.snake_blocks = []
        self.current_heading = current_heading
        for pos in starting_position:
            snake_body = Turtle("square")
            snake_body.color("black")
            snake_body.penup()
            snake_body.goto(pos)
            self.snake_blocks.insert(0, snake_body)
        self.head = self.snake_blocks[len(self.snake_blocks)-1]

    def move(self):
         for block in self.snake_blocks:
            if block != self.snake_blocks[len(self.snake_blocks) - 1]:
                block.goto(self.snake_blocks[self.snake_blocks.index(block) + 1].position())
            else:
                self.head.forward(20)

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

