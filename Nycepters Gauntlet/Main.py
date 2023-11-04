import time
import random
import sys
import textwrap
from Functions import fake_type
from Intro import Run_Intro
from Intro import Player
from Island import Island_Game
from RPS import RPS
from ConnectFour import Connect_Four
import os
import subprocess
from Functions import clear_console
from Horror import Haunted_School
from replit import db


def Load_Game(name):
    for key in db.keys():
        if key == name and db[key] < 200:
            Player.Score = db[key]
            Island_Game()
        elif key == name and 200 < db[key] < 400:
            Player.Score = db[key]
            RPS()
        elif key == name and 400 < db[key] < 700:
            Player.Score = db[key]
            Connect_Four()
        elif key == name and 700 < db[key] < 1200:
            Player.Score = db[key]
            Haunted_School()
        elif key == name and 1200 < db[key] < 2000:
            Player.Score = db[key]
            print("You will have to wait for the next chapter.")


Run_Intro()
Load_Game(Player.Name)

print("To be continued...")
