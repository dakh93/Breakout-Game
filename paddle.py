from turtle import Turtle

POSITION_X = 0
POSITION_Y = -250


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.create_dimensions()

    def create_dimensions(self):
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def change_position_to_player(self):
        self.penup()
        self.setposition(x=POSITION_X, y=POSITION_Y)

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < 345:
            self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > -345:
            self.goto(new_x, self.ycor())