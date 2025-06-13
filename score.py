
from turtle import Turtle

FONT = ("Courier", 30, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(-250, 260)
        self.write(f"Score: {self.l_score}", False, align=ALIGNMENT, font=FONT)
        self.goto(250, 260)
        self.write(f"Score: {self.r_score}", False, align=ALIGNMENT, font=FONT)

    def update_l_score(self):
        self.l_score += 1
        self.update_scores()

    def update_r_score(self):
        self.r_score += 1
        self.update_scores()