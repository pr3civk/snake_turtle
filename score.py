from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./Snake/data_snake.txt", "r") as data:
            self.high_score = int(data.read())
        self.pu()
        self.color("grey")
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Current Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./Snake/data_snake.txt", "w") as data:
                    data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


