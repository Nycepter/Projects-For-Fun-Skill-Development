import time
import random
import sys
import textwrap


def fake_type(words):
    words += "\n"
    for char in words:
        time.sleep(random.choice(
            [0.05]))
        sys.stdout.write(char)
        sys.stdout.flush(
        )
    time.sleep(.3)


class Player:
    Name = ""
    Age = 0
    Height = 0
    Gender = ""
