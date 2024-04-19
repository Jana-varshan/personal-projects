from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)


    def move(self):
        new_y=self.ycor()+MOVE_DISTANCE
        x=self.xcor()
        self.goto(x,new_y)

    def reset_pos(self):
        self.goto(STARTING_POSITION)



