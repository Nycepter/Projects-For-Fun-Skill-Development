import random
line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
board = [line1, line2, line3]
print("    A     B     C")
print(f"1{line1}\n2{line2}\n3{line3}")
turn_counter = 0
moves = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

while True:

    position = input("Where do you want to go? \n")
    letter = position[0].lower()
    abc = ["a", "b", "c"]
    letter_index = abc.index(letter)
    number_index = int(position[1]) - 1
    if board[number_index][letter_index] == "X" or board[number_index][letter_index] == "O":
        print("This space is already taken, please choose another")
        continue
    else:
        board[number_index][letter_index] = "X"
        turn_counter += 1
        print("    A     B     C")
        print(f"1{line1}\n2{line2}\n3{line3}\n")

    if (line1[0] == "X" and line2[0] == "X" and line3[0] == "X") or (line1[1] == "X" and line2[1] == "X" and line3[1] == "X") or (line1[2] == "X" and line2[2] == "X" and line3[2] == "X") or (line1[0] == "X" and line1[1] == "X" and line1[2] == "X") or (line2[0] == "X" and line2[1] == "X" and line2[2] == "X") or (line3[0] == "X" and line3[1] == "X" and line3[2] == "X") or (line1[0] == "X" and line2[1] == "X" and line3[2] == "X") or (line1[2] == "X" and line2[1] == "X" and line3[0] == "X"):
        print("You win!")
        exit()

    elif turn_counter == 9:
        print("The game is a Draw!")
        exit()

    while True:

        position = random.choice(
            moves)

        letter = position[0].lower()
        abc = ["a", "b", "c"]
        letter_index = abc.index(letter)
        number_index = int(position[1]) - 1
        if board[number_index][letter_index] == "X" or board[number_index][letter_index] == "O":

            continue

        else:
            board[number_index][letter_index] = "O"
            turn_counter += 1
            print("\n")
            print(f"Rando puts their 'O' on {position}. \n")
            print("    A     B     C")
            print(f"1{line1}\n2{line2}\n3{line3}\n")

        if (line1[0] == "O" and line2[0] == "O" and line3[0] == "O") or (line1[1] == "O" and line2[1] == "O" and line3[1] == "O") or (line1[2] == "O" and line2[2] == "O" and line3[2] == "O") or (line1[0] == "O" and line1[1] == "O" and line1[2] == "O") or (line2[0] == "O" and line2[1] == "O" and line2[2] == "O") or (line3[0] == "O" and line3[1] == "O" and line3[2] == "O") or (line1[0] == "O" and line2[1] == "O" and line3[2] == "O") or (line1[2] == "O" and line2[1] == "O" and line3[0] == "O"):
            print("Rando wins!")
            exit()
        elif turn_counter == 9:
            print("The game is a Draw!")
            exit()
        else:
            break
        
