from turtle import Turtle,Screen
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove=10
        self.ymove=10
    def movee(self):
        new_x= self.xcor() +self.xmove
        new_y=self.ycor() +self.ymove
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.ymove  *=-1

    def bounce_x(self):
        self.xmove *=-1

    def reset_position(self):
        self.goto(0,0)