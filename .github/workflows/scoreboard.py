from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=275)
        self.write(arg=f"Score = {self.score}", move=False, align="center", font=("Arial", 15, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score = {self.score}", move=False, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 15, "normal"))
