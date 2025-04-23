from turtle import  Turtle

STARTING_POSITION = (0,-260)
MOVE_DISTANCE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("brown")
        self.start()

    def start(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def success(self):
        if self.ycor() == FINISH_LINE:
            return True
        else:
            return False


