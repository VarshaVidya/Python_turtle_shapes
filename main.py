
import random
from turtle import Turtle,Screen

My_turtle = Turtle()
My_turtle.shape("turtle")


colours=["red","medium slate blue","medium sea green","tomato",
         "crimson","dark slate blue",
         "gold","dark slate gray","chocolate",
         "black"]

def shape(num_sides):
    for _ in range(num_sides):
        My_turtle.forward(100)
        My_turtle.right(360/num_sides)
for i in range(3,11):
    shape(i)
    My_turtle.color(random.choice(colours))

my_screen = Screen()
my_screen.exitonclick()

