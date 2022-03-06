import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

# start = False
screen = Screen()
screen.bgcolor('black')
screen.title('Snake Game')
screen.setup(width=600, height=600)
screen.tracer(0)

lily = Snake()
food = Food()
score = Score()

if score.ready():
    score.clear()


def start_game():
    start = True
    while start:
        screen.update()
        time.sleep(0.15)
        lily.move()

        #     Detect collision with food
        if lily.head.distance(food) < 19:
            print("non nom nom")
            food.relocate()
            lily.extend()
            score.add_score()

        #     Detect collision with wall
        if lily.head.xcor() > 290 or lily.head.xcor() < -290 or lily.head.ycor() > 290 or lily.head.ycor() < -290:
            start = False
            score.game_over()

        #     Detect collision with food
        for segment in lily.snake[1:]:
            if lily.head.distance(segment) < 10:
                start = False
                score.game_over()

        screen.update()


screen.listen()
screen.onkey(start_game, 'y')
screen.onkey(lily.up, 'Up')
screen.onkey(lily.down, 'Down')
screen.onkey(lily.move_left, 'Left')
screen.onkey(lily.move_right, 'Right')

screen.exitonclick()
