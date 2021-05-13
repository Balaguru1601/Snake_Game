from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()

screen = Screen()
food = Food()
score = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        snake.extend()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        score.game_over()
        is_game_on = False

    for body in snake.snake_box[3:]:
        if snake.head.distance(body) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
