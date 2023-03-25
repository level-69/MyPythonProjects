from turtle import Turtle
cod_list = [(0, 0), (-20, 0), (-40, 0)]
movement = 20


class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()

    def create_snake(self):
        for position in cod_list:
            self.add_segment(position)

    def add_segment(self, position):
        my_turtle = Turtle()
        my_turtle.shape("square")
        my_turtle.color("white")
        my_turtle.penup()
        my_turtle.goto(position)
        self.turtle_list.append(my_turtle)

    def extend(self):
        self.add_segment(self.turtle_list[-1].position())

    def move(self):
        for snake in range(len(self.turtle_list) - 1, 0, -1):
            new_xcor = self.turtle_list[snake - 1].xcor()
            new_ycor = self.turtle_list[snake - 1].ycor()
            self.turtle_list[snake].goto(new_xcor, new_ycor)
        self.turtle_list[0].forward(movement)

    def snake_control_up(self):
        if self.turtle_list[0].heading() != 270:
            self.turtle_list[0].setheading(90)

    def snake_control_down(self):
        if self.turtle_list[0].heading() != 90:
            self.turtle_list[0].setheading(270)

    def snake_control_left(self):
        if self.turtle_list[0].heading() != 0:
            self.turtle_list[0].setheading(180)

    def snake_control_right(self):
        if self.turtle_list[0].heading() != 180:
            self.turtle_list[0].setheading(0)
