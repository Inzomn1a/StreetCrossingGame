import turtle
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self, player_score):
        super().__init__()
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.goto(-250, 270)
        self.scoreboard.hideturtle()
        self.scoreboard.write(f"Level: {player_score}", align="center", font=("Arial", 25, "normal"))

    def update_scoreboard(self, player_score):
        self.scoreboard.clear()
        self.scoreboard.write(f"Level: {player_score}", align="center", font=("Arial", 25, "normal"))
