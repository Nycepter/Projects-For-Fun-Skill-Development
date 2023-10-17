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

    print("You see a giant temple in the distance. It seems to be at the center of the island. There are also some ruins to the left of where you landed and to you right is the remains of an old pirate ship.")
    HasKey = False
    OpenLock = False
    while True:

        print("\nWhere would you like to go?")
        Choice1 = input(
            "Would you like to go to the 'temple', investigate the 'ruins' or look at the remains of the 'pirate ship'?\n")

        if Choice1 == "temple":
            print("\nAs you are heading towards the temple, you come across a sign that says 'TURN BACK NOW OR SUFFER'. You notice a trail leading from the sign into the woods.")
            Choice1_A = input(
                "Would you like to ignore the sign and continue to the 'temple', take the signs advice and 'turn back', or 'follow the trail' into the woods?\n")
            if Choice1_A == 'temple' and OpenLock == False:
                print(
                    "\nYou arrive at the temple! There is a sturdy gate locking the entrance. The gate has a key hole!")
                Choice1_A_1 = input(
                    "Would you like to 'enter key', or 'go back' to your boat?\n")
                if Choice1_A_1 == "enter key":
                    if HasKey == False:
                        print(
                            "\nYou do not have the key that goes to this lock, go find it!")
                        print("Now begone!")
                        continue
                    if HasKey == True:
                        OpenLock = True
                        print(
                            "\nAs you turn the key, the lock drops away revaling a screen that has an equation and a place for you to enter an answer.")
                        print("The equation is (4x3-6+1)3(12÷6+1).")
                        Choice1_A_2 = input(
                            "Would you like to 'enter an answer' or 'go back'?\n")
                        if Choice1_A_2 == "enter an answer":
                            Answer = input("\nWhat is your answer?\n")
                            if Answer == "2":
                                print(
                                    "\n\n\nThe gate opens up! You travel into the temple, before your very eyes is more treasure than you could have imagined in your wildest dreams!")
                                print("DING!!!!")
                                print("DING!!!!DING!!!!DING!!!!")
                                print("It's your alarm.")
                                print(
                                    "Evidently you could have imagined it in your wildest dreams...")
                                Awake = True
                                break
                            else:
                                print(
                                    "that answer is not correct! Please try again.")
                                print("Now away with you!")
                                continue
                        if Choice1_A_2 == "go back":
                            continue
            if Choice1_A == "temple" and OpenLock == True:
                print(
                    "\nThe lock is still open, you see a screen that has an equation and a place for you to enter an answer.")
                print("The equation is (4x3-6+1)3(12÷6+1).")
                Choice1_A_2 = input(
                    "Would you like to 'enter an answer' or 'go back'?\n")
                if Choice1_A_2 == "enter an answer":
                    Answer = input("\nWhat is your answer?\n")
                    if Answer == "2":
                        print(
                            "\n\n\nThe gate opens up! You travel into the temple, before your very eyes is more treasure than you could have imagined in your wildest dreams!")
                        print("DING!!!!")
                        print("DING!!!!DING!!!!DING!!!!")
                        print("It's your alarm.")
                        print(
                            "Evidently you could have imagined it in your wildest dreams...")
                        Awake = True
                        break
                    else:
                        print("that answer is not correct! Please try again.")
                        print("Now away with you!")
                        continue
                if Choice1_A_2 == "go back":
                    continue

            if Choice1_A == "follow the trail":
                print(
                    "\nAs you are walking along the trail, you somehow get lost and find yourself back where you began!")
                continue
            if Choice1_A == "turn back":
                continue

        elif Choice1 == "ruins":
            print("\nThe ruins are mostly rubble, but as you are about to leave, you notice something that catches your eye. There is something engraved into the wall.'These operations once had order, now there is nothing but division amongst the ranks.' There does not seem to be anything else of note around the ruins.")
            Choice1_B = input(
                "there is nothing left to do here, you should 'go back'.\n")
            if Choice1_B == "go back":
                continue

        elif Choice1 == "pirate ship" and HasKey == False:
            print("\nThe ship is in many pieces, most of which have degraded beyond recognition. However, the cabin seems to be unaturally preseerved. As you approach the door, something begins to appear on the door!\n '2B||!2B'\n  You get the sense that the door is waiting for you to respond...")
            Choice1_C = input(
                "Would you like to forget about this magical nonsense and 'go back' to your boat, or 'respond' to the cabin door?\n")
            if Choice1_C == "respond":
                Response = input("\nWhat would you like to say?\n")
                if Response == "that is the question":
                    print(
                        "\nThe door opens! The room is empty except for a key laying in the middle")
                    TakeKey = input(
                        "Would you like to take the key? 'yes' or 'no'\n")
                    if TakeKey == "yes":
                        HasKey = True
                        print("\nYou take the key, you look down to put it in your pocket and as you look up, you are suddenly standing in the same place you began. You can feel the key still in your pocket.")
                        continue
                    if TakeKey == "no":
                        print(
                            "\nYou hear a voice say, then there is no need for you to be here, goodbye!")
                        print("You find yourself back where you began!")
                        continue
                else:
                    print(
                        "\nThat is incorrect, better luck next time! Deus Ex Machina something someting, you are back where you started!")
                continue
            if Choice1_C == "go back":
                continue

        elif Choice1 == "pirate ship" and HasKey == True:
            print("The cabin you saw before is now gone! How strange...")
            print("Almost as strange as finding yourself back where you began, with no memory of how you got here!")
            continue

        elif Choice1 == "wake up":
            print(f"Nice try {Player.Name}, I dont think so.")
            continue
        else:
            print("Invlaid response, try again.")
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
print("The door opens, revealing a hallway that splits left and right. Directly in front of you is a hole in the wall that seems to be a tunnel to somewhere.")
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
            print("You manage to squeeze your way into the tunnel, at the end of the tunnel you find a piece of paper that says: ")
