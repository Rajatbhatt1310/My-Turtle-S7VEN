from turtle import Turtle, Screen
import random

is_race_on=False
screen = Screen()
screen.setup(width=500, height=700)

user_guess = screen.textinput(title="Make your bet for turtle",prompt="Which coloured turtle will win the race, make your bet for it\n" \
"The colors are : Yellow, Blue, Green, Orange, Purple, Red")

colors = ["red", 'green', 'blue', 'orange', 'purple', 'yellow']
y_positions = [-70,80,-40,50,-10,20]
all_turtles=[]

for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[turtle_index])
    t.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(t)

if user_guess:
    is_race_on=True

while is_race_on: 
    for turtles in all_turtles:
        if turtles.xcor()>230:
            is_race_on=False
            winning = turtles.pencolor() 
            if user_guess==winning:
                print(f"You have won the bet, the winning turtle is {winning} coloured !!!!!! ")
            else:
                print(f"OOPS!!! You have lost the bet, the winning turtle is {winning} coloured :( ")

        rand_dist = random.randint(0,10)
        turtles.forward(rand_dist)        

screen.exitonclick()
