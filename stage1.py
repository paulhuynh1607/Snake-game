from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

turtle = Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
food.refresh()
level = screen.textinput(title="Level", prompt="Easy;Normal;Hard;Extreme").lower()
minus_time = 0

game_is_on = True
if level == "easy":
    minus_time = 0.0001
elif level == "normal":
    minus_time = 0.001
elif level == "hard":
    minus_time = 0.01
elif level == "extreme":
    minus_time = 0.01
else:
    print("Invalid!")

while game_is_on:
    screen.update()
    time.sleep(snake.speed)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
        snake.speed -= minus_time

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()

        again = screen.textinput(title="Again", prompt="Do you want to play again? Yes or no.").lower()
        if again == "yes":
            scoreboard.reset_snake()
            snake.reset()
        elif again == "no":
            game_is_on = False

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            again = screen.textinput(title="Again", prompt="Do you want to play again? Yes or no.").lower()
            if again == "yes":
                scoreboard.reset_snake()
                snake.reset()
            elif again == "no":
                game_is_on = False


screen.exitonclick()
