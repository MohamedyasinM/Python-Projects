from turtle import Turtle, Screen
import random

screen = Screen()
is_on = False

screen.setup(width=500,height=400)
s_input =screen.textinput(title="AAmai",prompt="which color are tou going to choose")

colors = ["red","blue","green","pink","orange","black","yellow"]
y = [-50,-100,0,50,100,150]
all_t = []

if s_input:
    is_on = True

for t in range (0,6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[t])
    tim.goto(x=-210,y=y[t])
    all_t.append(tim)


while is_on:
    for t in all_t:
        if t.xcor() > 230:
            wc = t.pencolor()
            if wc == s_input:
                print(f"You win.the winner is {wc}")
            else:
                print(f"You loose.the winner is {wc}")
            is_on = False
        a = random.randint(0, 10)
        t.fd(a)


screen.exitonclick()
