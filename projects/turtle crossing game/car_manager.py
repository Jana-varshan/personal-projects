from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():


    def __init__(self):
        self.cars=[]



    def create_cars(self):

        random_slow=random.randint(1,7)
        if random_slow==1:
            car=Turtle("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()


            car.color(random.choice(COLORS))
            y=random.randint(-250,250)
            car.goto(300,y)
            self.cars.append(car)


    def move_cars(self):

        for i in self.cars:
            i.backward(STARTING_MOVE_DISTANCE)

    def inc_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE +=MOVE_INCREMENT