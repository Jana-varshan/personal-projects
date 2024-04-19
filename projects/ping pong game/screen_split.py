from turtle import Turtle

class Screen_line(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.pensize(4)
        self.goto(0,-300)
        self.setheading(90)
        self.line()

    def line(self):
        for i in range(0,31):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)