from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.lscore=0
        self.rscore=0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.lscore}",align="center",font=("courier",80,"normal"))
        self.goto(100,200)
        self.write(f"{self.rscore}",align="center",font=("courier",80,"normal"))

    def l_score(self):
        self.lscore +=1
        self.updatescore()

    def r_score(self):
        self.rscore +=1
        self.updatescore()
