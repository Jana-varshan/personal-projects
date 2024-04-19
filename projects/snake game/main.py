from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()

screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("The Snake")
screen.tracer(0)
snake = Snake()
food = Food()
scr = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    snake.move_snake()

    # detect collision with food
    if (snake.blocklist[0]).distance(food) < 15:
        food.refresh()
        snake.extend()
        scr.increase_score()

    # detect collision with walls
    if (snake.blocklist[0]).xcor() > 280 or (snake.blocklist[0]).xcor() < -280 or (snake.blocklist[0]).ycor() > 250 or (
            snake.blocklist[0]).ycor() < -290:
        game_on = False
        scr.game_over()

    for i in range(3, len(snake.blocklist)):

        if (snake.blocklist[0]).distance(snake.blocklist[i]) < 15:
            game_on = False
            scr.game_over()

screen.exitonclick()
