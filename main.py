from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            is_game_on = False
            scoreboard.game_over()
    # detect of player reached the Finish line
    if player.reached_finish_line():
        player.reset()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
