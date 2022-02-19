import turtle
from turtle import Screen
from player import Player
import time
from player import Player
from car_manager import CarManager
import itertools
from scoreboard import Scoreboard

player_score = 0
screen = Screen()
scoreboard = Scoreboard(player_score)
screen.bgcolor("grey")
player = Player()
cars_manager = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
car_spawn_amount = 10

# GameLoop
game_is_on = True
car_spawn_counter = 0
all_cars = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if car_spawn_counter < car_spawn_amount:  # THIS GETS SKIPPED ONCE CARS ARE SPAWNED
        all_cars.append(cars_manager.spawn_new_car())
        car_spawn_counter += 1

    # Unlock player controls once all cars are spawned
    if car_spawn_counter == car_spawn_amount:
        screen.onkey(player.player_move_up, "w")
        screen.onkey(player.player_move_up, "Down")

    # check carCollission with player
    for car in all_cars:
        cars_manager.move_cars_left(car)
        if car.distance(player) < 30:
            print("Death")
            time.sleep(1)
    # Player reached finish line
    if player.ycor() == 280:
        player_score += 1
        scoreboard.update_scoreboard(player_score)
        print("YOU WON!")
        time.sleep(1)




