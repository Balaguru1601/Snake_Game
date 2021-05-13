from turtle import Turtle

POS = [(0, 0), (0, -20), (0, -40)]
MOVE_POS = 20


class Snake:
    def __init__(self):
        self.snake_box = []
        self.create_snake()
        self.head = self.snake_box[0]

    def create_snake(self):
        for i in POS:
            self.add_snake(i)

    def add_snake(self, pos):
        tim = Turtle(shape='square')
        tim.color('white')
        tim.penup()
        tim.goto(pos)
        self.snake_box.append(tim)

    def extend(self):
        self.add_snake(self.snake_box[-1].pos())

    def move(self):
        for item in range(len(self.snake_box) - 1, 0, -1):
            new_pos = self.snake_box[item - 1].pos()
            self.snake_box[item].goto(new_pos)

        self.snake_box[0].forward(MOVE_POS)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
