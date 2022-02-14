import imp
from turtle import Screen
import time 
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen  = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up',fun=snake.move_up)
screen.onkey(key='Down',fun=snake.move_down)
screen.onkey(key='Right',fun=snake.move_right)
screen.onkey(key='Left',fun=snake.move_left)







screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.snake_move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.increase_score()
        snake.snake_grow_up()
    
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 \
        or snake.head.ycor() >300 or snake.head.ycor() <-280:
        scoreboard.reset()
        snake.reset()
    
    #detect collision with tail
    for segment in snake.full_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset() 


screen.exitonclick()