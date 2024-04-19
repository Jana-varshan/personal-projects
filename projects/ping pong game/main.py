from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
from screen_split import Screen_line
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

r_pad = Paddle(350)

l_pad = Paddle(-350)

screen.listen()

screen.onkey(r_pad.up, "Up")
screen.onkey(r_pad.down, "Down")

screen.onkey(l_pad.up, "w")
screen.onkey(l_pad.down, "s")

ball = Ball()
scoreboard = ScoreBoard()
line=Screen_line()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_pad) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()
