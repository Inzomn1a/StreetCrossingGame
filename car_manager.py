from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
all_cars = []


class CarManager:
    def spawn_new_car(self):
        """Spawn Car at random location"""
        new_car = Turtle("square")
        new_car.penup()
        new_car.shapesize(1, 2)
        new_car.setheading(180)
        random_y_spawn = random.randrange(-220, 280, 20)
        random_x_spawn = random.randrange(-280, 280, 20)
        random_color = random.choice(COLORS)
        new_car.color(random_color)
        new_car.goto(random_x_spawn, random_y_spawn)
        all_cars.append(new_car)
        return new_car

    def move_cars_left(self, car, car_start_speed, speed_increment):
        """move cars to the left. and respawn on the right, if offscreen"""
        car.forward(car_start_speed + speed_increment)
        if car.xcor() < -320:
            car.setx(320)
