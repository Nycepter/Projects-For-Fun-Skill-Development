import time
import random
import sys
import textwrap
import os
from Intro import Player, Set_High_Score
from Functions import fake_type
from Functions import clear_console
from Functions import Hangman
from Functions import alphabet
from Functions import encrypt
from Functions import decrypt
from Functions import encrypt2
import pickle
from Functions import SaveData
from Functions import LoadData
import pickle
from Functions import SaveData
from Functions import LoadData
from Functions import db
import sqlite3
import mysql.connector
# fake_type(input("\n> ").lower())


def Haunted_School():

    fake_type("You stumble out of the portal, into some kind of classroom.")

    fake_type(
        "After orienting yourself, you can tell that this classroom has not been used in a very long time."
    )

    fake_type(
        "A thich layer of dust covers everthing, some of the desks are turned over, and there are boards covering the window on the door."
    )

    while True:
        Has_Door_Key = False
        Has_Battery = False
        Has_USB = False
        Has_Crowbar = False
        Door_open = False
        Locker_Open = False
        Password = "1234561234531235623213216413516841561698161968188961"
        Exit_Unlocked = False
        Battery_In_Laptop = False

        while True:
            fake_type("Do you want to 'look around' or 'open the door'?")
            Choice1 = input("> ").lower()
            clear_console()
            if Choice1 == "look around":
                fake_type(
                    "Walking around the room you notice a few things of interest. The teachers desk is pushed into the corner. A single locker locker lies on the back wall, it seems rather out of place. There is also backpack on the floor by the locker."
                )
                while True:
                    fake_type(
                        "Would you like to look at the 'desk', 'locker', 'backpack', or 'go back'?"
                    )
                    Choice2 = (input("> ").lower())
                    clear_console()
                    if Choice2 == "desk":
                        while True:
                            fake_type(
                                "You walk over to the desk, it is covered in scratches and gouges. There are two drawers on the front of the desk, one on the left and one on the right."
                            )
                            fake_type(
                                "Would you like to open the 'left drawer', 'right drawer', or 'go back'?"
                            )
                            Choice3 = input("> ").lower()
                            clear_console()
                            if Choice3 == "left drawer" and Has_Battery == False:
                                fake_type(
                                    "You open the left drawer, inside you find a battery of some kind."
                                )
                                fake_type(
                                    "Would you like to take the battery?")
                                Choice4 = input("> ").lower()
                                clear_console()
                                if Choice4 == "yes":
                                    Has_Battery = True
                                    fake_type(
                                        "You take the battery and put it in your pocket.")
                                    continue
                                elif Choice4 == "no":
                                    continue
                                else:
                                    fake_type(
                                        "Invalid selection, please try again.\n")
                                continue
                            elif Choice3 == "left drawer" and Has_Battery == True:
                                fake_type("The drawer is empty")
                                continue

                            elif Choice3 == "right drawer" and Has_Door_Key == False:
                                fake_type(
                                    "You open the right drawer, inside you find a small key.")
                                fake_type("Would you like to take the key?")
                                Choice5 = input("> ").lower()
                                clear_console()
                                if Choice5 == "yes":
                                    Has_Door_Key = True
                                    fake_type(
                                        "You take the key and put it in your pocket.")
                                    continue
                                elif Choice5 == "no":
                                    continue
                                else:
                                    fake_type(
                                        "Invalid selection, please try again.\n")
                                    continue
                            elif Choice3 == "right drawer" and Has_Door_Key == True:
                                fake_type("The drawer is empty")
                                continue
                            elif Choice3 == "go back":
                                break
                            else:
                                fake_type(
                                    "Invalid selection, please try again.\n")
                                continue
                    elif Choice2 == "locker":
                        if Locker_Open == False:
                            fake_type(
                                "You walk over to the locker, it is locked, but it is old and rusty, perhaps a little force could open it..."
                            )
                            fake_type(
                                "Would you like to try and bust open the locker?")
                            Choice6 = input("> ").lower()
                            clear_console()
                            if (Choice6 == "yes" and Player.Gender
                                == "male") or (Choice6 == "yes" and Player.Gender == "female"
                                               and Has_Crowbar == True):
                                if Player.Gender == "female":
                                    Locker_Open = True
                                    fake_type(
                                        'You put the crowbar in the locker and give it a good yank, the door flies open and a skeleton falls out, the bones scattering as they crash to the ground. Scratched into the paint on the inside of the locker is "I go out on my own terms, I refuse to be a part of this sick game." At the bottom of the locker you notice a gun.'
                                    )

                                else:
                                    Locker_Open = True
                                    fake_type(
                                        'You grab the locker and give it a good yank, the door flies open and a skeleton falls out, the bones scattering as they crash to the ground. Scratched into the paint on the inside of the locker is "I go out on my own terms, I refuse to be a part of this sick game." At the bottom of the locker you notice a gun.'
                                    )
                            elif Choice6 == "yes" and Player.Gender == "female":
                                fake_type(
                                    "You grab the locker and give it a good yank, however you are not quite strong enough to force the locker open. Perhaps there is a tool around that can help you."
                                )
                                continue
                            elif Choice6 == "no":
                                continue
                            else:
                                fake_type(
                                    "Invalid selection, please try again.\n")
                                continue
                        elif Locker_Open == True:
                            fake_type("The locker is still open")
                            pass

                        while True:
                            fake_type(
                                "Would you like to investigate the 'gun' the 'skeleton' or 'go back'?"
                            )
                            Choice7 = input("> ").lower()
                            clear_console()
                            if Choice7 == "gun":
                                fake_type(
                                    "You pick up the gun, it is a revolver that has 5 bullets in the cylinder, but the chamber is empty. You can tell that due to age, the gun by this point either no longer works, or that if it does work, it wouldn't work safetly. It is best to leave it be."
                                )
                                continue
                            elif Choice7 == "skeleton":
                                fake_type(
                                    "You look at the skeleton, there is a hole in the right side of the skull. Tattered remains of clothing are still present."
                                )
                                fake_type(
                                    "Would you like to 'check the pockets' or 'go back'? ")
                                Choice8 = input("> ").lower()
                                clear_console()
                                if Choice8 == "check the pockets" and Has_USB == False:
                                    fake_type(
                                        "You check the pockets, inside you find a USB drive. I wonder if this still works? You put the USB drive in your pocket."
                                    )
                                    Has_USB = True
                                    continue
                                elif Choice8 == "check the pockets" and Has_USB == True:
                                    fake_type("The pockets are empty")
                                    continue
                                elif Choice8 == "go back":
                                    break
                                else:
                                    fake_type(
                                        "Invalid selection, please try again.\n")
                                    continue
                            elif Choice7 == "go back":
                                break
                            else:
                                fake_type(
                                    "Invalid selection, please try again.\n")
                                continue
                        continue

                    elif Choice2 == "backpack":
                        clear_console
                        if Player.Gender == "female" and Has_Crowbar == False:
                            fake_type(
                                "You open the backpack, inside there is a note that says 'The answer to the universe is the key.' There is also a crowbar."
                            )
                            fake_type("Would you like to take the crowbar?")
                            Choice9 = input("> ").lower()
                            clear_console()
                            if Choice9 == "yes":
                                Has_Crowbar = True
                                fake_type("You take the crowbar.")
                                continue
                            else:
                                break
                        else:
                            fake_type(
                                "You open the backpack, inside there is a note that says 'The answer to the universe is the key. There is nothing else in the backpack."
                            )
                            continue
                    elif Choice2 == "go back":
                        break
                    else:
                        fake_type("Invalid selection, please try again.\n")
                        continue

            elif Choice1 == "open the door" and Door_open == True:
                fake_type(
                    "The door is already open, would you like to leave the room?")
                Choice11 = input("> ").lower()
                clear_console()
                if Choice11 == "yes":
                    pass
                else:
                    continue

            elif Choice1 == "open the door" and Has_Door_Key == False:
                fake_type(
                    "You grasp the handle and attempt to turn it, you hear a slight rattle as the knob encounters the locking mechanism. You will need to find the key to open this door.\n"
                )
                continue
            elif Choice1 == "open the door" and Has_Door_Key == True:
                fake_type(
                    "You grasp the handle and attempt to turn it, you hear a slight rattle as the knob encounters the locking mechanism. Would you like to try the key you found?"
                )
                Choice10 = input("> ").lower()
                clear_console()
                if Choice10 == "yes":
                    Door_open = True
                    fake_type(
                        "As you turn the key, you hear a loud KLUNK as lock disengages, you pull the door open."
                    )
                    fake_type("Would you like to leave the room?")
                    Choice12 = input("> ").lower()
                    clear_console()
                    if Choice12 == "yes":
                        pass
                    else:
                        continue

                else:
                    continue

            else:
                fake_type("Invalid selection, please try again.\n")
                continue

            while Door_open == True:
                fake_type(
                    "You open the door, the hallway lights are flickering, and the walls are covered in blood. You can hear a faint sound of a radio playing in the distance. You can also see a sign that says 'Exit' in the distance. Would you like to 'go to the exit', 'investigate the radio', or 'go back' into the room?"
                )
                Choice13 = input("> ").lower()
                clear_console()
                if Choice13 == "go to the exit" and Exit_Unlocked == False:
                    fake_type(
                        "You walk towards the exit, as you get closer, you notice that the door is locked by am electronic lock. You will need to find a way to unlock the door."
                    )
                    continue
                elif Choice13 == "go to the exit" and Exit_Unlocked == True:
                    fake_type(
                        "You walk towards the exit, as you get closer, you notice that the door is now unlocked. Would you like to go through the exit door?"
                    )
                    Choice14 = input("> ").lower()
                    clear_console()
                    if Choice14 == "yes":
                        db[Player.Name]["Completed"] += 1
                        return
                    else:
                        continue
                elif Choice13 == "investigate the radio":
                    while True:
                        fake_type(
                            "You walk towards the music, there is a radio sitting on a table in the middle of a room. It is an old radio, it looks like it is from the 80's. The radio is playing a song, but it is very faint. You can't quite make out what the song is. You notice that the radio is sitting next to a laptop. \nWould you like to investigate the 'laptop' or 'go back'?"
                        )
                        Choice15 = input("> ").lower()
                        clear_console()
                        if Choice15 == "laptop" and Has_Battery == False:
                            fake_type(
                                "You open the laptop, it is dead. You will need to find a replacement battery to power it."
                            )
                            continue
                        elif Choice15 == "laptop" and Has_Battery == True and Battery_In_Laptop == True:
                            fake_type("The laptop is already powered on.")

                        elif Choice15 == "laptop" and Has_Battery == True and Battery_In_Laptop == False:
                            fake_type(
                                "You open the laptop, it is dead. It needs a replacement battery to power it."
                            )
                            fake_type(
                                "Would you like to insert the battery you found?")
                            Choice16 = input("> ").lower()
                            clear_console()
                            if Choice16 == "yes":
                                Battery_In_Laptop = True
                                fake_type(
                                    "You insert the battery, the laptop powers on.")
                            else:
                                continue
                        elif Choice15 == "go back":
                            break

                        if Has_USB == False:
                            while True:
                                fake_type(
                                    "On the desktop are various files, one of note is a file called 'Exit Door Controls'. Would you like to open the file?"
                                )
                                Choice17 = input("> ").lower()
                                clear_console()
                                if Choice17 == "yes":
                                    fake_type(
                                        "You open the file, it is asking for a password.")
                                    fake_type(
                                        "Would you like to enter the password?")
                                    Choice18 = input("> ").lower()
                                    clear_console()
                                    if Choice18 == "yes":
                                        fake_type("Please enter the password.")
                                        Password_attempt = input("> ").lower()
                                        clear_console()
                                        if Password_attempt == Password:
                                            fake_type(
                                                "The password is correct, the door unlocks.")
                                            Exit_Unlocked = True

                                            break
                                        else:
                                            fake_type(
                                                "The password is incorrect, please try again.")
                                            fake_type("Hint: Hangman")
                                            continue

                                    else:
                                        break

                                else:
                                    continue
                        elif Has_USB == True:
                            while True:
                                fake_type(
                                    "On the desktop are various files, one of note is a file called: Exit Door Controls. Would you like to open the 'controls' 'plugin the USB', or 'go back'? "
                                )
                                Choice19 = input("> ").lower()
                                clear_console()
                                if Choice19 == "controls":
                                    fake_type(
                                        "You open the file, it is asking for a password.")
                                    fake_type(
                                        "Would you like to enter the password?")
                                    Choice20 = input("> ").lower()
                                    clear_console()
                                    if Choice20 == "yes":
                                        fake_type("Please enter the password.")
                                        Password_attempt = input("> ").lower()
                                        clear_console()
                                        if Password_attempt == Password:
                                            fake_type(
                                                "The password is correct, the door unlocks.")
                                            if Exit_Unlocked == False:
                                                if Player.Score < 1210:
                                                    Set_High_Score(500)
                                                    SaveData()
                                            Exit_Unlocked = True
                                            break
                                        else:
                                            fake_type(
                                                "The password is incorrect, please try again.")
                                            fake_type("Hint: Hangman")
                                            continue

                                    else:
                                        continue
                                elif Choice19 == "plugin the usb":
                                    while True:
                                        fake_type(
                                            "You plug in the USB drive. It contains two files, one is a game file called 'hangman' and the other is a program called 'Encryption/Decryption'. Would you like to open the 'Hangman' game, the 'encryption' program, or 'go back'?"
                                        )
                                        Choice21 = input("> ").lower()
                                        clear_console()
                                        if Choice21 == "hangman":
                                            while True:
                                                Password = encrypt2(
                                                    Hangman(), 42)
                                                fake_type(
                                                    "Well that was a fun game, now back to the task at hand."
                                                )
                                                break

                                        elif Choice21 == "encryption":
                                            while True:
                                                choice = input(
                                                    "Would you like to 'encrypt', 'decrypt' a message, or 'go back'?\n"
                                                ).lower()
                                                clear_console()
                                                if choice == "encrypt":
                                                    encrypt(
                                                        input(
                                                            "\nEnter the message you would like to encrypt: \n"
                                                        ).lower(),
                                                        int(input("\nEnter the number key: \n")))
                                                    continue
                                                elif choice == "decrypt":
                                                    decrypt(
                                                        input(
                                                            "\nEnter the message you would like to decrypt: \n"
                                                        ).lower(),
                                                        int(input("\nEnter the number key: \n")))
                                                    continue
                                                elif choice == "go back":
                                                    break
                                                else:
                                                    print(
                                                        "\nError, please choose a valid option. \n")
                                                    continue

                                        elif Choice21 == "go back":
                                            break
                                        else:
                                            fake_type(
                                                "Invalid selection, please try again.\n")
                                            continue
                                elif Choice19 == "go back":
                                    break

                            continue
                        else:
                            continue
                elif Choice13 == "go back":
                    break
