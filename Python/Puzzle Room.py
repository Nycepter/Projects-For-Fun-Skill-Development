print("You wake up in an unfamiliar room. There is a TV, a door, and a desk.")

while True:
    choice1 = input(
        "Do you investigate the 'TV', the 'Door', or the 'Desk'?\n")

    if choice1 == "Quit":
        break
    elif choice1 == "TV":
        print("The TV is currently off.")
        choice2 = input("Do you 'Turn the TV on' or 'Go back'?\n")

        if choice2 == "Turn the TV on":
            print("A hissing noise emanates from the TV as static erupts on the screen, slowly a picture comes into view, the number 13 flashes on the screen. All other channels are static. What would you like to do next?")
            continue
        elif choice2 == "Go back":
            continue
    elif choice1 == "Door":
        print("The door is locked by a digital lock that allows the input of three single-digit numbers.")
        choice3 = input("Do you 'Input code' or 'Go back'?\n")

        if choice3 == "Input code":
            number1 = int(input("Enter the first number\n"))
            number2 = int(input("Enter the second number\n"))
            number3 = int(input("Enter the third number\n"))
            sum = number1 + number2 + number3

            if sum == 20:
                print("You hear a click as the door is unlocked!")
                choice5 = input("Do you want to go through the door?\n")

                if choice5 == "Yes":
                    print(
                        "You push the door open, as you walk through you discover.... That you will have to wait for Chapter 2 ;) THANK YOU FOR PLAYING")
                    break
                elif choice5 == "No":
                    continue
        else:
            print("The lock flashes red, the combination you entered was incorrect.")
            continue

        if choice3 == "Go back":
            continue
    elif choice1 == "Desk":
        print("The desk has two drawers")
        choice6 = input(
            "Do you want to 'Open the top drawer', 'Open the bottom drawer', or 'Go Back'?\n")

        if choice6 == "Open the top drawer":
            print("The top drawer slides open to reveal that it is empty.")
            choice7 = input(
                "Do you want to 'Open the bottom drawer', or 'Go Back'?\n")

            if choice7 == "Open the bottom drawer":
                print(
                    'You find a piece of paper that says "The world has many wonders!" There is nothing more at the desk.')
                continue
            elif choice7 == "Go back":
                continue
        elif choice6 == "Open the bottom drawer":
            print('You find a piece of paper that says "The world has many wonders!" There is nothing more at the desk, what would you like to do next?')
            choice8 = input(
                "Do you want to 'Open the top drawer', or 'Go Back'?\n")

            if choice8 == "Open the top drawer":
                print("The top drawer slides open to reveal that it is empty. There is nothing more at the desk, what would you like to do next?")
                continue
            elif choice8 == "Go back":
                continue
        elif choice6 == "Go Back":
            continue
