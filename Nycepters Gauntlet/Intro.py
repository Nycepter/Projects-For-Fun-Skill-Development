import pickle
import time
import random
import sys
import textwrap
from Functions import fake_type
import os
import subprocess
from Functions import clear_console
from prettytable import PrettyTable
from Functions import SaveData
from Functions import LoadData
from Functions import db
import sqlite3
import mysql.connector


class Player:
    Name = ""
    Age = 0
    Height = 0
    Gender = ""
    Score = 0
    Completed = 0
    Password = ""


Player.Name = ("")


def Set_High_Score(score):
    if Player.Name != "Aaron":
        Player.Score += score
        if db[f"{Player.Name}"]["Score"] < Player.Score:
            db[f"{Player.Name}"]["Score"] = Player.Score


def Show_High_Scores():
    table = PrettyTable()
    table.field_names = ["Name", "Score", "Completed"]
    sorted_keys = sorted(db.keys(), key=lambda x: db[x]['Score'], reverse=True)
    sorted_keys = sorted(
        db.keys(), key=lambda x: db[x]['Completed'], reverse=True)
    for key in sorted_keys:
        table.add_row([key, db[key]['Score'], db[key]['Completed']])

    print(table)


def Run_Intro():
    Intro = """ 
 _   _                      _            _       _____                   _   _      _   
| \ | |                    | |          ( )     |  __ \                 | | | |    | |  
|  \| |_   _  ___ ___ _ __ | |_ ___ _ __|/ ___  | |  \/ __ _ _   _ _ __ | |_| | ___| |_ 
| . ` | | | |/ __/ _ \ '_ \| __/ _ \ '__| / __| | | __ / _` | | | | '_ \| __| |/ _ \ __|
| |\  | |_| | (_|  __/ |_) | ||  __/ |    \__ \ | |_\ \ (_| | |_| | | | | |_| |  __/ |_ 
\_| \_/\__, |\___\___| .__/ \__\___|_|    |___/  \____/\__,_|\__,_|_| |_|\__|_|\___|\__|
        __/ |        | |                                                                
       |___/         |_|                                                                
"""

    fake_type(
        '\n\nPlease wait for the " > " to appear before typing your answers during the game.    \nIf you need to copy or paste something, right click. Do not use CTRL+C or CTRL+V as it will cause an input error.'
    )
    while True:
        fake_type(
            "\n\n\n Hello there... Before we get started, please enter your username."
        )

        Player.Name = input("> ")
        if Player.Name in db.keys():
            fake_type(
                "I see you have played before, please enter your password. If you have have not played before, this username is taken, please use a different one."
            )
            login = input("> ")
            if login == db[Player.Name]["Password"]:
                print(f"Welcome back, {Player.Name}.\n")
                print("High Scores:")
                Show_High_Scores()
                fake_type("Please press enter to continue...")
                input("> ")
                clear_console()
                return
            else:
                print("Incorrect password.")
                continue
        else:
            break

    db[f"{Player.Name}"] = {
        'Age': 0,
        'Height': 0,
        'Gender': "",
        'Score': 0,
        'Completed': 0,
        'Password': ""
    }

    clear_console()
    Set_High_Score(10)
    fake_type("That is a stupid name, I think I will call you Bob.")
    fake_type(f"I am just kidding {Player.Name}, that is a good name!")
    fake_type("Just a few more questions and then we can get the ball rolling.")
    fake_type("Please create a password.")
    db[Player.Name]["Password"] = input("> ")
    fake_type("What is your age in years?")
    Player.Age = int(input("> "))
    db[f"{Player.Name}"]["Age"] = Player.Age
    clear_console()
    while Player.Age < 10 or Player.Age > 90:
        fake_type("Please provide a valid age...")
        Player.Age = int(input("> "))
    try:
        fake_type("What is your height in inches?")
        Player.Height = int(input("> "))
        db[f"{Player.Name}"]["Height"] = Player.Height
        clear_console()
        while Player.Height < 30 or Player.Height > 72:
            fake_type("Please provide a valid height...")
            Player.Height = int(input("> "))
    except:
        fake_type(
            "Input Error, please only put in inches. i.e. 5 foot 5 is 65 inches.")

    fake_type("Are you male, or female?")
    Player.Gender = (input("> "))
    db[f"{Player.Name}"]["Gender"] = Player.Gender
    clear_console()
    Player.Gender = Player.Gender.lower()
    while Player.Gender != "male" and Player.Gender != "female":
        fake_type("Please enter a valid gender...")
        Player.Gender = (input("> "))
        Player.Gender = Player.Gender.lower()
    fake_type(
        f"\n Thank you {Player.Name}, I would now like to welcome you to:")
    print(Intro)
    print("High Scores:")
    Show_High_Scores()
    fake_type(
        f"\n\n\n I already know your name {Player.Name}, my name is Nycepter.")
    fake_type("I have a series of challenges for you!")
    fake_type(
        "But alas, you are currently in a strange place and need to find your way out.\n\n\n"
    )
    fake_type("Please press enter to continue...")
    input("> ")
    clear_console()
    db[Player.Name]["Completed"] += 1
    SaveData()
    return
