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

    def move(self, heading=None):
         if heading != None:
             self.current_heading = heading
         for block in self.snake_blocks:
            if block != self.snake_blocks[len(self.snake_blocks) - 1]:
                block.goto(self.snake_blocks[self.snake_blocks.index(block) + 1].position())
            else:
                block.setheading(self.current_heading)
                block.forward(20)
                