from food import Food
from turtle import Turtle, Screen
import time
from snake import Snake
from score import Score, score
import pickle
from Functions import SaveData
from Functions import LoadData
from Functions import db
from Intro import Player, Set_High_Score
from Functions import fake_type, clear_console


def main():
    fake_type("Can you get a score of 20? Lets find out...")
    fake_type("Please press enter to continue...")
    input("> ")
    clear_console()
    # Screen settings
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.title("Nycepter's Pet Snake")
    screen.tracer(0)

# Game initialization value

    game_is_on = True

    snake = Snake()
    food = Food()
    user_score = Score()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.right, "d")

    # Game loop
    while game_is_on == True:
        if user_score.score == 5:
            db[Player.Name]["Completed"] += 1
            Set_High_Score(300)
            SaveData()
            game_is_on = False

        screen.update()
        time.sleep(.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            user_score.score += 1
            user_score.update_score()
            snake.extend()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            user_score.reset()
            snake.reset()

        for seg in snake.segments[2:]:
            if snake.head.distance(seg) < 10:
                user_score.reset()
                snake.reset()

    screen.bye()


if __name__ == "__main__":
    main()
