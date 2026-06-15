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
        self.create_snake()
        self.head = self.snake_blocks[len(self.snake_blocks)-1]

    def create_snake(self):
        for pos in starting_position:
            self.add_block(pos)

    def add_block(self, position):
        snake_body = Turtle("square")
        snake_body.color("black")
        snake_body.penup()
        snake_body.goto(position)
        self.snake_blocks.insert(0, snake_body)

    def move(self):
         for block in self.snake_blocks:
            if block != self.snake_blocks[len(self.snake_blocks) - 1]:
                block.goto(self.snake_blocks[self.snake_blocks.index(block) + 1].position())
            else:
                self.head.forward(20)
            block.showturtle()

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

    def grow(self):
        snake_body = Turtle("square")
        snake_body.hideturtle()
        snake_body.color("black")
        snake_body.penup()
        self.snake_blocks.insert(0, snake_body)

    def out_of_bounds(self):
        if -290 > self.head.xcor() or self.head.xcor() > 290:
            return True
        elif -290 > self.head.ycor() or self.head.ycor() > 290:
            return True
        else:
            return False
    
    def collides_with_self(self):
        for block in self.snake_blocks[:-1]:
            if self.head.distance(block) < 10:
                return True
        return False
    
    def reset(self):
        for block in self.snake_blocks:
            block.goto(1000, 1000)
            block.hideturtle()
            
        self.snake_blocks.clear()
        self.create_snake()
        self.head = self.snake_blocks[len(self.snake_blocks)-1]

        