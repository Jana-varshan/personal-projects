import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
car=CarManager()
score=Scoreboard()

# movement
screen.onkey(player.move,"Up")
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    car.create_cars()
    car.move_cars()


    if player.ycor()>280:
        player.reset_pos()
        car.inc_speed()
        score.increase_level()

    #detect collision

    for i in car.cars:
        if i.distance(player)<30:
            score.game_over()
            game_is_on=False


screen.exitonclick()
