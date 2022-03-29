from turtle import Turtle, Screen
import random

# Creating screen
screen = Screen()
# Fixing Screen size
screen.setup(width=500, height=400)
# Giving user a choice which color turtle will win race
choice = screen.textinput("Turtle Bet", 'Which rainbow colored turtle will win the race ? ')
# Range of colors in rainbow
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
# Creating seven turtle objects
t1 = Turtle(shape='turtle')
t2 = Turtle(shape='turtle')
t3 = Turtle(shape='turtle')
t4 = Turtle(shape='turtle')
t5 = Turtle(shape='turtle')
t6 = Turtle(shape='turtle')
t7 = Turtle(shape='turtle')
# Putting all turtle in the race
turtles = [t1, t2, t3, t4, t5, t6, t7]
# Setting x,y coordinates of turtles in the start
x = -230
y = 155
# turtle at their respective places
for i in range(len(turtles)):
    # choosing each turtle a unique color
    turtles[i].color(colors[i])
    turtles[i].penup()
    # making that turtle to goto their respective position
    turtles[i].goto(x, y)
    # Decreasing y because making all turtles be in same-line but same x position
    y = y - 50
# creating the ranges which turtles can move
len_movable = list(range(5, 15, 5))
flag = True
# starting race
while flag:
    for turtle in turtles:
        # making turtle to move a random distance
        turtle.forward(random.choice(len_movable))
        # if turtle reaches end point
        if turtle.xcor() >= 250:
            flag = False
            color_won = colors[turtles.index(turtle)]
            if color_won == choice:
                print("Yay you guessed correctly")
                break
            else:
                print(f'Your guess was {choice} colored turtle.But {color_won} turtle win the race')
                break