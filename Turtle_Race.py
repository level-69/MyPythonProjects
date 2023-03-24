import turtle
from turtle import Turtle, Screen
import random


turtle.title("Turtle Race")


my_good_turtle = Turtle()
my_good_turtle.color("white")
color_list = ["red", "green", "purple", "blue"]
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
position_list = [-30, 30]
all_turtle = []

for _turtle in range(2):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(color_list[_turtle])
    my_turtle.left(90)
    my_turtle.penup()
    my_turtle.goto(position_list[_turtle], -230)
    all_turtle.append(my_turtle)


red_list = []
length_red_list = len(red_list)

green_list = []
length_green_list = len(green_list)

tap_by_red = 0
tap_by_green = 0


def move_forward1():
    global tap_by_red

    tap_by_red += 1
    all_turtle[0].forward(random.choice(number_list))
    y1 = all_turtle[0].ycor()
    red_list.append(y1)

    if y1 >= 230:
        print("Red win")
        print(f"Clicks by Red: {tap_by_red}")
        print(f"Clicks by Green: {tap_by_green}")
        turtle.bye()


def move_forward2():
    global tap_by_green

    tap_by_green += 1
    all_turtle[1].forward(random.choice(number_list))
    y2 = all_turtle[1].ycor()
    green_list.append(y2)
    # print(empty_list)
    if y2 > 230:
        print("Green win")
        print(f"Clicks by Red: {tap_by_red}")
        print(f"Clicks by Green: {tap_by_green}")
        turtle.bye()


screen = Screen()
screen.setup(width=500, height=500)
screen.listen()
screen.onkey(key="space", fun=move_forward1)
screen.onkey(key="0", fun=move_forward2)
screen.exitonclick()
