
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
import pickle
from Functions import SaveData
from Functions import LoadData
from Functions import db
import sqlite3
import mysql.connector


def Load_Game(name):
    for key in db.keys():
        if key == name and db[Player.Name]["Completed"] == 1:
            Player.Score = db[key]["Score"]
            Player.Age = db[key]["Age"]
            Player.Height = db[key]["Height"]
            Player.Gender = db[key]["Gender"]
            Island_Game()
            RPS()
            Connect_Four()
            Haunted_School()
        elif key == name and db[Player.Name]["Completed"] == 2:
            Player.Score = db[key]["Score"]
            Player.Age = db[key]["Age"]
            Player.Height = db[key]["Height"]
            Player.Gender = db[key]["Gender"]
            RPS()
            Connect_Four()
            Haunted_School()
        elif key == name and db[Player.Name]["Completed"] == 3:
            Player.Score = db[key]["Score"]
            Player.Age = db[key]["Age"]
            Player.Height = db[key]["Height"]
            Player.Gender = db[key]["Gender"]
            Connect_Four()
            Haunted_School()
        elif key == name and db[Player.Name]["Completed"] == 4:
            Player.Score = db[key]["Score"]
            Player.Age = db[key]["Age"]
            Player.Height = db[key]["Height"]
            Player.Gender = db[key]["Gender"]
            Haunted_School()
        elif key == name and db[Player.Name]["Completed"] == 5:
            Player.Score = db[key]["Score"]
            Player.Age = db[key]["Age"]
            Player.Height = db[key]["Height"]
            Player.Gender = db[key]["Gender"]
            print("You will have to wait for the next chapter.")


Run_Intro()
Load_Game(Player.Name)

print("To be continued...")
