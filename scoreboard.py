from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(self.xcor(), 260)
        self.update_score()

    def update_score(self):
        self.write("Score: " + str(self.score), move=False, align=ALIGNMENT, font=FONT)
    def increment_score(self):
        self.clear()
        self.score += 1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)

