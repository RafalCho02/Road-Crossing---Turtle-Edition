import turtle
from turtle import Turtle
import random
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = -5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car_numbers = []
        self.start_x = 300
        self.far_x = 45300
        self.move_speed = 0.1
    def create_cars(self):
        for car in range(1000):
            self.add_car()
            self.start_x += 45
    def car_reach_goal(self):
        random_y = random.randint(-240, 240)
        for car in self.car_numbers[1:]:
            if car.xcor() == -360:
                car.goto(x=self.far_x,y=random_y)
                self.far_x += 45
            if self.far_x > 90600:
                self.far_x = 45300
    def add_car(self):
        car = turtle.Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.color(random.choice(COLORS))
        random_y = random.randint(-240, 240)
        car.setposition(self.start_x, random_y)
        self.car_numbers.append(car)
        self.car_numbers.append(car)
        self.hideturtle()
    def car_move(self):
        for seg_num in range(len(self.car_numbers)):
            self.car_numbers[seg_num].forward(STARTING_MOVE_DISTANCE)
    def speed_up(self):
        self.move_speed *= 0.5