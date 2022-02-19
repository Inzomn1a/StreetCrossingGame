from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
all_cars = []


class CarManager(Turtle):
    """Spawn Car at random location"""
    def __init__(self):
        super().__init__()


    def spawn_new_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(1, 2)
        new_car.setheading(180)
        random_y_spawn = random.randrange(-250, 280, 20)
        random_x_spawn = random.randrange(-280, 280, 20)
        random_color = random.choice(COLORS)
        new_car.color(random_color)
        new_car.goto(random_x_spawn, random_y_spawn)
        all_cars.append(new_car)
        return new_car


    def move_cars_left(self, car):
        """move car to the left. and respawn on the right if offscreen"""
        car.forward(STARTING_MOVE_DISTANCE)
        if car.xcor() < -320:
            car.setx(320)

    # def check_player_collision(self, player_position):
    #     if self.distance(player_position) < 50:
    #         print("Death")
