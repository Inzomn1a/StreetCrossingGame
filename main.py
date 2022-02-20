import turtle
from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player_score = 0
screen = Screen()
screen.tracer(0)
scoreboard = Scoreboard(player_score)
screen.bgcolor("grey")
player = Player()
cars_manager = CarManager()
screen.setup(width=600, height=600)
screen.listen()

car_spawn_amount = 14
car_start_speed = 0
car_speed_increment = 5
car_spawn_counter = 0
all_cars = []

# GameLoop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if car_spawn_counter < car_spawn_amount:  # THIS GETS SKIPPED ONCE CARS ARE SPAWNED
        turtle.write("Standby.\nBuilding world", align="center", font=("Arial", 25, "normal"))
        turtle.hideturtle()
        all_cars.append(cars_manager.spawn_new_car())
        car_spawn_counter += 1

    # Unlock player controls once all cars are spawned
    if car_spawn_counter == car_spawn_amount:
        turtle.clear()
        screen.onkey(player.player_move_up, "w")
        screen.onkey(player.player_move_up, "Up")

    # check carCollission with player
    for car in all_cars:
        cars_manager.move_cars_left(car, car_start_speed, car_speed_increment)
        if car.distance(player) < 20:
            player_score = 0
            scoreboard.update_scoreboard(player_score)
            car_speed_increment = 5
            car_start_speed = 0
            player.reset_player_location()
    # Player reached finish line
    if player.ycor() >= 280:
        player_score += 1
        scoreboard.update_scoreboard(player_score)
        car_speed_increment += 5
        player.reset_player_location()
