from turtle import Turtle

FONT = ("Courier",18,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.color("white")
        self.on_write()

    def on_write(self):
        self.goto(-250, 250)
        self.write(f"LEVEL {self.level}", align="left", font=FONT)


    def show_level (self):
        self.level+=1
        self.clear()
        self.on_write()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)




