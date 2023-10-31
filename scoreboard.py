from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 4
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-200, 307)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))
        self.goto(200, 307)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 20, "normal"))

    def point(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def decrease_live(self):
        self.clear()
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 100, "bold"))