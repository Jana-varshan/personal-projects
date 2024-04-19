from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level_num = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-230, 260)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"level={self.level_num}", align="center", font=FONT)

    def increase_level(self):
        self.level_num += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
