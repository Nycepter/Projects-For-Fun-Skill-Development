import time
import random
import sys
import textwrap
from Functions import fake_type
from Intro import Run_Intro
from Island import Island_Game
from RPS import RPS
from ConnectFour import Connect_Four


class Player:
    Name = ""
    Age = 0
    Height = 0
    Gender = ""


Run_Intro()
Island_Game()
RPS()
Connect_Four()
print("Test")
