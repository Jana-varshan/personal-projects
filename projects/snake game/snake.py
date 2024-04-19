from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.blocklist = []
        self.create_snake()

    def create_snake(self):
        for i in positions:
            self.add_block(i)

    def add_block(self, i):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(i)
        self.blocklist.append(tim)

    def extend(self):
        self.add_block((self.blocklist[-1]).position())

    def move_snake(self):
        for i in range((len(self.blocklist) - 1), 0, -1):
            x = self.blocklist[i - 1].xcor()
            y = self.blocklist[i - 1].ycor()
            self.blocklist[i].goto(x, y)
        self.blocklist[0].forward(20)

    def up(self):
        if (self.blocklist[0]).heading() != down:
            (self.blocklist[0]).setheading(up)

    def down(self):
        if (self.blocklist[0]).heading() != up:
            (self.blocklist[0]).setheading(down)

    def left(self):
        if (self.blocklist[0]).heading() != right:
            (self.blocklist[0]).setheading(left)

    def right(self):
        if (self.blocklist[0]).heading() != left:
            (self.blocklist[0]).setheading(right)
