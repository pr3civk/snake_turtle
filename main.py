from turtle import Screen
from snake import Snake
from time import sleep
from food import Food
from score import Score


# Screen:
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python in snake in reverse")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")


# game
game_on = True
while game_on:
    score.write
    screen.update()
    snake.current_speed()
    snake.move()
    print(snake.snake_speed)
    # Detect collision with food

    if snake.head.distance(food) < 23:
        food.refresh()
        snake.extend()
        score.add_score()

    # Detect collision with walls
    if abs(snake.head.xcor()) > 294 or abs(snake.head.ycor()) > 294:
        sleep(0.2)
        score.game_reset()
        snake.reset()

    for segment in snake.snake_body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            sleep(0.2)
            score.game_reset()
            snake.reset()



screen.exitonclick()
