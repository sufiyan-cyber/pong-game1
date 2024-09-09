from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.pos=pos
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

        self.goto(pos)

    def go_up(self):
        new_x = self.xcor()
        new_y = self.ycor() + 40
        self.goto(new_x, new_y)

    def go_down(self):

        new_x = self.xcor()
        new_y = self.ycor() - 40
        self.goto(new_x, new_y)






