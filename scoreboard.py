from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

with open("data.txt") as file:
    HIGH_SCORE = file.read()
    HIGH_SCORE = int(HIGH_SCORE)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.goto(self.xcor(), 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write("Score: " + str(self.score) + " High score: " + str(self.high_score), move=False, align=ALIGNMENT, font=FONT)
    def increment_score(self):
        self.score += 1
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as write:
            write.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

