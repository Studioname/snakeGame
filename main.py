from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)
game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#detect collision with food using distance

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increment_score()

#detect collision on wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset_self()
        scoreboard.reset_score()

#detect collision with tail

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_self()
            scoreboard.reset_score()

screen.exitonclick()


# class GameState:
#     def __init__(self):
#         self.game_is_on = False
#
#     def start(self):
#         self.game_is_on = True
#
#     def stop(self):
#         self.game_is_on = False
#
#     @property
#     def is_on(self):
#         return self.game_is_on
#
#
# class Snake:
#     def __init__(self, game_state):
#         self.game_state = game_state
#
#     def tick(self):
#         if self.game_state.is_on:
#             ...
#
#
# game_state = GameState()
# game_state.start()
#
# snake = Snake(game_state=game_state)