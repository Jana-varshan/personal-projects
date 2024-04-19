from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.scorenum = 0
        self.color("white")
        self.penup()

        self.hideturtle()
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        self.write(f"Score={self.scorenum}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.scorenum += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
