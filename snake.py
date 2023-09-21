from turtle import Turtle, position
from time import sleep


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.speed("fastest")
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for _ in range(3):
            self.add_segment(position)

    def add_segment(self, position):
        sx = 0
        segment = Turtle("square")
        segment.up()
        segment.goto(x=sx, y=0)
        sx -= 20
        self.snake_body.append(segment)
        segment.color("black")
        segment.color("white")

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def current_speed(self, snake_speed=0.1):
        self.snake_speed = snake_speed
        sleep(self.snake_speed)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    # #def accelerate(self):
    #     self.snake_speed -= 0.02
    #     return self.snake_speed
