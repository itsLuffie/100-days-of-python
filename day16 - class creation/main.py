from turtle import *

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")

timmy.setheading(90)
timmy.heading()
for i in range(100):
    timmy.forward(1)
timmy.left(90)
for i in range(100):
    timmy.forward(1)
timmy.left(90)
for i in range(100):
    timmy.forward(1)
timmy.left(90)
for i in range(100):
    timmy.forward(1)
my_screen = Screen()
my_screen.exitonclick()
