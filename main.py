from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput("Turtle Bet", 'Which rainbow colored turtle will win the race ? ')

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
t1 = Turtle(shape='turtle')
t2 = Turtle(shape='turtle')
t3 = Turtle(shape='turtle')
t4 = Turtle(shape='turtle')
t5 = Turtle(shape='turtle')
t6 = Turtle(shape='turtle')
t7 = Turtle(shape='turtle')
turtles = [t1, t2, t3, t4, t5, t6, t7]
x = -230
y = 155
for i in range(len(turtles)):
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x, y)
    y = y - 50
len_movable = list(range(5, 15, 5))
flag = True
while flag:
    for turtle in turtles:
        turtle.forward(random.choice(len_movable))
        if turtle.xcor() >= 250:
            flag = False
            color_won = colors[turtles.index(turtle)]
            if color_won == choice:
                print("Yay you guessed correctly")
                break
            else:
                print(f'Your guess was {choice} colored turtle.But {color_won} turtle win the race')
                break