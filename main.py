import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
SPEED = 0.1


def game():

    _screen = Screen()
    _screen.setup(600, 600)
    _screen.bgcolor("black")
    _screen.tracer(0)

    snake = Snake()
    food = Food()
    score = ScoreBoard()
    _screen.listen()
    _screen.onkey(key="Up", fun=snake.snake_control_up)
    _screen.onkey(key="Down", fun=snake.snake_control_down)
    _screen.onkey(key="Left", fun=snake.snake_control_left)
    _screen.onkey(key="Right", fun=snake.snake_control_right)
    _screen.onkey(key="w", fun=snake.snake_control_up)
    _screen.onkey(key="s", fun=snake.snake_control_down)
    _screen.onkey(key="a", fun=snake.snake_control_left)
    _screen.onkey(key="d", fun=snake.snake_control_right)

    on = True
    while on:
        _screen.update()
        time.sleep(SPEED)

        snake.move()
        if snake.turtle_list[0].distance(food) < 15:
            food.refresh()
            snake.extend()
            score.inc_score()

        if snake.turtle_list[0].xcor() > 280 or snake.turtle_list[0].xcor() < -280 \
                or snake.turtle_list[0].ycor() > 280 or snake.turtle_list[0].ycor() < -280:
            on = False
            score.game_over()

        for item in snake.turtle_list[2:]:
            if snake.turtle_list[0].distance(item) < 10:
                on = False
                score.game_over()

    _screen.exitonclick()


def reset_screen():
    turtle.resetscreen()
    game()


screen = Screen()
screen.listen()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.onkey(key="r", fun=reset_screen)
screen.exitonclick()
