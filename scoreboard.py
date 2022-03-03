from turtle import Turtle
score = 0
FONT = ('Times', 20, 'normal')
ALIGNMENT = 'center'

class Score(Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.scoreboard()

    def scoreboard(self):
        self.write(f'Score = {score}', False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()
