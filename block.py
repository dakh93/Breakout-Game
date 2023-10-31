import turtle
import random


class Block(turtle.Turtle):
    def __init__(self, xpos, ypos):
        super().__init__(shape='square')
        self.up()
        self.colors = ['red', 'blue', 'green', 'cyan', 'yellow', 'orange', 'purple']
        self.shapesize(1, 5)
        self.goto(xpos, ypos)
        self.color(random.choice(self.colors))