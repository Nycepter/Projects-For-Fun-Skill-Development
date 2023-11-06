import time
import random
import sys
import textwrap
from Intro import Player, Set_High_Score
from Functions import fake_type
import os
import subprocess
from Functions import clear_console
import pickle
from Functions import SaveData
from Functions import LoadData
from Functions import db


def RPS():

    fake_type(f"\n\n\nLook at that, {Player.Name}! You are awake now!!!")
    fake_type("I hope your dreams were pleasant.")
    fake_type(
        "As you look around you can see that you are alone in an empty room with only one door."
    )
    fake_type(
        "If you want the door to open, you will have to beat me in a game of Rock, Paper, Scissors!"
    )
    fake_type(f"Alright, lets go, {Player.Name} vs Nycepter!")
    Exposed = False

    while Exposed == False:
        Rock = '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    '''

        Paper = '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''

        Scissors = '''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    '''
        Computer_Choices = ["Rock", "Paper", "Scissors"]
        print("Let's play Rock, Paper, Scissors!\n")
        User_Score = 0
        Computer_Score = 0
        Draws = 0

        while True:
            print(f"Player Wins: {User_Score}")
            print(f"Nycepter Wins: {Computer_Score}")
            print(f"Draws: {Draws}")

            Prompt = input(
                "Would you like to choose 'Rock' 'Paper' or 'Scissors'?\n> ")
            User_Choice = Prompt.lower()
            if User_Choice == "rock":
                Computer_Choice = "paper"
            elif User_Choice == "paper":
                Computer_Choice = "scissors"
            else:
                Computer_Choice = "rock"
            if User_Choice == "rock":
                print(f"\nYou chose {User_Choice}. \n {Rock}\n")
            elif User_Choice == "paper":
                print(f"\nYou chose {User_Choice}. \n {Paper}\n")
            else:
                print(f"\nYou chose {User_Choice}. \n {Scissors}\n")

            if Computer_Choice == "rock":
                print(f"Nycepter chose {Computer_Choice}. \n {Rock}\n")
            elif Computer_Choice == "paper":
                print(f"Nycepter chose {Computer_Choice}. \n {Paper}\n")
            else:
                print(f"Nycepter chose {Computer_Choice}. \n {Scissors}\n")

            if User_Choice == "rock" and Computer_Choice == "paper":
                print("Nycepter wins!\n")
                Computer_Score += 1
                continue
            elif User_Choice == "rock" and Computer_Choice == "rock":
                print("It's a Draw, try again!\n")
                Draws += 1
                continue
            elif User_Choice == "rock" and Computer_Choice == "scissors":
                print('You win!\n')
                User_Score += 1
                continue
            elif User_Choice == "paper" and Computer_Choice == "paper":
                print("It's a Draw, try again!\n")
                Draws += 1
                continue
            elif User_Choice == "paper" and Computer_Choice == "rock":
                print("You win!\n")
                User_Score += 1
                continue
            elif User_Choice == "paper" and Computer_Choice == "scissors":
                print("Nycepter wins!\n")
                Computer_Score += 1
                continue
            elif User_Choice == "scissors" and Computer_Choice == "scissors":
                print("It's a Draw, try again!\n")
                Draws += 1
                continue
            elif User_Choice == "scissors" and Computer_Choice == "paper":
                print("You win!\n")
                User_Score += 1
                continue
            elif User_Choice == "scissors" and Computer_Choice == "rock":
                print("Nycepter wins!\n")
                Computer_Score += 1
                continue
            elif "cheat" in User_Choice or "cheater" in User_Choice or "cheating" in User_Choice:
                Exposed = True
                db[Player.Name]["Completed"] += 1
                if Player.Score < 410:
                    Set_High_Score(200)
                    SaveData()
                break
