import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.tracer(0)

lily = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(lily.up, 'Up')
screen.onkey(lily.down, 'Down')
screen.onkey(lily.left, 'Left')
screen.onkey(lily.right, 'Right')

scoreboard = 0
start = True
while start:
    screen.update()
    time.sleep(0.1)
    lily.move()

#     Detect collision with food
    if lily.head.distance(food) < 15:
        print("non nom nom")
        food.relocate()
        lily.add_segment()

        #     Detect collision with food
        if lily.head.xcor() > 280 or lily.head.xcor() < -280 or lily.head.ycor() > 280 or lily.head.ycor() < -280:
            start = False
            score.game_over()

        score.add_score()
        screen.update()
screen.exitonclick()
