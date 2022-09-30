import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Road Crossing - Turtle Edition')
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()
car.create_cars()

screen.listen()
screen.onkey(player.move,"Up")

WINNING_COLORS = ['green', 'blue', 'purple']

game_is_on = True
while game_is_on:
    time.sleep(car.move_speed)
    screen.update()
    car.car_move()
    car.car_reach_goal()
    scoreboard.update_scoreboard()
    if player.ycor() >= 260:
        time.sleep(0.1)
        screen.bgcolor(random.choice(WINNING_COLORS))
        time.sleep(0.1)
        screen.bgcolor('white')
        player.achieve_line()
        scoreboard.increase_score()
        car.speed_up()
    for cars in car.car_numbers[1:]:
        if player.distance(cars) < 20:
            scoreboard.game_over()
            screen.bgcolor('red')
            game_is_on = False
screen.exitonclick()