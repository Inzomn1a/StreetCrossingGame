from turtle import Turtle
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def player_move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_player_location(self):
        self.setposition(STARTING_POSITION)
        time.sleep(1.5)
