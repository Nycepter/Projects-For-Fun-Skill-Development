from turtle import Turtle
import os

score = 0


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.high_score = int(self.LoadData())
        self.score = 0
        self.penup()
        self.goto(0, 265)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))

    def update_score(self):
        self.SaveData()
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center",
                   font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def SaveData(self):
        try:
            with open('C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 20/High_Score.txt', 'w') as file:
                file.write(str(self.high_score))
        except Exception as e:
            print("Failed to save data:", e)

    def LoadData(self):
        if os.path.exists('C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 20/High_Score.txt'):
            with open("C:/Users/Nycepter/Documents/GitHub/100-Days-Of-Code-Python-/Day 20/High_Score.txt", mode="r") as file:
                return file.read()

        else:
            print("No saved data found.")
            pass

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center",
    #                font=("Arial", 24, "normal"))
