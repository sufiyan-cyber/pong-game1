from turtle import Screen,Turtle
from another import Paddle
from bal import Ball
import time
from scoreboard import Scoreboard
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)

screen.tracer(0)
paddler=Paddle((350,0))
paddlel=Paddle((-350,0))

ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkeypress(paddler.go_up,"Up")
screen.onkeypress(paddler.go_down,"Down")
screen.onkeypress(paddlel.go_up,"w")
screen.onkeypress(paddlel.go_down,"s")



is_on=True

while is_on:
    screen.update()
    time.sleep(0.05)
    ball.movee()

    if ball.ycor()>300 or ball.ycor() <-300:
        ball.bounce_y()

    if ball.distance(paddler)<50 and ball.xcor()>340 or ball.distance(paddlel) <50 and ball.xcor()<-340:
        ball.bounce_x()

    if ball.xcor()>380:
        ball.reset_position()
        ball.bounce_x()
        score.l_score()


    if ball.xcor()<-380:
        ball.reset_position()
        ball.bounce_x()
        score.r_score()


screen.exitonclick()