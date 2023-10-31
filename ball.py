import random
from turtle import Turtle

STARTING_POSITION_X = 0
STARTING_POSITION_Y = 0
DEFAULT_COLOR = "white"
SHAPE = "circle"
INITIAL_SPEED = 1

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(DEFAULT_COLOR)
        self.penup()
        self.x_move = 5
        self.y_move = -10
        self.dx, self.dy = 5, 6
        self.lives = 4
        self.move_speed = INITIAL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(STARTING_POSITION_X, STARTING_POSITION_Y)
        self.move_speed = INITIAL_SPEED
        self.decrease_live()
        self.bounce_x()

    def decrease_live(self):
        self.lives -= 1