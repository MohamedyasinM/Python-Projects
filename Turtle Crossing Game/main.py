from turtle import Screen
from Player import Player
from scoreboard import Score
from car import Car
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
car = Car()
score = Score()

screen.listen()

screen.onkey(player.move,key="Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()
    for c in car.all_cars:
        if c.distance(player) < 20:
            game_on = False
            score.game_over()

    if player.success():
        player.start()
        car.leve_lup()
        score.show_level()


screen.exitonclick()