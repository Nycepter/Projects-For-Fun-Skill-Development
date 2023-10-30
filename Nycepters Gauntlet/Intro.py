import time
import random
import sys
import textwrap
from Functions import fake_type


class Player:
    Name = ""
    Age = 0
    Height = 0
    Gender = ""


def Run_Intro():
    Intro = """ _   _                      _            _       _____                   _   _      _   
| \ | |                    | |          ( )     |  __ \                 | | | |    | |  
|  \| |_   _  ___ ___ _ __ | |_ ___ _ __|/ ___  | |  \/ __ _ _   _ _ __ | |_| | ___| |_ 
| . ` | | | |/ __/ _ \ '_ \| __/ _ \ '__| / __| | | __ / _` | | | | '_ \| __| |/ _ \ __|
| |\  | |_| | (_|  __/ |_) | ||  __/ |    \__ \ | |_\ \ (_| | |_| | | | | |_| |  __/ |_ 
\_| \_/\__, |\___\___| .__/ \__\___|_|    |___/  \____/\__,_|\__,_|_| |_|\__|_|\___|\__|
        __/ |        | |                                                                
       |___/         |_|                                                                
"""

    fake_type(
        "\n\n\n Hello there... Before we get started, please tell me your name.")

    Player.Name = input("> ")
    fake_type("That is a stupid name, I think I will call you Bob.")
    fake_type(f"I am just kidding {Player.Name}, that is a good name!")
    fake_type("Just a few more questions and then we can get the ball rolling.")
    fake_type("What is your age in years?")
    Player.Age = int(input("> "))
    while Player.Age < 10 or Player.Age > 90:
        fake_type("Please provide a valid age...")
        Player.Age = int(input("> "))
    fake_type("What is your height in inches?")
    Player.Height = int(input("> "))
    while Player.Height < 30 or Player.Height > 72:
        fake_type("Please provide a valid height...")
        Player.Height = int(input("> "))

    fake_type("Are you male, or female?")
    Player.Gender = (input("> "))
    Player.Gender = Player.Gender.lower()
    while Player.Gender != "male" and Player.Gender != "female":
        fake_type("Please enter a valid gender...")
        Player.Gender = (input("> "))
        Player.Gender = Player.Gender.lower()
    fake_type(
        f"\n Thank you {Player.Name}, I would now like to welcome you to:")
    print(Intro)

    fake_type(
        f"\n\n\n I already know your name {Player.Name}, my name is Nycepter.")
    fake_type("I have a series of challenges for you!")
    fake_type(
        "But alas, you are currently in a strange place and need to find your way out.\n\n\n")
    result = [Player.Age, Player.Name, Player.Height, Player.Gender]
    return result
