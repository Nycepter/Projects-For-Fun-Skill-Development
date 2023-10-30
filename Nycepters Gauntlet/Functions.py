import time
import random
import sys
import textwrap


def fake_type(words):
    words += "\n"
    for char in words:
        time.sleep(random.choice(
            [0.00]))
        sys.stdout.write(char)
        sys.stdout.flush(
        )
    time.sleep(0)
