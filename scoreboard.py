from turtle import Turtle
FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.score = 0
        self.goto(0, 260)
        self.hideturtle()
        self.scoreboard()

    def scoreboard(self):
        self.goto(0, 260)
        self.write(f'Score = {self.score}', False, align=ALIGNMENT, font=FONT)

    def ready(self):
        self.goto(0, 150)
        self.write("Ready to play? press 'y'", False, align=ALIGNMENT, font=FONT)
        # return True//

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.scoreboard()
