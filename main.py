from turtle import Screen
from player import Player
import time
from player import Player
from car_manager import CarManager
import itertools
from scoreboard import Scoreboard

screen = Screen()
player = Player()
cars_manager = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.player_move_up, "w")
screen.onkey(player.player_move_up, "Down")


game_is_on = True
car_spawn_counter = 0
all_cars = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if car_spawn_counter < 10:
        all_cars.append(cars_manager.spawn_new_car())  # RETURNS 'newCar' and adds to list
        car_spawn_counter += 1
        print(all_cars)
    for car in all_cars:
        cars_manager.move_cars_left(car)



