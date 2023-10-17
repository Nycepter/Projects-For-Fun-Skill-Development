import time
import random
import sys
import textwrap


def fake_type(words):
    words += "\n"
    for char in words:
        time.sleep(random.choice(
            [0.3, 0.11, 0.08, 0.07, 0.07, 0.07, 0.06, 0.06, 0.05, 0.01]))
        sys.stdout.write(char)
        sys.stdout.flush(

        )
    time.sleep(1)


class Player:
    Name = ""
    Age = 0
    Height = 0
    Gender = ""


Intro = """ _   _                      _            _       _____                   _   _      _   
| \ | |                    | |          ( )     |  __ \                 | | | |    | |  
|  \| |_   _  ___ ___ _ __ | |_ ___ _ __|/ ___  | |  \/ __ _ _   _ _ __ | |_| | ___| |_ 
| . ` | | | |/ __/ _ \ '_ \| __/ _ \ '__| / __| | | __ / _` | | | | '_ \| __| |/ _ \ __|
| |\  | |_| | (_|  __/ |_) | ||  __/ |    \__ \ | |_\ \ (_| | |_| | | | | |_| |  __/ |_ 
\_| \_/\__, |\___\___| .__/ \__\___|_|    |___/  \____/\__,_|\__,_|_| |_|\__|_|\___|\__|
        __/ |        | |                                                                
       |___/         |_|                                                                
"""


fake_type("\n\n\n Hello there... Before we get started, please tell me your name.")
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
fake_type(f"\n Thank you {Player.Name}, I would now like to welcome you to:")
print(Intro)

fake_type(
    f"\n\n\n I already know your name {Player.Name}, my name is Nycepter.")
fake_type("I have a series of challenges for you!")
fake_type(
    "But alas, you are currently in a strange place and need to find your way out.\n\n\n")
Awake = False

while Awake == False:

    fake_type("You see a giant temple in the distance. It seems to be at the center of the island. There are also some ruins to the left of where you landed and to you right is the remains of an old pirate ship.")
    HasKey = False
    OpenLock = False
    while True:

        fake_type("\nWhere would you like to go?")
        Choice1 = input(
            "Would you like to go to the 'temple', investigate the 'ruins' or look at the remains of the 'pirate ship'?\n")

        if Choice1 == "temple":
            fake_type("\nAs you are heading towards the temple, you come across a sign that says 'TURN BACK NOW OR SUFFER'. You notice a trail leading from the sign into the woods.")
            Choice1_A = input(
                "Would you like to ignore the sign and continue to the 'temple', take the signs advice and 'turn back', or 'follow the trail' into the woods?\n")
            if Choice1_A == 'temple' and OpenLock == False:
                fake_type(
                    "\nYou arrive at the temple! There is a sturdy gate locking the entrance. The gate has a key hole!")
                Choice1_A_1 = input(
                    "Would you like to 'enter key', or 'go back' to your boat?\n")
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
                        Choice1_A_2 = input(
                            "Would you like to 'enter an answer' or 'go back'?\n")
                        if Choice1_A_2 == "enter an answer":
                            Answer = input("\nWhat is your answer?\n")
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
                Choice1_A_2 = input(
                    "Would you like to 'enter an answer' or 'go back'?\n")
                if Choice1_A_2 == "enter an answer":
                    Answer = input("\nWhat is your answer?\n")
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
            Choice1_B = input(
                "there is nothing left to do here, you should 'go back'.\n")
            if Choice1_B == "go back":
                continue

        elif Choice1 == "pirate ship" and HasKey == False:
            fake_type("\nThe ship is in many pieces, most of which have degraded beyond recognition. However, the cabin seems to be unaturally preseerved. As you approach the door, something begins to appear on the door!\n '2B||!2B'\n  You get the sense that the door is waiting for you to respond...")
            Choice1_C = input(
                "Would you like to forget about this magical nonsense and 'go back' to your boat, or 'respond' to the cabin door?\n")
            if Choice1_C == "respond":
                Response = input("\nWhat would you like to say?\n")
                if Response == "that is the question":
                    fake_type(
                        "\nThe door opens! The room is empty except for a key laying in the middle")
                    TakeKey = input(
                        "Would you like to take the key? 'yes' or 'no'\n")
                    if TakeKey == "yes":
                        HasKey = True
                        fake_type(
                            "\nYou take the key, you look down to put it in your pocket and as you look up, you are suddenly standing in the same place you began. You can feel the key still in your pocket.")
                        continue
                    if TakeKey == "no":
                        fake_type(
                            "\nYou hear a voice say, then there is no need for you to be here, goodbye!")
                        fake_type("You find yourself back where you began!")
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


fake_type(f"\n\n\nLook at that, {Player.Name}! You are awake now!!!")
fake_type("I hope your dreams were pleasant.")
fake_type("As you look around you can see that you are alone in an empty room with only one door.")
fake_type("If you want the door to open, you will have to beat me in a game of Rock, Paper, Scissors!")
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
            "Would you like to choose 'Rock' 'Paper' or 'Scissors'?\n")
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
            break

fake_type("Dang, you caught me! You are more observant than I expected, this will be a fun game... You now have a choice to make.")
fake_type("The door opens, revealing a hallway that splits left and right. Directly in front of you is a hole in the wall that seems to be a tunnel to somewhere.")
Has_Portal_Key = False
Hallway_Complete = False
while Hallway_Complete == False:
    fake_type(
        "Do you want to go 'left', 'right', or go through the 'tunnel'? So many choices so little time")
    Hallway_Choice = input("> ")
    if Hallway_Choice == "tunnel":
        if Player.Height > 65:
            fake_type(
                f"Sorry {Player.Name}, it would seem that you are too big to fit through the opening! You will have to go another way.")
            continue
        else:
            fake_type("You manage to squeeze your way into the tunnel, at the end of the tunnel you find a piece of paper that says: Wow..... you sure are short!")
            fake_type("Well, that was anticlamactic, wasn't it?")
            fake_type("You crawl backwards and leave the tunnel.")
            continue
    elif Hallway_Choice == "left":
        fake_type(
            "You follow the hallway all the way until the end, there you find a portal.")
        fake_type(
            "A random portal in a strange place? There's no way this can be bad, go ahead!")
        fake_type("Do you got through the 'portal' or 'go back'?")
        Portal_Choice = input("> ")
        if Portal_Choice == "portal" and Has_Portal_Key == True:
            fake_type(
                "The keycard has to be put into the portal terminal, but when you try to put the card in the terminal says:")
            fake_type(
                "Error: Please finish current task before attempting another.")
            while True:
                fake_type(
                    "The current task on the screen says: Write a statement that subtracts 3 from i and then multiplies the result by 2.")
                statement = input("> ")
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
                        fake_type(
                            "You passed all the tests, the portal is now ready to use.")
                        fake_type("Would you like to go through the portal?")
                        Portal_Choice2 = input("> ")
                        if Portal_Choice2 == "yes":
                            fake_type("To be continued...")
                        else:
                            continue

                    else:
                        fake_type(
                            "One or more tests failed, please try again.")
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
                        "What column would you like to drop your token into? \n")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
                        print(f"Nycepter Score: {Nycepter_Score_Connect_Four}")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
                                    print("  A    B    C    D    E    F    G")
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
        Has_Portal_Key = True
        fake_type("I will take you back to the beginning now.")
        continue
