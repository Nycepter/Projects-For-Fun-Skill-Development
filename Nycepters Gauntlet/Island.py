import time
import random
import sys
import textwrap
from Intro import Player
from Functions import fake_type
import os
import subprocess
from Functions import clear_console


def Island_Game():
    Awake = False
    while Awake == False:

        fake_type("You see a giant temple in the distance. It seems to be at the center of the island. There are also some ruins to the left of where you landed and to you right is the remains of an old pirate ship.")
        HasKey = False
        OpenLock = False
        while True:

            fake_type("\nWhere would you like to go?")
            fake_type(
                "Would you like to go to the 'temple', investigate the 'ruins' or look at the remains of the 'pirate ship'?")
            Choice1 = input("> ")
            clear_console()
            if Choice1 == "temple":
                fake_type("\nAs you are heading towards the temple, you come across a sign that says 'TURN BACK NOW OR SUFFER'. You notice a trail leading from the sign into the woods.")
                fake_type(
                    "Would you like to ignore the sign and continue to the 'temple', take the signs advice and 'turn back', or 'follow the trail' into the woods?")
                Choice1_A = input("> ")
                clear_console()
                if Choice1_A == 'temple' and OpenLock == False:
                    fake_type(
                        "\nYou arrive at the temple! There is a sturdy gate locking the entrance. The gate has a key hole!")
                    fake_type(
                        "Would you like to 'enter key', or 'go back' to your boat?")
                    Choice1_A_1 = input("> ")
                    clear_console()
                    if Choice1_A_1 == "enter key":
                        if HasKey == False:
                            fake_type(
                                "\nYou do not have the key that goes to this lock, go find it!")
                            fake_type("Now begone!")
                            continue
                        if HasKey == True:
                            OpenLock = True
                            fake_type(
                                "\nAs you turn the key, the lock drops away revealing a screen that has an equation and a place for you to enter an answer.")
                            fake_type("The equation is (4x3-6+1)3(12÷6+1).")
                            fake_type(
                                "Would you like to 'answer' or 'go back'?")
                            Choice1_A_2 = input("> ")
                            clear_console()
                            if Choice1_A_2 == "answer":
                                fake_type(
                                    "\nWhat is your answer?")
                                Answer = input("> ")
                                clear_console()
                                if Answer == "2":
                                    fake_type(
                                        "\n\n\nThe gate opens up! You travel into the temple, before your very eyes is more treasure than you could have imagined in your wildest dreams!")
                                    fake_type("DING!!!!")
                                    fake_type("DING!!!!DING!!!!DING!!!!")
                                    fake_type("It's your alarm.")
                                    fake_type(
                                        "Evidently you could have imagined it in your wildest dreams...")
                                    Awake = True
                                    break
                                else:
                                    fake_type(
                                        "that answer is not correct! Please try again.")
                                    fake_type("Now away with you!")
                                    continue
                            if Choice1_A_2 == "go back":
                                continue
                if Choice1_A == "temple" and OpenLock == True:
                    fake_type(
                        "\nThe lock is still open, you see a screen that has an equation and a place for you to enter an answer.")
                    fake_type("The equation is (4x3-6+1)3(12÷6+1).")
                    fake_type(
                        "Would you like to 'answer' or 'go back'?")
                    Choice1_A_2 = input("> ")
                    clear_console()
                    if Choice1_A_2 == "answer":
                        Answer = fake_type("\nWhat is your answer?")
                        Answer = input("> ")
                        clear_console()
                        if Answer == "2":
                            fake_type(
                                "\n\n\nThe gate opens up! You travel into the temple, before your very eyes is more treasure than you could have imagined in your wildest dreams!")
                            fake_type("DING!!!!")
                            fake_type("DING!!!!DING!!!!DING!!!!")
                            fake_type("It's your alarm.")
                            fake_type(
                                "Evidently you could have imagined it in your wildest dreams...")
                            Awake = True
                            break
                        else:
                            fake_type(
                                "that answer is not correct! Please try again.")
                            fake_type("Now away with you!")
                            continue

                    if Choice1_A_2 == "go back":
                        continue

                if Choice1_A == "follow the trail":
                    fake_type(
                        "\nAs you are walking along the trail, you somehow get lost and find yourself back where you began!")
                    continue
                if Choice1_A == "turn back":
                    continue

            elif Choice1 == "ruins":
                fake_type("\nThe ruins are mostly rubble, but as you are about to leave, you notice something that catches your eye. There is something engraved into the wall.'These operations once had order, now there is nothing but division amongst the ranks.' There does not seem to be anything else of note around the ruins.")
                fake_type(
                    "there is nothing left to do here, you should 'go back'.")
                Choice1_B = input("> ")
                clear_console()
                if Choice1_B == "go back":
                    continue

            elif Choice1 == "pirate ship" and HasKey == False:
                fake_type("\nThe ship is in many pieces, most of which have degraded beyond recognition. However, the cabin seems to be unaturally preseerved. As you approach the door, something begins to appear on the door!\n '2B||!2B'\n  You get the sense that the door is waiting for you to respond...")
                fake_type(
                    "Would you like to forget about this magical nonsense and 'go back' to your boat, or 'respond' to the cabin door?")
                Choice1_C = input("> ")
                clear_console()
                if Choice1_C == "respond":
                    fake_type(
                        "\nWhat would you like to say?")
                    Response = input("> ")
                    clear_console()
                    if Response == "that is the question":
                        fake_type(
                            "\nThe door opens! The room is empty except for a key laying in the middle")
                        TakeKey = fake_type(
                            "Would you like to take the key? 'yes' or 'no'")
                        TakeKey = input("> ")
                        clear_console()
                        if TakeKey == "yes":
                            HasKey = True
                            fake_type(
                                "\nYou take the key, you look down to put it in your pocket and as you look up, you are suddenly standing in the same place you began. You can feel the key still in your pocket.")
                            continue
                        if TakeKey == "no":
                            fake_type(
                                "\nYou hear a voice say, then there is no need for you to be here, goodbye!")
                            fake_type(
                                "You find yourself back where you began!")
                            continue
                    else:
                        fake_type(
                            "\nThat is incorrect, better luck next time! Deus Ex Machina something someting, you are back where you started!")
                    continue
                if Choice1_C == "go back":
                    continue

            elif Choice1 == "pirate ship" and HasKey == True:
                fake_type("The cabin you saw before is now gone! How strange...")
                fake_type(
                    "Almost as strange as finding yourself back where you began, with no memory of how you got here!")
                continue

            elif Choice1 == "wake up":
                fake_type(f"Nice try {Player.Name}, I dont think so.")
                continue
            else:
                fake_type("Invlaid response, try again.")
                continue
