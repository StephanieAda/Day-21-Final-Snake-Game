from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20,0), (-40, 0)]


class Snake(Turtle):
    snake_segment = 3

    def __init__(self):
        super().__init__()
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.penup()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
        lily = Turtle()
        lily.color('white')
        lily.shape('square')
        lily.penup()
        lily.goto(position)
        self.snake.append(lily)

    def extend(self):
        self.add_segments(self.snake[-1].position())

    def move(self):

        for segment in range((len(self.snake) - 1), 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.snake[0].setheading(270)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.snake[0].setheading(180)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
