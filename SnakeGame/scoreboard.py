from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("arial", 18, "normal"))
        self.hideturtle()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("arial", 24, "normal"))

    def inc_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("arial", 18, "normal"))
