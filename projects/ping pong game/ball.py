from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.move_y = 10
        self.move_x = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.move_x
        y = self.ycor() + self.move_y
        self.goto(x, y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.99

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.move_x *= -1
