import random
from turtle import  Turtle

COLORS = ["blue","green","red","white","orange","pink"]
MOVING_DISTANCE = 10
INCREMENT = 10

class Car():
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVING_DISTANCE

    def create_car(self):
        rand = random.randint(1,6)
        if rand == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            y = random.randint(-230,230)
            new_car.goto(300,y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def leve_lup(self):
        self.car_speed +=INCREMENT

