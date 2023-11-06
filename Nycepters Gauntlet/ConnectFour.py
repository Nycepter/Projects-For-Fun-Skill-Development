import time
import random
import sys
import textwrap
from Intro import Player, Set_High_Score
from Functions import fake_type
import os
import subprocess
from Functions import clear_console
from replit import db


def Connect_Four():

    fake_type("Dang, you caught me! You are more observant than I expected, this will be a fun game... You now have a choice to make.")
    fake_type("The door opens, revealing a hallway that splits left and right. Directly in front of you is a hole in the wall that seems to be a tunnel to somewhere.")
    Has_Portal_Key = False
    Hallway_Complete = False
    while Hallway_Complete == False:
        fake_type(
            "Do you want to go 'left', 'right', or go through the 'tunnel'? So many choices so little time")
        Hallway_Choice = input("> ")
        clear_console()
        if Hallway_Choice == "tunnel":
            if Player.Height > 65:
                fake_type(
                    f"Sorry {Player.Name}, it would seem that you are too big to fit through the opening! You will have to go another way.")

                continue
            else:
                fake_type(
                    "You manage to squeeze your way into the tunnel, at the end of the tunnel you find a piece of paper that says: Wow..... you sure are short!")
                fake_type("Well, that was anticlamactic, wasn't it?")
                fake_type("You crawl backwards and leave the tunnel.")

                continue
        elif Hallway_Choice == "left":
            fake_type(
                "You follow the hallway all the way until the end, there you find a portal.")
            fake_type(
                "A random portal in a strange place? There's no way this can be bad, go ahead!")
            fake_type("Do you go through the 'portal' or 'go back'?")
            Portal_Choice = input("> ")
            clear_console()
            if Portal_Choice == "portal" and Has_Portal_Key == True:
                fake_type(
                    "The keycard has to be put into the portal terminal, but when you try to put the card in the terminal says:")
                fake_type(
                    "Error: Please finish current task before attempting another.")
                while True:
                    fake_type(
                        "The current task on the screen says: Write a statement that subtracts 3 from i and then multiplies the result by 2. Please note that if you want to multiply, you have to use the * symbol")
                    statement = input("> ")
                    clear_console()
                    try:
                        for i in range(20, 25):
                            statement
                            if i == 20 and eval(statement) == 34:
                                fake_type("Testing...")
                                fake_type("Test 1 passed.")
                                Passed1 = True
                            elif i == 20 and eval(statement) != 34:
                                fake_type("Test 1 failed.")
                                Passed1 = False
                            elif i == 21 and eval(statement) == 36:
                                fake_type("Testing...")
                                fake_type("Test 2 passed.")
                                Passed2 = True
                            elif i == 21 and eval(statement) != 36:
                                fake_type("Test 2 failed.")
                                Passed2 = False
                            elif i == 22 and eval(statement) == 38:
                                fake_type("Testing...")
                                fake_type("Test 3 passed.")
                                Passed3 = True
                            elif i == 22 and eval(statement) != 38:
                                fake_type("Test 3 failed.")
                                Passed3 = False
                            elif i == 23 and eval(statement) == 40:
                                fake_type("Testing...")
                                fake_type("Test 4 passed.")
                                Passed4 = True
                            elif i == 23 and eval(statement) != 40:
                                fake_type("Test 4 failed.")
                                Passed4 = False
                            elif i == 24 and eval(statement) == 42:
                                fake_type("Testing...")
                                fake_type("Test 5 passed.")
                                Passed5 = True
                            elif i == 24 and eval(statement) != 42:
                                fake_type("Test 5 failed.")
                                Passed5 = False
                            else:
                                fake_type("Error, try again.")
                                continue
                    except:
                        print("Error, try again.")
                        continue

                    if Passed1 == True and Passed2 == True and Passed3 == True and Passed4 == True and Passed5 == True:
                        db[Player.Name]["Completed"] += 1
                        if Player.Score < 610:
                            Set_High_Score(200)
                        fake_type(
                            "You passed all the tests, the portal is now ready to use.")
                        fake_type("Would you like to go through the portal?")
                        Portal_Choice2 = input("> ")
                        clear_console()
                        if Portal_Choice2 == "yes":

                            return
                        else:
                            continue

                    else:
                        fake_type(
                            "One or more tests failed, please try again.")
                        continue
            if Portal_Choice == "go back":
                continue
            else:
                fake_type(
                    "You feel as though the portal is rejecting you for some reason, you suddenly find yourself back at the beginning of the hallway!")
                continue
        elif Hallway_Choice == "right":
            fake_type("You go down the hallway and find a locked box.")
            fake_type("The box is just begging to be opened...")
            fake_type(
                f"But, {Player.Name}, what kind of host would I be if I just gave things out willy nilly?")
            fake_type("If you want what is in the box, you will have to earn it! Let's say... You have to beat me at connect four, four times in a row, no cheating this time, I promise!")
            fake_type("Do you accept the challenge?")
            Challenge_Acceptance = input("> ")
            Player_Score = 0
            if Challenge_Acceptance == "yes":
                while Player_Score < 4:
                    Reset = False

                    Nycepter_Score_Connect_Four = 0
                    Line1 = ["_", "️_", "️_", "️_", "️_", "️_", "️_"]
                    Line2 = ["_", "_", "️_", "️_", "️_", "️_", "️_"]
                    Line3 = ["_️", "_️", "_️", "️_", "️_", "️_", "️_"]
                    Line4 = ["_️", "_️", "_️", "️_", "️_", "️_", "️_"]
                    Line5 = ["_️", "_️", "_️", "️_", "️_", "️_", "️_"]
                    Line6 = ["_️", "_️", "_️", "️_", "️_", "️_", "️_"]
                    Board = [Line6, Line5, Line4, Line3, Line2, Line1]
                    print("  A    B    C    D    E    F    G")
                    print(f"{Line1}\n{Line2}\n{Line3}\n{Line4}\n{Line5}\n{Line6}\n")
                    print("Let's play connect four!")
                    print(f"Your score: {Player_Score}")
                    print(f"Nycepter Score: {Nycepter_Score_Connect_Four}")

                    Moves = ["a", "b", "c", "d", "e", "f", "g"]

                    # X-Loop
                    while Player_Score < 4:
                        while Reset == True:
                            Line1 = ["_", "️_", "️_", "️_", "️_", "️_", "️_"]
                            Line2 = ["_", "_", "️_", "️_", "️_", "️_", "️_"]
                            Line3 = ["_️", "_️", "_️", "️_", "️_", "️_", "️_"]
                            Line4 = ["_️", "_️", "_️", "️_", "️_", "️_", "️_"]
                            Line5 = ["_️", "_️", "_️", "️_", "️_", "️_", "️_"]
                            Line6 = ["_️", "_️", "_️", "️_", "️_", "️_", "️_"]
                            Board = [Line6, Line5, Line4, Line3, Line2, Line1]
                            Reset = False
                            break

                        Position = input(
                            "What column would you like to drop your token into? \n> ")
                        Column = Position[0].lower()
                        if Column not in ["a", "b", "c", "d", "e", "f", "g"]:
                            print("Invalid column selection, please choose again.")
                            continue
                        Letter_Index = Moves.index(Column)

                        if Column == "a":
                            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":
                                                    print(
                                                        "This Column is full, please choose another.")
                                                    continue
                                                else:
                                                    Board[0][Letter_Index] = "X"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[1][Letter_Index] = "X"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[2][Letter_Index] = "X"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[3][Letter_Index] = "X"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[4][Letter_Index] = "X"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            else:
                                Board[5][Letter_Index] = "X"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                        elif Column == "b":
                            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":
                                                    print(
                                                        "This Column is full, please choose another.")
                                                    continue
                                                else:
                                                    Board[0][Letter_Index] = "X"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[1][Letter_Index] = "X"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[2][Letter_Index] = "X"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[3][Letter_Index] = "X"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[4][Letter_Index] = "X"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            else:
                                Board[5][Letter_Index] = "X"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                        elif Column == "c":
                            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":
                                                    print(
                                                        "This Column is full, please choose another.")
                                                    continue
                                                else:
                                                    Board[0][Letter_Index] = "X"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[1][Letter_Index] = "X"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[2][Letter_Index] = "X"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[3][Letter_Index] = "X"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[4][Letter_Index] = "X"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            else:
                                Board[5][Letter_Index] = "X"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                        elif Column == "d":
                            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":
                                                    print(
                                                        "This Column is full, please choose another.")
                                                    continue
                                                else:
                                                    Board[0][Letter_Index] = "X"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[1][Letter_Index] = "X"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[2][Letter_Index] = "X"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[3][Letter_Index] = "X"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[4][Letter_Index] = "X"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            else:
                                Board[5][Letter_Index] = "X"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                        elif Column == "e":
                            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":
                                                    print(
                                                        "This Column is full, please choose another.")
                                                    continue
                                                else:
                                                    Board[0][Letter_Index] = "X"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[1][Letter_Index] = "X"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[2][Letter_Index] = "X"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[3][Letter_Index] = "X"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[4][Letter_Index] = "X"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            else:
                                Board[5][Letter_Index] = "X"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                        elif Column == "f":
                            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":
                                                    print(
                                                        "This Column is full, please choose another.")
                                                    continue
                                                else:
                                                    Board[0][Letter_Index] = "X"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[1][Letter_Index] = "X"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[2][Letter_Index] = "X"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[3][Letter_Index] = "X"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[4][Letter_Index] = "X"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            else:
                                Board[5][Letter_Index] = "X"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                        elif Column == "g":
                            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":
                                                    print(
                                                        "This Column is full, please choose another.")
                                                    continue
                                                else:
                                                    Board[0][Letter_Index] = "X"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[1][Letter_Index] = "X"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[2][Letter_Index] = "X"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[3][Letter_Index] = "X"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[4][Letter_Index] = "X"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            else:
                                Board[5][Letter_Index] = "X"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                        if (Line1[0] == "X" and Line2[0] == "X" and Line3[0] == "X" and Line4[0] == "X") or (Line5[0] == "X" and Line2[0] == "X" and Line3[0] == "X" and Line4[0] == "X") or (Line5[0] == "X" and Line6[0] == "X" and Line3[0] == "X" and Line4[0] == "X") or (Line1[1] == "X" and Line2[1] == "X" and Line3[1] == "X" and Line4[1] == "X") or (Line5[1] == "X" and Line2[1] == "X" and Line3[1] == "X" and Line4[1] == "X") or (Line5[1] == "X" and Line6[1] == "X" and Line3[1] == "X" and Line4[1] == "X") or (Line1[2] == "X" and Line2[2] == "X" and Line3[2] == "X" and Line4[2] == "X") or (Line5[2] == "X" and Line2[2] == "X" and Line3[2] == "X" and Line4[2] == "X") or (Line5[2] == "X" and Line6[2] == "X" and Line3[2] == "X" and Line4[2] == "X") or (Line1[3] == "X" and Line2[3] == "X" and Line3[3] == "X" and Line4[3] == "X") or (Line5[3] == "X" and Line2[3] == "X" and Line3[3] == "X" and Line4[3] == "X") or (Line5[3] == "X" and Line6[3] == "X" and Line3[3] == "X" and Line4[3] == "X") or (Line1[4] == "X" and Line2[4] == "X" and Line3[4] == "X" and Line4[4] == "X") or (Line5[4] == "X" and Line2[4] == "X" and Line3[4] == "X" and Line4[4] == "X") or (Line5[4] == "X" and Line6[4] == "X" and Line3[4] == "X" and Line4[4] == "X") or (Line1[5] == "X" and Line2[5] == "X" and Line3[5] == "X" and Line4[5] == "X") or (Line5[5] == "X" and Line2[5] == "X" and Line3[5] == "X" and Line4[5] == "X") or (Line5[5] == "X" and Line6[5] == "X" and Line3[5] == "X" and Line4[5] == "X") or (Line1[6] == "X" and Line2[6] == "X" and Line3[6] == "X" and Line4[6] == "X") or (Line5[6] == "X" and Line2[6] == "X" and Line3[6] == "X" and Line4[6] == "X") or (Line5[6] == "X" and Line6[6] == "X" and Line3[6] == "X" and Line4[6] == "X") or (Line6[0] == "X" and Line6[1] == "X" and Line6[2] == "X" and Line6[3] == "X") or (Line6[4] == "X" and Line6[1] == "X" and Line6[2] == "X" and Line6[3] == "X") or (Line6[4] == "X" and Line6[5] == "X" and Line6[2] == "X" and Line6[3] == "X") or (Line6[4] == "X" and Line6[5] == "X" and Line6[6] == "X" and Line6[3] == "X") or (Line5[0] == "X" and Line5[1] == "X" and Line5[2] == "X" and Line5[3] == "X") or (Line5[4] == "X" and Line5[1] == "X" and Line5[2] == "X" and Line5[3] == "X") or (Line5[4] == "X" and Line5[5] == "X" and Line5[2] == "X" and Line5[3] == "X") or (Line5[4] == "X" and Line5[5] == "X" and Line5[6] == "X" and Line5[3] == "X") or (Line4[0] == "X" and Line4[1] == "X" and Line4[2] == "X" and Line4[3] == "X") or (Line4[4] == "X" and Line4[1] == "X" and Line4[2] == "X" and Line4[3] == "X") or (Line4[4] == "X" and Line4[5] == "X" and Line4[2] == "X" and Line4[3] == "X") or (Line4[4] == "X" and Line4[5] == "X" and Line4[6] == "X" and Line4[3] == "X") or (Line3[0] == "X" and Line3[1] == "X" and Line3[2] == "X" and Line3[3] == "X") or (Line3[4] == "X" and Line3[1] == "X" and Line3[2] == "X" and Line3[3] == "X") or (Line3[4] == "X" and Line3[5] == "X" and Line3[2] == "X" and Line3[3] == "X") or (Line3[4] == "X" and Line3[5] == "X" and Line3[6] == "X" and Line3[3] == "X") or (Line2[0] == "X" and Line2[1] == "X" and Line2[2] == "X" and Line2[3] == "X") or (Line2[4] == "X" and Line2[1] == "X" and Line2[2] == "X" and Line2[3] == "X") or (Line2[4] == "X" and Line2[5] == "X" and Line2[2] == "X" and Line2[3] == "X") or (Line2[4] == "X" and Line2[5] == "X" and Line2[6] == "X" and Line2[3] == "X") or (Line1[0] == "X" and Line1[1] == "X" and Line1[2] == "X" and Line1[3] == "X") or (Line1[4] == "X" and Line1[1] == "X" and Line1[2] == "X" and Line1[3] == "X") or (Line1[4] == "X" and Line1[5] == "X" and Line1[2] == "X" and Line1[3] == "X") or (Line1[4] == "X" and Line1[5] == "X" and Line1[6] == "X" and Line1[3] == "X") or (Line6[3] == "X" and Line5[4] == "X" and Line4[5] == "X" and Line3[6] == "X") or (Line5[3] == "X" and Line4[4] == "X" and Line3[5] == "X" and Line2[6] == "X") or (Line4[3] == "X" and Line3[4] == "X" and Line2[5] == "X" and Line1[6] == "X") or (Line6[2] == "X" and Line5[3] == "X" and Line4[4] == "X" and Line3[5] == "X") or (Line5[2] == "X" and Line4[3] == "X" and Line3[4] == "X" and Line2[5] == "X") or (Line4[2] == "X" and Line3[3] == "X" and Line2[4] == "X" and Line1[5] == "X") or (Line6[1] == "X" and Line5[2] == "X" and Line4[3] == "X" and Line3[4] == "X") or (Line5[1] == "X" and Line4[2] == "X" and Line3[3] == "X" and Line2[4] == "X") or (Line4[1] == "X" and Line3[2] == "X" and Line2[3] == "X" and Line1[4] == "X") or (Line6[0] == "X" and Line5[1] == "X" and Line4[2] == "X" and Line3[3] == "X") or (Line5[0] == "X" and Line4[1] == "X" and Line3[2] == "X" and Line2[3] == "X") or (Line4[0] == "X" and Line3[1] == "X" and Line2[2] == "X" and Line1[3] == "X") or (Line4[0] == "X" and Line3[1] == "X" and Line2[2] == "X" and Line1[3] == "X") or (Line5[0] == "X" and Line4[1] == "X" and Line3[2] == "X" and Line2[3] == "X") or (Line6[0] == "X" and Line5[1] == "X" and Line4[2] == "X" and Line3[3] == "X") or (Line4[1] == "X" and Line3[2] == "X" and Line2[3] == "X" and Line1[4] == "X") or (Line5[1] == "X" and Line4[2] == "X" and Line3[3] == "X" and Line2[4] == "X") or (Line6[1] == "X" and Line5[2] == "X" and Line4[3] == "X" and Line3[4] == "X") or (Line4[2] == "X" and Line3[3] == "X" and Line2[4] == "X" and Line1[5] == "X") or (Line5[2] == "X" and Line4[3] == "X" and Line3[4] == "X" and Line2[5] == "X") or (Line6[2] == "X" and Line5[3] == "X" and Line4[4] == "X" and Line3[5] == "X") or (Line4[3] == "X" and Line3[4] == "X" and Line2[5] == "X" and Line1[6] == "X") or (Line5[3] == "X" and Line4[4] == "X" and Line3[5] == "X" and Line2[6] == "X") or (Line6[3] == "X" and Line5[4] == "X" and Line4[5] == "X" and Line3[6] == "X"):

                            print("You Win!")
                            Reset = True
                            Player_Score += 1
                            print(f"Your score: {Player_Score}")
                            print(
                                f"Nycepter Score: {Nycepter_Score_Connect_Four}")
                            continue

                        # O-Loop
                        while True:

                            Position = random.choice(Moves)
                            Column = Position[0].lower()
                            Letter_Index = Moves.index(Column)
                            if Column == "a":
                                if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                    if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                        if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                            if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                                if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                    if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":
                                                        continue
                                                    else:
                                                        Board[0][Letter_Index] = "O"
                                                        print(
                                                            "  A    B    C    D    E    F    G")
                                                        print(
                                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                                else:
                                                    Board[1][Letter_Index] = "O"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[2][Letter_Index] = "O"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[3][Letter_Index] = "O"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[4][Letter_Index] = "O"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[5][Letter_Index] = "O"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            elif Column == "b":
                                if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                    if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                        if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                            if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                                if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                    if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                                        continue
                                                    else:
                                                        Board[0][Letter_Index] = "O"
                                                        print(
                                                            "  A    B    C    D    E    F    G")
                                                        print(
                                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                                else:
                                                    Board[1][Letter_Index] = "O"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[2][Letter_Index] = "O"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[3][Letter_Index] = "O"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[4][Letter_Index] = "O"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[5][Letter_Index] = "O"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            elif Column == "c":
                                if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                    if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                        if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                            if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                                if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                    if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                                        continue
                                                    else:
                                                        Board[0][Letter_Index] = "O"
                                                        print(
                                                            "  A    B    C    D    E    F    G")
                                                        print(
                                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                                else:
                                                    Board[1][Letter_Index] = "O"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[2][Letter_Index] = "O"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[3][Letter_Index] = "O"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[4][Letter_Index] = "O"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[5][Letter_Index] = "O"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            elif Column == "d":
                                if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                    if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                        if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                            if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                                if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                    if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                                        continue
                                                    else:
                                                        Board[0][Letter_Index] = "O"
                                                        print(
                                                            "  A    B    C    D    E    F    G")
                                                        print(
                                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                                else:
                                                    Board[1][Letter_Index] = "O"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[2][Letter_Index] = "O"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[3][Letter_Index] = "O"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[4][Letter_Index] = "O"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[5][Letter_Index] = "O"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            elif Column == "e":
                                if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                    if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                        if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                            if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                                if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                    if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                                        continue
                                                    else:
                                                        Board[0][Letter_Index] = "O"
                                                        print(
                                                            "  A    B    C    D    E    F    G")
                                                        print(
                                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                                else:
                                                    Board[1][Letter_Index] = ")"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[2][Letter_Index] = "O"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[3][Letter_Index] = "O"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[4][Letter_Index] = "O"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[5][Letter_Index] = "O"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            elif Column == "f":
                                if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                    if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                        if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                            if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                                if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                    if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                                        continue
                                                    else:
                                                        Board[0][Letter_Index] = "O"
                                                        print(
                                                            "  A    B    C    D    E    F    G")
                                                        print(
                                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                                else:
                                                    Board[1][Letter_Index] = "O"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[2][Letter_Index] = "O"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[3][Letter_Index] = "O"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[4][Letter_Index] = "O"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[5][Letter_Index] = "O"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            elif Column == "g":
                                if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                                    if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                                        if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                                            if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                                                if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                                    if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                                        continue
                                                    else:
                                                        Board[0][Letter_Index] = "O"
                                                        print(
                                                            "  A    B    C    D    E    F    G")
                                                        print(
                                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                                else:
                                                    Board[1][Letter_Index] = "O"
                                                    print(
                                                        "  A    B    C    D    E    F    G")
                                                    print(
                                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                            else:
                                                Board[2][Letter_Index] = "O"
                                                print(
                                                    "  A    B    C    D    E    F    G")
                                                print(
                                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                        else:
                                            Board[3][Letter_Index] = "O"
                                            print(
                                                "  A    B    C    D    E    F    G")
                                            print(
                                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                    else:
                                        Board[4][Letter_Index] = "O"
                                        print(
                                            "  A    B    C    D    E    F    G")
                                        print(
                                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                                else:
                                    Board[5][Letter_Index] = "O"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}\n")

                            if (Line1[0] == "X" and Line2[0] == "X" and Line3[0] == "O" and Line4[0] == "O") or (Line5[0] == "O" and Line2[0] == "O" and Line3[0] == "O" and Line4[0] == "O") or (Line5[0] == "O" and Line6[0] == "O" and Line3[0] == "O" and Line4[0] == "O") or (Line1[1] == "O" and Line2[1] == "O" and Line3[1] == "O" and Line4[1] == "O") or (Line5[1] == "O" and Line2[1] == "O" and Line3[1] == "O" and Line4[1] == "O") or (Line5[1] == "O" and Line6[1] == "O" and Line3[1] == "O" and Line4[1] == "O") or (Line1[2] == "O" and Line2[2] == "O" and Line3[2] == "O" and Line4[2] == "O") or (Line5[2] == "O" and Line2[2] == "O" and Line3[2] == "O" and Line4[2] == "O") or (Line5[2] == "O" and Line6[2] == "O" and Line3[2] == "O" and Line4[2] == "O") or (Line1[3] == "O" and Line2[3] == "O" and Line3[3] == "O" and Line4[3] == "O") or (Line5[3] == "O" and Line2[3] == "O" and Line3[3] == "O" and Line4[3] == "O") or (Line5[3] == "O" and Line6[3] == "O" and Line3[3] == "O" and Line4[3] == "O") or (Line1[4] == "O" and Line2[4] == "O" and Line3[4] == "O" and Line4[4] == "O") or (Line5[4] == "O" and Line2[4] == "O" and Line3[4] == "O" and Line4[4] == "O") or (Line5[4] == "O" and Line6[4] == "O" and Line3[4] == "O" and Line4[4] == "O") or (Line1[5] == "O" and Line2[5] == "O" and Line3[5] == "O" and Line4[5] == "O") or (Line5[5] == "O" and Line2[5] == "O" and Line3[5] == "O" and Line4[5] == "O") or (Line5[5] == "O" and Line6[5] == "O" and Line3[5] == "O" and Line4[5] == "O") or (Line1[6] == "O" and Line2[6] == "O" and Line3[6] == "O" and Line4[6] == "O") or (Line5[6] == "O" and Line2[6] == "O" and Line3[6] == "O" and Line4[6] == "O") or (Line5[6] == "O" and Line6[6] == "O" and Line3[6] == "O" and Line4[6] == "O") or (Line6[0] == "O" and Line6[1] == "O" and Line6[2] == "O" and Line6[3] == "O") or (Line6[4] == "O" and Line6[1] == "O" and Line6[2] == "O" and Line6[3] == "O") or (Line6[4] == "O" and Line6[5] == "O" and Line6[2] == "O" and Line6[3] == "O") or (Line6[4] == "O" and Line6[5] == "O" and Line6[6] == "O" and Line6[3] == "O") or (Line5[0] == "O" and Line5[1] == "O" and Line5[2] == "O" and Line5[3] == "O") or (Line5[4] == "O" and Line5[1] == "O" and Line5[2] == "O" and Line5[3] == "O") or (Line5[4] == "O" and Line5[5] == "O" and Line5[2] == "O" and Line5[3] == "O") or (Line5[4] == "O" and Line5[5] == "O" and Line5[6] == "O" and Line5[3] == "O") or (Line4[0] == "O" and Line4[1] == "O" and Line4[2] == "O" and Line4[3] == "O") or (Line4[4] == "O" and Line4[1] == "O" and Line4[2] == "O" and Line4[3] == "O") or (Line4[4] == "O" and Line4[5] == "O" and Line4[2] == "O" and Line4[3] == "O") or (Line4[4] == "O" and Line4[5] == "O" and Line4[6] == "O" and Line4[3] == "O") or (Line3[0] == "O" and Line3[1] == "O" and Line3[2] == "O" and Line3[3] == "O") or (Line3[4] == "O" and Line3[1] == "O" and Line3[2] == "O" and Line3[3] == "O") or (Line3[4] == "O" and Line3[5] == "O" and Line3[2] == "O" and Line3[3] == "O") or (Line3[4] == "O" and Line3[5] == "O" and Line3[6] == "O" and Line3[3] == "O") or (Line2[0] == "O" and Line2[1] == "O" and Line2[2] == "O" and Line2[3] == "O") or (Line2[4] == "O" and Line2[1] == "O" and Line2[2] == "O" and Line2[3] == "O") or (Line2[4] == "O" and Line2[5] == "O" and Line2[2] == "O" and Line2[3] == "O") or (Line2[4] == "O" and Line2[5] == "O" and Line2[6] == "O" and Line2[3] == "O") or (Line1[0] == "O" and Line1[1] == "O" and Line1[2] == "O" and Line1[3] == "O") or (Line1[4] == "O" and Line1[1] == "O" and Line1[2] == "O" and Line1[3] == "O") or (Line1[4] == "O" and Line1[5] == "O" and Line1[2] == "O" and Line1[3] == "O") or (Line1[4] == "O" and Line1[5] == "O" and Line1[6] == "O" and Line1[3] == "O") or (Line6[3] == "O" and Line5[4] == "O" and Line4[5] == "O" and Line3[6] == "O") or (Line5[3] == "O" and Line4[4] == "O" and Line3[5] == "O" and Line2[6] == "O") or (Line4[3] == "O" and Line3[4] == "O" and Line2[5] == "O" and Line1[6] == "O") or (Line6[2] == "O" and Line5[3] == "O" and Line4[4] == "O" and Line3[5] == "O") or (Line5[2] == "O" and Line4[3] == "O" and Line3[4] == "O" and Line2[5] == "O") or (Line4[2] == "O" and Line3[3] == "O" and Line2[4] == "O" and Line1[5] == "O") or (Line6[1] == "O" and Line5[2] == "O" and Line4[3] == "O" and Line3[4] == "O") or (Line5[1] == "O" and Line4[2] == "O" and Line3[3] == "O" and Line2[4] == "O") or (Line4[1] == "O" and Line3[2] == "O" and Line2[3] == "O" and Line1[4] == "O") or (Line6[0] == "O" and Line5[1] == "O" and Line4[2] == "O" and Line3[3] == "O") or (Line5[0] == "O" and Line4[1] == "O" and Line3[2] == "O" and Line2[3] == "O") or (Line4[0] == "O" and Line3[1] == "O" and Line2[2] == "O" and Line1[3] == "O") or (Line4[0] == "O" and Line3[1] == "O" and Line2[2] == "O" and Line1[3] == "O") or (Line5[0] == "O" and Line4[1] == "O" and Line3[2] == "O" and Line2[3] == "O") or (Line6[0] == "O" and Line5[1] == "O" and Line4[2] == "O" and Line3[3] == "O") or (Line4[1] == "O" and Line3[2] == "O" and Line2[3] == "O" and Line1[4] == "O") or (Line5[1] == "O" and Line4[2] == "O" and Line3[3] == "O" and Line2[4] == "O") or (Line6[1] == "O" and Line5[2] == "O" and Line4[3] == "O" and Line3[4] == "O") or (Line4[2] == "O" and Line3[3] == "O" and Line2[4] == "O" and Line1[5] == "O") or (Line5[2] == "O" and Line4[3] == "O" and Line3[4] == "O" and Line2[5] == "O") or (Line6[2] == "O" and Line5[3] == "O" and Line4[4] == "O" and Line3[5] == "O") or (Line4[3] == "O" and Line3[4] == "O" and Line2[5] == "O" and Line1[6] == "O") or (Line5[3] == "O" and Line4[4] == "O" and Line3[5] == "O" and Line2[6] == "O") or (Line6[3] == "O" and Line5[4] == "O" and Line4[5] == "O" and Line3[6] == "O"):
                                print("The Computer Wins!")
                                Reset = True
                                Nycepter_Score_Connect_Four += 1
                                Player_Score = 0
                                print(f"Your score: {Player_Score}")
                                print(
                                    f"Nycepter Score: {Nycepter_Score_Connect_Four}")
                                break
                            else:
                                break
            fake_type("Congratulations! The box is now unlocked.")
            fake_type("Inside the box is a heavy keycard that says: Portal Key.")
            if Player.Score < 710:
                Set_High_Score(100)
            Has_Portal_Key = True
            fake_type("I will take you back to the beginning now.")
            continue
