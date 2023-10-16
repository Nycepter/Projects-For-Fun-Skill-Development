import random
Reset = False
Player_Score = 0
Computer_Score = 0
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
print(f"Computer score: {Computer_Score}")


Moves = ["a", "b", "c", "d", "e", "f", "g"]


# X-Loop
while True:
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

    Position = input("What column would you like to drop your token into? \n")
    Column = Position[0].lower()
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
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[1][Letter_Index] = "X"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[2][Letter_Index] = "X"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[3][Letter_Index] = "X"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[4][Letter_Index] = "X"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        else:
            Board[5][Letter_Index] = "X"
            print("  A    B    C    D    E    F    G")
            print(
                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

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
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[1][Letter_Index] = "X"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[2][Letter_Index] = "X"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[3][Letter_Index] = "X"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[4][Letter_Index] = "X"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        else:
            Board[5][Letter_Index] = "X"
            print("  A    B    C    D    E    F    G")
            print(
                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

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
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[1][Letter_Index] = "X"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[2][Letter_Index] = "X"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[3][Letter_Index] = "X"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[4][Letter_Index] = "X"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        else:
            Board[5][Letter_Index] = "X"
            print("  A    B    C    D    E    F    G")
            print(
                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

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
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[1][Letter_Index] = "X"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[2][Letter_Index] = "X"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[3][Letter_Index] = "X"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[4][Letter_Index] = "X"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        else:
            Board[5][Letter_Index] = "X"
            print("  A    B    C    D    E    F    G")
            print(
                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

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
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[1][Letter_Index] = "X"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[2][Letter_Index] = "X"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[3][Letter_Index] = "X"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[4][Letter_Index] = "X"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        else:
            Board[5][Letter_Index] = "X"
            print("  A    B    C    D    E    F    G")
            print(
                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

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
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[1][Letter_Index] = "X"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[2][Letter_Index] = "X"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[3][Letter_Index] = "X"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[4][Letter_Index] = "X"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        else:
            Board[5][Letter_Index] = "X"
            print("  A    B    C    D    E    F    G")
            print(
                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

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
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[1][Letter_Index] = "X"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[2][Letter_Index] = "X"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[3][Letter_Index] = "X"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[4][Letter_Index] = "X"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        else:
            Board[5][Letter_Index] = "X"
            print("  A    B    C    D    E    F    G")
            print(
                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

    if (Line1[0] == "X" and Line2[0] == "X" and Line3[0] == "X" and Line4[0] == "X") or (Line5[0] == "X" and Line2[0] == "X" and Line3[0] == "X" and Line4[0] == "X") or (Line5[0] == "X" and Line6[0] == "X" and Line3[0] == "X" and Line4[0] == "X") or (Line1[1] == "X" and Line2[1] == "X" and Line3[1] == "X" and Line4[1] == "X") or (Line5[1] == "X" and Line2[1] == "X" and Line3[1] == "X" and Line4[1] == "X") or (Line5[1] == "X" and Line6[1] == "X" and Line3[1] == "X" and Line4[1] == "X") or (Line1[2] == "X" and Line2[2] == "X" and Line3[2] == "X" and Line4[2] == "X") or (Line5[2] == "X" and Line2[2] == "X" and Line3[2] == "X" and Line4[2] == "X") or (Line5[2] == "X" and Line6[2] == "X" and Line3[2] == "X" and Line4[2] == "X") or (Line1[3] == "X" and Line2[3] == "X" and Line3[3] == "X" and Line4[3] == "X") or (Line5[3] == "X" and Line2[3] == "X" and Line3[3] == "X" and Line4[3] == "X") or (Line5[3] == "X" and Line6[3] == "X" and Line3[3] == "X" and Line4[3] == "X") or (Line1[4] == "X" and Line2[4] == "X" and Line3[4] == "X" and Line4[4] == "X") or (Line5[4] == "X" and Line2[4] == "X" and Line3[4] == "X" and Line4[4] == "X") or (Line5[4] == "X" and Line6[4] == "X" and Line3[4] == "X" and Line4[4] == "X") or (Line1[5] == "X" and Line2[5] == "X" and Line3[5] == "X" and Line4[5] == "X") or (Line5[5] == "X" and Line2[5] == "X" and Line3[5] == "X" and Line4[5] == "X") or (Line5[5] == "X" and Line6[5] == "X" and Line3[5] == "X" and Line4[5] == "X") or (Line1[6] == "X" and Line2[6] == "X" and Line3[6] == "X" and Line4[6] == "X") or (Line5[6] == "X" and Line2[6] == "X" and Line3[6] == "X" and Line4[6] == "X") or (Line5[6] == "X" and Line6[6] == "X" and Line3[6] == "X" and Line4[6] == "X") or (Line6[0] == "X" and Line6[1] == "X" and Line6[2] == "X" and Line6[3] == "X") or (Line6[4] == "X" and Line6[1] == "X" and Line6[2] == "X" and Line6[3] == "X") or (Line6[4] == "X" and Line6[5] == "X" and Line6[2] == "X" and Line6[3] == "X") or (Line6[4] == "X" and Line6[5] == "X" and Line6[6] == "X" and Line6[3] == "X") or (Line5[0] == "X" and Line5[1] == "X" and Line5[2] == "X" and Line5[3] == "X") or (Line5[4] == "X" and Line5[1] == "X" and Line5[2] == "X" and Line5[3] == "X") or (Line5[4] == "X" and Line5[5] == "X" and Line5[2] == "X" and Line5[3] == "X") or (Line5[4] == "X" and Line5[5] == "X" and Line5[6] == "X" and Line5[3] == "X") or (Line4[0] == "X" and Line4[1] == "X" and Line4[2] == "X" and Line4[3] == "X") or (Line4[4] == "X" and Line4[1] == "X" and Line4[2] == "X" and Line4[3] == "X") or (Line4[4] == "X" and Line4[5] == "X" and Line4[2] == "X" and Line4[3] == "X") or (Line4[4] == "X" and Line4[5] == "X" and Line4[6] == "X" and Line4[3] == "X") or (Line3[0] == "X" and Line3[1] == "X" and Line3[2] == "X" and Line3[3] == "X") or (Line3[4] == "X" and Line3[1] == "X" and Line3[2] == "X" and Line3[3] == "X") or (Line3[4] == "X" and Line3[5] == "X" and Line3[2] == "X" and Line3[3] == "X") or (Line3[4] == "X" and Line3[5] == "X" and Line3[6] == "X" and Line3[3] == "X") or (Line2[0] == "X" and Line2[1] == "X" and Line2[2] == "X" and Line2[3] == "X") or (Line2[4] == "X" and Line2[1] == "X" and Line2[2] == "X" and Line2[3] == "X") or (Line2[4] == "X" and Line2[5] == "X" and Line2[2] == "X" and Line2[3] == "X") or (Line2[4] == "X" and Line2[5] == "X" and Line2[6] == "X" and Line2[3] == "X") or (Line1[0] == "X" and Line1[1] == "X" and Line1[2] == "X" and Line1[3] == "X") or (Line1[4] == "X" and Line1[1] == "X" and Line1[2] == "X" and Line1[3] == "X") or (Line1[4] == "X" and Line1[5] == "X" and Line1[2] == "X" and Line1[3] == "X") or (Line1[4] == "X" and Line1[5] == "X" and Line1[6] == "X" and Line1[3] == "X") or (Line6[3] == "X" and Line5[4] == "X" and Line4[5] == "X" and Line3[6] == "X") or (Line5[3] == "X" and Line4[4] == "X" and Line3[5] == "X" and Line2[6] == "X") or (Line4[3] == "X" and Line3[4] == "X" and Line2[5] == "X" and Line1[6] == "X") or (Line6[2] == "X" and Line5[3] == "X" and Line4[4] == "X" and Line3[5] == "X") or (Line5[2] == "X" and Line4[3] == "X" and Line3[4] == "X" and Line2[5] == "X") or (Line4[2] == "X" and Line3[3] == "X" and Line2[4] == "X" and Line1[5] == "X") or (Line6[1] == "X" and Line5[2] == "X" and Line4[3] == "X" and Line3[4] == "X") or (Line5[1] == "X" and Line4[2] == "X" and Line3[3] == "X" and Line2[4] == "X") or (Line4[1] == "X" and Line3[2] == "X" and Line2[3] == "X" and Line1[4] == "X") or (Line6[0] == "X" and Line5[1] == "X" and Line4[2] == "X" and Line3[3] == "X") or (Line5[0] == "X" and Line4[1] == "X" and Line3[2] == "X" and Line2[3] == "X") or (Line4[0] == "X" and Line3[1] == "X" and Line2[2] == "X" and Line1[3] == "X") or (Line4[0] == "X" and Line3[1] == "X" and Line2[2] == "X" and Line1[3] == "X") or (Line5[0] == "X" and Line4[1] == "X" and Line3[2] == "X" and Line2[3] == "X") or (Line6[0] == "X" and Line5[1] == "X" and Line4[2] == "X" and Line3[3] == "X") or (Line4[1] == "X" and Line3[2] == "X" and Line2[3] == "X" and Line1[4] == "X") or (Line5[1] == "X" and Line4[2] == "X" and Line3[3] == "X" and Line2[4] == "X") or (Line6[1] == "X" and Line5[2] == "X" and Line4[3] == "X" and Line3[4] == "X") or (Line4[2] == "X" and Line3[3] == "X" and Line2[4] == "X" and Line1[5] == "X") or (Line5[2] == "X" and Line4[3] == "X" and Line3[4] == "X" and Line2[5] == "X") or (Line6[2] == "X" and Line5[3] == "X" and Line4[4] == "X" and Line3[5] == "X") or (Line4[3] == "X" and Line3[4] == "X" and Line2[5] == "X" and Line1[6] == "X") or (Line5[3] == "X" and Line4[4] == "X" and Line3[5] == "X" and Line2[6] == "X") or (Line6[3] == "X" and Line5[4] == "X" and Line4[5] == "X" and Line3[6] == "X"):

        print("You Win!")
        Reset = True
        Player_Score += 1
        print(f"Your score: {Player_Score}")
        print(f"Computer score: {Computer_Score}")
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
                                    break
                                else:
                                    Board[0][Letter_Index] = "O"
                                    print("  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                            else:
                                Board[1][Letter_Index] = "O"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[2][Letter_Index] = "O"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[3][Letter_Index] = "O"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[4][Letter_Index] = "O"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[5][Letter_Index] = "O"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        elif Column == "b":
            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                    break
                                else:
                                    Board[0][Letter_Index] = "O"
                                    print(
                                        "  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                            else:
                                Board[1][Letter_Index] = "O"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[2][Letter_Index] = "O"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[3][Letter_Index] = "O"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[4][Letter_Index] = "O"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[5][Letter_Index] = "O"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        elif Column == "c":
            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                    break
                                else:
                                    Board[0][Letter_Index] = "O"
                                    print(
                                        "  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                            else:
                                Board[1][Letter_Index] = "O"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[2][Letter_Index] = "O"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[3][Letter_Index] = "O"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[4][Letter_Index] = "O"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[5][Letter_Index] = "O"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        elif Column == "d":
            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                    break
                                else:
                                    Board[0][Letter_Index] = "O"
                                    print(
                                        "  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                            else:
                                Board[1][Letter_Index] = "O"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[2][Letter_Index] = "O"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[3][Letter_Index] = "O"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[4][Letter_Index] = "O"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[5][Letter_Index] = "O"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        elif Column == "e":
            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                    break
                                else:
                                    Board[0][Letter_Index] = "O"
                                    print(
                                        "  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                            else:
                                Board[1][Letter_Index] = ")"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[2][Letter_Index] = "O"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[3][Letter_Index] = "O"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[4][Letter_Index] = "O"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[5][Letter_Index] = "O"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        elif Column == "f":
            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                    break
                                else:
                                    Board[0][Letter_Index] = "O"
                                    print(
                                        "  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                            else:
                                Board[1][Letter_Index] = "O"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[2][Letter_Index] = "O"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[3][Letter_Index] = "O"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[4][Letter_Index] = "O"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[5][Letter_Index] = "O"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        elif Column == "g":
            if Board[5][Letter_Index] == "X" or Board[5][Letter_Index] == "O":
                if Board[4][Letter_Index] == "X" or Board[4][Letter_Index] == "O":
                    if Board[3][Letter_Index] == "X" or Board[3][Letter_Index] == "O":
                        if Board[2][Letter_Index] == "X" or Board[2][Letter_Index] == "O":
                            if Board[1][Letter_Index] == "X" or Board[1][Letter_Index] == "O":
                                if Board[0][Letter_Index] == "X" or Board[0][Letter_Index] == "O":

                                    break
                                else:
                                    Board[0][Letter_Index] = "O"
                                    print(
                                        "  A    B    C    D    E    F    G")
                                    print(
                                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                            else:
                                Board[1][Letter_Index] = "O"
                                print("  A    B    C    D    E    F    G")
                                print(
                                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                        else:
                            Board[2][Letter_Index] = "O"
                            print("  A    B    C    D    E    F    G")
                            print(
                                f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                    else:
                        Board[3][Letter_Index] = "O"
                        print("  A    B    C    D    E    F    G")
                        print(
                            f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

                else:
                    Board[4][Letter_Index] = "O"
                    print("  A    B    C    D    E    F    G")
                    print(
                        f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

            else:
                Board[5][Letter_Index] = "O"
                print("  A    B    C    D    E    F    G")
                print(
                    f"{Line6}\n{Line5}\n{Line4}\n{Line3}\n{Line2}\n{Line1}")

        if (Line1[0] == "X" and Line2[0] == "X" and Line3[0] == "O" and Line4[0] == "O") or (Line5[0] == "O" and Line2[0] == "O" and Line3[0] == "O" and Line4[0] == "O") or (Line5[0] == "O" and Line6[0] == "O" and Line3[0] == "O" and Line4[0] == "O") or (Line1[1] == "O" and Line2[1] == "O" and Line3[1] == "O" and Line4[1] == "O") or (Line5[1] == "O" and Line2[1] == "O" and Line3[1] == "O" and Line4[1] == "O") or (Line5[1] == "O" and Line6[1] == "O" and Line3[1] == "O" and Line4[1] == "O") or (Line1[2] == "O" and Line2[2] == "O" and Line3[2] == "O" and Line4[2] == "O") or (Line5[2] == "O" and Line2[2] == "O" and Line3[2] == "O" and Line4[2] == "O") or (Line5[2] == "O" and Line6[2] == "O" and Line3[2] == "O" and Line4[2] == "O") or (Line1[3] == "O" and Line2[3] == "O" and Line3[3] == "O" and Line4[3] == "O") or (Line5[3] == "O" and Line2[3] == "O" and Line3[3] == "O" and Line4[3] == "O") or (Line5[3] == "O" and Line6[3] == "O" and Line3[3] == "O" and Line4[3] == "O") or (Line1[4] == "O" and Line2[4] == "O" and Line3[4] == "O" and Line4[4] == "O") or (Line5[4] == "O" and Line2[4] == "O" and Line3[4] == "O" and Line4[4] == "O") or (Line5[4] == "O" and Line6[4] == "O" and Line3[4] == "O" and Line4[4] == "O") or (Line1[5] == "O" and Line2[5] == "O" and Line3[5] == "O" and Line4[5] == "O") or (Line5[5] == "O" and Line2[5] == "O" and Line3[5] == "O" and Line4[5] == "O") or (Line5[5] == "O" and Line6[5] == "O" and Line3[5] == "O" and Line4[5] == "O") or (Line1[6] == "O" and Line2[6] == "O" and Line3[6] == "O" and Line4[6] == "O") or (Line5[6] == "O" and Line2[6] == "O" and Line3[6] == "O" and Line4[6] == "O") or (Line5[6] == "O" and Line6[6] == "O" and Line3[6] == "O" and Line4[6] == "O") or (Line6[0] == "O" and Line6[1] == "O" and Line6[2] == "O" and Line6[3] == "O") or (Line6[4] == "O" and Line6[1] == "O" and Line6[2] == "O" and Line6[3] == "O") or (Line6[4] == "O" and Line6[5] == "O" and Line6[2] == "O" and Line6[3] == "O") or (Line6[4] == "O" and Line6[5] == "O" and Line6[6] == "O" and Line6[3] == "O") or (Line5[0] == "O" and Line5[1] == "O" and Line5[2] == "O" and Line5[3] == "O") or (Line5[4] == "O" and Line5[1] == "O" and Line5[2] == "O" and Line5[3] == "O") or (Line5[4] == "O" and Line5[5] == "O" and Line5[2] == "O" and Line5[3] == "O") or (Line5[4] == "O" and Line5[5] == "O" and Line5[6] == "O" and Line5[3] == "O") or (Line4[0] == "O" and Line4[1] == "O" and Line4[2] == "O" and Line4[3] == "O") or (Line4[4] == "O" and Line4[1] == "O" and Line4[2] == "O" and Line4[3] == "O") or (Line4[4] == "O" and Line4[5] == "O" and Line4[2] == "O" and Line4[3] == "O") or (Line4[4] == "O" and Line4[5] == "O" and Line4[6] == "O" and Line4[3] == "O") or (Line3[0] == "O" and Line3[1] == "O" and Line3[2] == "O" and Line3[3] == "O") or (Line3[4] == "O" and Line3[1] == "O" and Line3[2] == "O" and Line3[3] == "O") or (Line3[4] == "O" and Line3[5] == "O" and Line3[2] == "O" and Line3[3] == "O") or (Line3[4] == "O" and Line3[5] == "O" and Line3[6] == "O" and Line3[3] == "O") or (Line2[0] == "O" and Line2[1] == "O" and Line2[2] == "O" and Line2[3] == "O") or (Line2[4] == "O" and Line2[1] == "O" and Line2[2] == "O" and Line2[3] == "O") or (Line2[4] == "O" and Line2[5] == "O" and Line2[2] == "O" and Line2[3] == "O") or (Line2[4] == "O" and Line2[5] == "O" and Line2[6] == "O" and Line2[3] == "O") or (Line1[0] == "O" and Line1[1] == "O" and Line1[2] == "O" and Line1[3] == "O") or (Line1[4] == "O" and Line1[1] == "O" and Line1[2] == "O" and Line1[3] == "O") or (Line1[4] == "O" and Line1[5] == "O" and Line1[2] == "O" and Line1[3] == "O") or (Line1[4] == "O" and Line1[5] == "O" and Line1[6] == "O" and Line1[3] == "O") or (Line6[3] == "O" and Line5[4] == "O" and Line4[5] == "O" and Line3[6] == "O") or (Line5[3] == "O" and Line4[4] == "O" and Line3[5] == "O" and Line2[6] == "O") or (Line4[3] == "O" and Line3[4] == "O" and Line2[5] == "O" and Line1[6] == "O") or (Line6[2] == "O" and Line5[3] == "O" and Line4[4] == "O" and Line3[5] == "O") or (Line5[2] == "O" and Line4[3] == "O" and Line3[4] == "O" and Line2[5] == "O") or (Line4[2] == "O" and Line3[3] == "O" and Line2[4] == "O" and Line1[5] == "O") or (Line6[1] == "O" and Line5[2] == "O" and Line4[3] == "O" and Line3[4] == "O") or (Line5[1] == "O" and Line4[2] == "O" and Line3[3] == "O" and Line2[4] == "O") or (Line4[1] == "O" and Line3[2] == "O" and Line2[3] == "O" and Line1[4] == "O") or (Line6[0] == "O" and Line5[1] == "O" and Line4[2] == "O" and Line3[3] == "O") or (Line5[0] == "O" and Line4[1] == "O" and Line3[2] == "O" and Line2[3] == "O") or (Line4[0] == "O" and Line3[1] == "O" and Line2[2] == "O" and Line1[3] == "O") or (Line4[0] == "O" and Line3[1] == "O" and Line2[2] == "O" and Line1[3] == "O") or (Line5[0] == "O" and Line4[1] == "O" and Line3[2] == "O" and Line2[3] == "O") or (Line6[0] == "O" and Line5[1] == "O" and Line4[2] == "O" and Line3[3] == "O") or (Line4[1] == "O" and Line3[2] == "O" and Line2[3] == "O" and Line1[4] == "O") or (Line5[1] == "O" and Line4[2] == "O" and Line3[3] == "O" and Line2[4] == "O") or (Line6[1] == "O" and Line5[2] == "O" and Line4[3] == "O" and Line3[4] == "O") or (Line4[2] == "O" and Line3[3] == "O" and Line2[4] == "O" and Line1[5] == "O") or (Line5[2] == "O" and Line4[3] == "O" and Line3[4] == "O" and Line2[5] == "O") or (Line6[2] == "O" and Line5[3] == "O" and Line4[4] == "O" and Line3[5] == "O") or (Line4[3] == "O" and Line3[4] == "O" and Line2[5] == "O" and Line1[6] == "O") or (Line5[3] == "O" and Line4[4] == "O" and Line3[5] == "O" and Line2[6] == "O") or (Line6[3] == "O" and Line5[4] == "O" and Line4[5] == "O" and Line3[6] == "O"):
            print("The Computer Wins!")
            Reset = True
            Computer_Score += 1
            print(f"Your score: {Player_Score}")
            print(f"Computer score: {Computer_Score}")
            continue
        else:
            break
