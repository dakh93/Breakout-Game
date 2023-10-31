from turtle import Screen
import time

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from block import Block


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
INITIAL_X_POSITION = -400
INITIAL_Y_POSITION = 200


def initialize_blocks():
    blocks = []
    x_list = [-340, -230, -120, -10, 100, 210, 320]
    y_list = [280, 255, 230, 205, 180]

    for i in x_list:
        for j in y_list:
            block = Block(i, j)
            blocks.append(block)
    return blocks


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()
paddle.change_position_to_player()

block_list = initialize_blocks()

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle.go_right, "Right")
screen.onkeypress(paddle.go_left, "Left")


while len(block_list) > 0:
    screen.update()
    # GAME OVER
    if ball.lives < 1: break

    ball.move()
    time.sleep(0.05)

    # Detect collision with left or right wall
    if ball.xcor() > 355 or ball.xcor() < -355:
        ball.bounce_x()

    # Detect collision with top wall
    if ball.ycor() > 290:
        ball.bounce_y()

    # # Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.xcor() < 355 or ball.distance(paddle) < 50 and ball.xcor() > -355:
        ball.bounce_y()

    # Detect paddle misses
    if ball.ycor() < -300:
        ball.reset_position()
        scoreboard.decrease_live()
        scoreboard.update_scoreboard()

    # Block collision check
    for i in block_list:
        if (i.ycor() - 20 <= ball.ycor() <= i.ycor() + 20) and (
                i.xcor() - 60 < ball.xcor() < i.xcor() + 60) and ball.dy > 0:
            i.goto(1000, 1000)
            ball.bounce_y()
            block_list.remove(i)
            scoreboard.point()

# Final update of screen
scoreboard.game_over()
scoreboard.update_scoreboard()

screen.update()

screen.exitonclick()
